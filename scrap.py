import requests
from bs4 import BeautifulSoup
import pprint  # pretty print the data which is inbuilt module

" requests module allows to get the web page html and beuatiful soup used to perform scraping on those html code"

response = requests.get("https://news.ycombinator.com/news")
print(response)
#print(response.text)  # response is a string which is HTML code

"Parsing the response string as html to get clear html code"

soup = BeautifulSoup(response.text,'html.parser')
#print(soup)

#print(soup.body)  # Prints only body and contents of html
#print(soup.body.contents)

#print(soup.find_all('a')) # Finding all url tags and returns as list
#print(soup.find(id="score_24029002"))

'''
using css selectors and select function.knowing about class by inspecting in the website
links are stored in class storlink and votes are stored in class subtext in Hacker news website.
'''
links = soup.select('.storylink')
print(links)
subtext = soup.select('.subtext')
print(subtext)

def sorted_stories_list(hnList):
    """Sorting the list in decreasing order
       with respect to votes"""
    return sorted(hnList,key=lambda x:x['votes'],reverse=True)

def create_custom_hackernews(links,subtext):
    hn =[]
    for index,item in enumerate(links):
        title = links[index].getText()  #function in beuatiful soup
        href = links[index].get('href',None) # To get link of news if no link is there, default is None
        vote = subtext[index].select('.score') # points are stored inside class score of class subtext,if points not available, then class score wont be present
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 100:
                hn.append({'title': title, 'link': href,'votes':points})
            #print(points)
    return sorted_stories_list(hn)

pprint.pprint(create_custom_hackernews(links,subtext))