from covid_Faq.naive_bayes import translate

def spread_sub(query):
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
                                            "text": "Can humans infected from animal?"
                                        },
                                        {
                                            "text": "Can coronavirus spread through swimming pool?"
                                        },
                                        {
                                            "text": "Can coronavirus stick to clothes?"
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
