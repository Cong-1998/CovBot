from covid_Faq.naive_bayes import translate

def symptom(query):
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
                                            "text": "Are there long-term effects of COVID-19?"
                                        },
                                        {
                                            "text": "How long does it take to develop symptoms?"
                                        },
                                        {
                                            "text": "Is it possible to have the flu and COVID-19 at the same time?"
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
