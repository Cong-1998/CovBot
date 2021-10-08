from GoogleNews import GoogleNews
from newspaper import Article
import pandas as pd

googlenews = GoogleNews()

query = "covid 19 movement control malaysia"

googlenews.search(query)

result = googlenews.result()

df = pd.DataFrame(result)

def extract_title():
    
    titl = []
    titl = df['title'] 
    return titl

def extract_link():
    
    lin = []
    lin = df['link']
    return lin

#print(extract_title())
#print(extract_link())
