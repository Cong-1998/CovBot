from covid_Faq.naive_bayes import translate

def testing(query):
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
                                        "text": "Is home testing available?"
                                    },
                                    {
                                        "text": "Is COVID-19 test procedure painful?"
                                    },
                                    {
                                        "text": "How accurate is COVID-19 test?"
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
    
