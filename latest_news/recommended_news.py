from GoogleNews import GoogleNews
from newspaper import Article
import pandas as pd

googlenews = GoogleNews()

query = "covid 19 latest news malaysia"

googlenews.search(query)

result = googlenews.result()

df = pd.DataFrame(result)

def extra_title():
    
    titl = []
    titl = df['title'] 
    return titl

def extra_link():
    
    lin = []
    lin = df['link']
    return lin

#print(extra_title())
#print(extra_link())


