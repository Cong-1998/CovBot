from GoogleNews import GoogleNews
from newspaper import Article
import pandas as pd

googlenews = GoogleNews()

query = "covid 19 vaccine malaysia"

googlenews.search(query)

result = googlenews.result()

df = pd.DataFrame(result)

def extrac_title():
    
    titl = []
    titl = df['title']      
    return titl

def extrac_link():
    
    lin = []
    lin = df['link']      
    return lin

#print(extrac_title())
#print(extrac_link())
