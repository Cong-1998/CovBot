from covid_Faq.naive_bayes import translate

def child(query):
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
                                            "text": "Should children wear masks?"
                                        },
                                        {
                                            "text": "How are babies affected by COVID-19?"
                                        },
                                        {
                                            "text": "What is MIS-C?"
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
