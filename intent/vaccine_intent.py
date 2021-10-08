from covid_Faq.naive_bayes import translate

def vaccine(query):
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
                                        "text": "Is there a vaccine for COVID-19?"
                                    },
                                    {
                                        "text": "Is COVID-19 vaccine safe for everyone?"
                                    },
                                    {
                                        "text": "How much will the vaccine cost?"
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
    
