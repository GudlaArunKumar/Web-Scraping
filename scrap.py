'''
First page in Hacker news website is scrapped in this code uisng requests and Beautiful soup module
'''

import requests
from bs4 import BeautifulSoup
import pprint  # pretty is used print the data in pretty manner which is inbuilt module

" requests module allows to get the web page html and beuatiful soup used to perform scraping on those html code"

response = requests.get("https://news.ycombinator.com/news")
print(response)
#print(response.text)  # response is a string which is HTML code

"Parsing the response string as html to get clear html code"

soup = BeautifulSoup(response.text,'html.parser')
#print(soup)

#print(soup.body)  # Prints only body and contents of html
#print(soup.body.contents)

'''
using css selectors and select class which contains story links and class which contains votes 
for the story links.
links are stored in class storlink and votes are stored in class subtext in Hacker news website.
'''
links = soup.select('.storylink')
#print(links)
subtext = soup.select('.subtext')
#print(subtext)

def sorted_stories_list(hnList):
    """Sorting the list in decreasing order
       with respect to votes"""
    return sorted(hnList,key=lambda x:x['votes'],reverse=True)

def create_custom_hackernews(links,subtext):
    hn =[]
    for index,item in enumerate(links):
        title = links[index].getText()  #function in beaytiful soup
        href = links[index].get('href',None) # To get link of news if no link is there, default is None
        vote = subtext[index].select('.score') # points are stored inside class score of class subtext,if points not available, then class score wont be present
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 100:
                hn.append({'title': title, 'link': href,'votes':points})
            #print(points)
    return sorted_stories_list(hn)

pprint.pprint(create_custom_hackernews(links,subtext))
