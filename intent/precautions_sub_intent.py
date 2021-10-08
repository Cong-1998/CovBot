from covid_Faq.naive_bayes import translate

def precautions_sub(query):
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
                                            "text": "Can I leave home?"
                                        },
                                        {
                                            "text": "Is it okay for me to donate blood?"
                                        },
                                        {
                                            "text": "Should I wear a face mask?"
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
