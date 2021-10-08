from covid_Faq.naive_bayes import translate

def contact(query):
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
                                            "text": "what is close contact?"
                                        },
                                        {
                                            "text": "What is contact tracing?"
                                        },
                                        {
                                            "text": "if i am a close contact, will i be tested for covid-19"
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
