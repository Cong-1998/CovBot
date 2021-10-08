import pandas as pd
from statistic.case_malaysia import data_malaysia

def country(cust_country):

    print(cust_country)
    
    if (cust_country == "Malaysia"):

        df = pd.read_csv("malaysia.csv")

        webhookrespon = "Date: " + df.iloc[0,0] + "\n" + \
                        "Location: " + df.iloc[0, 1] + "\n" + \
                        "New active cases: " + str(df.iloc[0, 2]) + "\n" + \
                        "Total active cases: " + str(df.iloc[0, 4]) + "\n" + \
                        "New death cases: " + str(df.iloc[0, 3]) + "\n" + \
                        "Total death cases: " + str(df.iloc[0, 5]) + "\n" + \
                        "New recover cases: " + str(df.iloc[0, 6]) + "\n" + \
                        "Total recover cases: "+str(df.iloc[0, 7])

        return webhookrespon

def state(name):
    
    print(name)
    
    if (name == "Perlis"):
        return get_response(0)

    elif (name == "Kedah"):
        return get_response(1)

    elif (name == "Penang"):
        return get_response(2)

    elif name == "Perak":
        return get_response(3)

    elif name == "Selangor":
        return get_response(4)

    elif name == "Negeri Sembilan":
        return get_response(5)

    elif name == "Malacca":
        return get_response(6)

    elif name == "Johor":
        return get_response(7)

    elif name == "Pahang":
        return get_response(8)

    elif name == "Terengganu":
        return get_response(9)

    elif name == "Kelantan":
        return get_response(10)

    elif name == "Sabah":
        return get_response(11)

    elif name == "Sarawak":
        return get_response(12)

    elif name == "Federal Territory of Kuala Lumpur":
        return get_response(13)

    elif name == "Putrajaya":
        return get_response(14)

    elif name == "Labuan Federal Territory":
        return get_response(15)

    else:
        return "Please enter valid state in Malaysia"

def get_response(index):

    dff = pd.read_csv("state.csv")
    dff['new_cases'] = dff['new_cases'].astype('int')
    dff['total_cases'] = dff['total_cases'].astype('int')

    webhookrespons = "Date: " + dff.iloc[index, 0] + "\n" + \
                     "Location: " + dff.iloc[index, 1] + "\n" + \
                     "New active cases: " + str(dff.iloc[index, 2]) + "\n" + \
                     "Total active cases: " + str(dff.iloc[index, 3]) + "\n" + \
                     "New death cases: " + str(dff.iloc[index, 4]) + "  \n" + \
                     "Total death cases: "+str(dff.iloc[index, 5])

    return webhookrespons

#print(country("Malaysia"))
#print(state("Putrajaya"))
