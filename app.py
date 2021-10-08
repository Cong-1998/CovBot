import pandas as pd
from flask import Flask, request, make_response, jsonify, render_template
from flask_cors import CORS, cross_origin
import json
import os
import time
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from intent.spread_sub_intent import spread_sub
from intent.precautions_sub_intent import precautions_sub
from intent.symptom_intent import symptom
from intent.testing_intent import testing
from intent.child_intent import child
from intent.contact_intent import contact
from intent.common_intent import common
from intent.pet_intent import pet
from intent.vaccine_intent import vaccine
from covid_Faq.naive_bayes import translate
from statistic.data_request import country, state
from latest_news.cmco_news import extract_title, extract_link
from latest_news.vaccine_news import extrac_title, extrac_link
from latest_news.recommended_news import extra_title, extra_link

app = Flask(__name__)  # initialising the flask app with the name 'app'

# default route
@app.route('/')
def index():
    return 'Hello World!'

# function for responses
def results(req):
    # build a request object
    #req = request.get_json(force=True)

    # fetch action from json
    result = req.get("queryResult")
    intent = result.get("intent").get("displayName")
    parameters = result.get("parameters")
    query = result.get("queryText")

    # return a fulfillment response
    return get_response(intent, parameters, query)

def get_response(intent, parameters, query):

    # get current time
    startTime = time.time()
    
    if intent == "covid_searchcountry":
        cust_country = parameters.get("geo-country")

        if cust_country == "Malaysia":
            webhookresponse = country(cust_country)

            print(webhookresponse)

            return {
                "fulfillmentMessages": [
                    {
                        "text": {
                            "text": [
                                "Here are the details."
                            ]
                        }
                    },
                    {
                        "text": {
                            "text": [
                                webhookresponse
                            ] 
                        }
                    },
                    {
                        "payload": {
                            "richContent": [
                                [
                                      {
                                            "type": "chips",
                                            "options": [
                                                  {
                                                        "text": "State"
                                                  },
                                                  {
                                                        "text": "FAQ"
                                                  },
                                                  {
                                                        "text": "Latest News 📰"
                                                  }
                                            ]
                                      }
                                ]
                            ]
                        }
                    }
                ]
                    }
        else:
            return {
                "fulfillmentMessages": [
                    {
                        "text": {
                            "text": [
                                "Sorry, this is about COVID-19 in Malaysia."
                            ]
                        }
                    },
                    {
                        "payload": {
                            "richContent": [
                                [
                                      {
                                            "type": "chips",
                                            "options": [
                                                  {
                                                        "text": "Malaysia"
                                                  }
                                            ]
                                      }
                                ]
                            ]
                        }
                    }
                ]
                    }
        
    elif intent == "covid_searchstate":
        
        cust_state = parameters.get("geo-state")
        
        webhookresponse = state(cust_state)
        
        print(webhookresponse)

        executionTime = (time.time() - startTime)
        print('Execution time in seconds: ' + str(executionTime))
        
        return {
            "fulfillmentMessages": [
                {
                     "text": {
                         "text": [
                            "Here are the details."
                          ]
                     }
                },
                {
                    "text": {
                        "text": [
                            webhookresponse
                        ] 
                    }
                },
                {
                    "payload": {
                        "richContent": [
                            [
                                  {
                                        "type": "chips",
                                        "options": [
                                              {
                                                    "text": "Statistic"
                                              },
                                              {
                                                    "text": "FAQ"
                                              },
                                              {
                                                    "text": "Latest News 📰"
                                              }
                                        ]
                                  }
                            ]
                        ]
                    }
                }
            ]
                }
    
    elif intent == "news_cmco_intent":

        cmco_title = extract_title()
        cmco_link = extract_link()

        return {
            "fulfillmentMessages": [
                {
                    "text": {
                        "text": [
                            "Here are the news."
                        ]
                    }
                },
                {
                    "payload": {
                        "richContent": [
                            [   
                                {
                                    "image": {
                                        "src": {
                                            "rawUrl": ""
                                        }
                                    },
                                    "title": cmco_title[0],
                                    "actionLink": cmco_link[0],
                                    "subtitle": "",
                                    "type": "info"
                                }
                            ]
                          ]
                    }
                },
                {
                    "payload": {
                        "richContent": [
                            [
                                {
                                    "image": {
                                          "src": {
                                                "rawUrl": ""
                                          }
                                    },
                                    "title": cmco_title[1],
                                    "actionLink": cmco_link[1],
                                    "subtitle": "",
                                    "type": "info"
                                }
                            ]
                        ]
                    }
                },
                {
                    "payload": {
                        "richContent": [
                            [
                                {
                                    "image": {
                                          "src": {
                                                "rawUrl": ""
                                          }
                                    },
                                    "title": cmco_title[2],
                                    "actionLink": cmco_link[2],
                                    "subtitle": "",
                                    "type": "info"
                                }
                            ]
                        ]
                    }
                },
                {
                    "payload": {
                        "richContent": [
                            [
                                  {
                                        "type": "chips",
                                        "options": [
                                              {
                                                    "text": "recommended"
                                              },
                                              {
                                                    "text": "vaccine"
                                              },
                                              {
                                                    "text": "main menu"
                                              }
                                        ]
                                  }
                            ]
                        ]
                    }
                }
            ]
        }

    elif intent == "news_vaccine_intent":

        vaccine_title = extrac_title()
        vaccine_link = extrac_link()

        return {
            "fulfillmentMessages": [
                {
                    "text": {
                        "text": [
                            "Here are the news."
                        ]
                    }
                },
                {
                    "payload": {
                        "richContent": [
                            [   
                                {
                                    "image": {
                                        "src": {
                                            "rawUrl": ""
                                        }
                                    },
                                    "title": vaccine_title[0],
                                    "actionLink": vaccine_link[0],
                                    "subtitle": "",
                                    "type": "info"
                                }
                            ]
                          ]
                    }
                },
                {
                    "payload": {
                        "richContent": [
                            [
                                {
                                    "image": {
                                          "src": {
                                                "rawUrl": ""
                                          }
                                    },
                                    "title": vaccine_title[1],
                                    "actionLink": vaccine_link[1],
                                    "subtitle": "",
                                    "type": "info"
                                }
                            ]
                        ]
                    }
                },
                {
                    "payload": {
                        "richContent": [
                            [
                                {
                                    "image": {
                                          "src": {
                                                "rawUrl": ""
                                          }
                                    },
                                    "title": vaccine_title[2],
                                    "actionLink": vaccine_link[2],
                                    "subtitle": "",
                                    "type": "info"
                                }
                            ]
                        ]
                    }
                },
                {
                    "payload": {
                        "richContent": [
                            [
                                  {
                                        "type": "chips",
                                        "options": [
                                              {
                                                    "text": "recommended"
                                              },
                                              {
                                                    "text": "movement control"
                                              },
                                              {
                                                    "text": "main menu"
                                              }
                                        ]
                                  }
                            ]
                        ]
                    }
                }
            ]
        }

    elif intent == "news_recommended_intent":

        recommended_title = extra_title()
        recommended_link = extra_link()

        return {
            "fulfillmentMessages": [
                {
                    "text": {
                        "text": [
                            "Here are the news."
                        ]
                    }
                },
                {
                    "payload": {
                        "richContent": [
                            [   
                                {
                                    "image": {
                                        "src": {
                                            "rawUrl": ""
                                        }
                                    },
                                    "title": recommended_title[0],
                                    "actionLink": recommended_link[0],
                                    "subtitle": "",
                                    "type": "info"
                                }
                            ]
                          ]
                    }
                },
                {
                    "payload": {
                        "richContent": [
                            [
                                {
                                    "image": {
                                          "src": {
                                                "rawUrl": ""
                                          }
                                    },
                                    "title": recommended_title[1],
                                    "actionLink": recommended_link[1],
                                    "subtitle": "",
                                    "type": "info"
                                }
                            ]
                        ]
                    }
                },
                {
                    "payload": {
                        "richContent": [
                            [
                                {
                                    "image": {
                                          "src": {
                                                "rawUrl": ""
                                          }
                                    },
                                    "title": recommended_title[2],
                                    "actionLink": recommended_link[2],
                                    "subtitle": "",
                                    "type": "info"
                                }
                            ]
                        ]
                    }
                },
                {
                    "payload": {
                        "richContent": [
                            [
                                  {
                                        "type": "chips",
                                        "options": [
                                              {
                                                    "text": "vaccine"
                                              },
                                              {
                                                    "text": "movement control"
                                              },
                                              {
                                                    "text": "main menu"
                                              }
                                        ]
                                  }
                            ]
                        ]
                    }
                }
            ]
        }
    
    elif intent == "spread_sub_intent":
        webhookresponse = spread_sub(query)

        return webhookresponse

    elif intent == "precautions_sub_intent":
        webhookresponse = precautions_sub(query)

        return webhookresponse

    elif intent == "symptom_intent":
        webhookresponse = symptom(query)

        return webhookresponse

    elif intent == "testing_intent":
        webhookresponse = testing(query)

        return webhookresponse

    elif intent == "child_intent":
        webhookresponse = child(query)

        return webhookresponse

    elif intent == "contact_intent":
        webhookresponse = contact(query)

        return webhookresponse

    elif intent == "common_intent":
        webhookresponse = common(query)

        return webhookresponse
    
    elif intent == "pet_intent":
        webhookresponse = pet(query)

        return webhookresponse
    
    elif intent == "vaccine_intent":
        webhookresponse = vaccine(query)

        return webhookresponse
    
    elif intent == "Default Fallback Intent":
        webhookresponse = translate(query)
        
        return {
            "fulfillmentMessages": [
                {
                    "text": {
                        "text": [
                            webhookresponse
                        ] 
                    }
                },
                {
                    "payload": {
                        "richContent": [
                            [
                                  {
                                        "type": "chips",
                                        "options": [
                                              {
                                                    "text": "State"
                                              },
                                              {
                                                    "text": "FAQ"
                                              },
                                              {
                                                    "text": "Latest News 📰"
                                              }
                                        ]
                                  }
                            ]
                        ]
                    }
                }
            ]
                }

# create a route for webhook
@app.route('/webhook', methods=['POST'])
@cross_origin()
def webhook():
    # return response
    #return make_response(jsonify(results()))
    req = request.get_json(silent=True, force=True)
    res = results(req)
    res = json.dumps(res, indent=4)
    #print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r
    
# run the app
if __name__ == '__main__':
    port = 5000
    port = int(os.getenv('PORT', port))
    print("Starting app on port %d" % port)
    app.run()
