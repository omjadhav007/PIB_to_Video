import urllib.request
import lxml
from bs4 import BeautifulSoup
import pandas as pd
import sumarry as extr

def scrap_ids(present_in_db):
    theurl = "https://pib.gov.in/indexd.aspx"
    thepage = urllib.request.urlopen(theurl)

    soup = BeautifulSoup(thepage,'html.parser')
    u=soup.find('ul',class_='release_list')
    ids=[]
    c=0
    for url in u.find_all('a',href=True):
        c+=1
        if c==6:
            break
        temp_id=url['href'][-7:]
        if not present_in_db(temp_id):
            ids.append(temp_id)
    return ids

def scrap_data_and_summarize(ids):
    hl=[]
    rel=[]
    des=[]
    sum=[]
    url=[]
    url_part="https://pib.gov.in/PressReleasePage.aspx?PRID="

    for id in ids:
        url.append(url_part+id)

    for i in url:
        page = urllib.request.urlopen(i)
        s = BeautifulSoup(page,'html.parser')
        hl.append(s.find('h2').text.strip())
        rel.append(s.find('div',class_='ReleaseDateSubHeaddateTime').text.strip())
        z=s.find_all('p')
        d=""
        for j in z:
            d+=j.text.strip()
            if d=="":
                break
        des.append(d)
        sum.append(extr.abstractive_summarization(d))

    obj={'id':ids, 'headline':hl, 'release':rel, 'description':des, 'summary':sum}
    df=pd.DataFrame(obj)

    df.to_csv("newPIB_data.csv")
    return df

# def present_in_db(id):
#     return False

# ids=scrap_ids(present_in_db)
# # print(ids)
# data=web_scrap(ids)
# print(data)

