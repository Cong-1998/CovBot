from covid_Faq.naive_bayes import translate

def pet(query):
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
                                            "text": "Can I use hand sanitizer on pets?"
                                        },
                                        {
                                            "text": "What should I do if my pet gets COVID-19?"
                                        },
                                        {
                                            "text": "Can I get COVID-19 from my pets?"
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
