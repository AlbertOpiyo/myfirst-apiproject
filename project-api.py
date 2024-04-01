import requests
import pandas as pd

baseurl='https://rickandmortyapi.com/api/'

endpoint= 'character'


def main_request(baseurl,endpoint, x):
    r=requests.get(baseurl + endpoint + f'?page={x}')
    return r.json()


def get_pages(response):
    return response['info']['pages']

def parse_json(response):
    char_list=[]
    for item in response['results']:
        char={
            'name': item['name'], 
            'no_episodes': len(item['episode'])
        }
        char_list.append(char)
    return char_list


data= main_request(baseurl=baseurl,endpoint=endpoint,x=1)

mainlist=[]
for x in range(1,get_pages(data)+1):
    print(x)
    mainlist.extend(parse_json(main_request(baseurl,endpoint,x)))

df = pd.DataFrame(mainlist)

# print(df.head())

df.to_csv("char_list.csv",index=False)


