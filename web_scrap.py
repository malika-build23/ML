import pandas as pd
import requests
from bs4 import BeautifulSoup
import numpy as np


final = pd.DataFrame()
for j in range(1,7):
    
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36'}
    webpage = requests.get('https://www.ambitionbox.com/list-of-companies?campaign=homepage_explore_companies_widget&page={}'.format(j),headers=headers).text
    soup = BeautifulSoup(webpage,'lxml')
    company = soup.find_all('div',class_= 'companyCardWrapper')
    name =[]
    rating= []
    Reviews = []
    Salaries = []
    Interviews=[]
    Jobs =[]
    Benefits=[]
    Highly_Rated_for = []
    Critically_Rated_for = []
    for i in company:
        h = i.find('h2')
        name.append(h.get_text(strip=True) if h else np.nan)

        r = i.find('div', class_='rating_text rating_text--md')
        rating.append(r.get_text(strip=True) if r else np.nan)

        counts = [s.get_text(strip=True) for s in i.find_all('span', class_='companyCardWrapper__ActionCount')]
        Reviews.append(counts[0] if len(counts) > 0 else np.nan)
        Salaries.append(counts[1] if len(counts) > 1 else np.nan)
        Interviews.append(counts[2] if len(counts) > 2 else np.nan)
        Jobs.append(counts[3] if len(counts) > 3 else np.nan)
        Benefits.append(counts[4] if len(counts) > 4 else np.nan)

        rv = [s.get_text(strip=True) for s in i.find_all('span', class_='companyCardWrapper__ratingValues')]
        Highly_Rated_for.append(rv[0] if len(rv) > 0 else np.nan)
        Critically_Rated_for.append(rv[1] if len(rv) > 1 else np.nan)


    d = {'Name':name ,'Rating':rating,'Reviews' :Reviews ,'Salaries':Salaries,'Interviews':Interviews,'Jobs':Jobs,'Benefits':Benefits,'Highly_Rated_for':Highly_Rated_for ,'Critically_Rated_for':Critically_Rated_for}

    df = pd.DataFrame(d)
    
    final = pd.concat([final, df], ignore_index=True)


final




