#Scraping Module
from bs4 import BeautifulSoup
#Allows you to get the webpage without visting the site by sending a get request for defind URl
import requests
#allows us to change json dictionary to python dictionary for parsing
import json
#URLs for two sites that are scraped
twothreeURL = 'http://traintimelb-367443097.us-east-1.elb.amazonaws.com/getTime/2/232?callback=angular.callbacks._0'
fourfiveURL = 'http://traintimelb-367443097.us-east-1.elb.amazonaws.com/getTime/4/423?callback=angular.callbacks._0'
def FourFive(trainURL): #Function that scrapes the 4/5 train site
    r = requests.get(trainURL) # sets r so when you call it you send a GET request to specified URL
    soup = BeautifulSoup(r.text,'html.parser') # scrapes the returned page as html, and only includes text
    json1 = soup.text #json1 since need to call an actual json funtion later on
    json1 = json1.split('(') # removes junk before dictionary
    json1 = json1[1].split(')') #removes unk after dictionary
    json1 = json1[0] # after split, things are placed in a list, so by doing this json1 is now just the dictionary without junk code.
    jsonDict = json.loads(json1) # sets JSON dict as python dict so it can be parsed.

# Manhattan is uptown, Brooklyn is downtown. Both of these look into the dictionary and get the first two trains under the 'times' key.
# The direction1 key is for Manhattan and direction 2 is for brooklyn
# Inside the "times" value is the "last stop" "minutes away" and "route"
    manhattan = jsonDict["direction1"]["times"][0:2]
    brooklyn = jsonDict["direction2"]["times"][0:2]

# Prints direction1 value and the name, runs a loop that prints the upcoming trains with some text to help distinguish
    print(jsonDict ["direction1"]["name"],"4/5:")
    for i in range(0,2):
        NextTrainsManhattan = ("There is a", manhattan[i]["route"], "train to", manhattan[i]["lastStation"],":", manhattan[i]["minutes"], "minutes away")
        print(*NextTrainsManhattan)
    print('---------')

    #Brooklyn bound 4 5 # same a above loop but for Brooklyn bound trains
    print(jsonDict["direction2"]["name"],("4/5:"))
    for j in range(0,2):
        NextTrainsBrooklyn = ("There is a", brooklyn[j]["route"], "train to", brooklyn[j]["lastStation"],":", brooklyn[j]["minutes"], "minutes away")
        print(*NextTrainsBrooklyn)
def TwoThree(trainURL2):
    r = requests.get(trainURL2)
    soup = BeautifulSoup(r.text,'html.parser')
    json1 = soup.text
    json1 = json1.split('(')
    json1 = json1[1].split(')')
    json1 = json1[0]
    jsonDict = json.loads(json1)
    manhattan = jsonDict["direction1"]["times"][0:2]
    brooklyn = jsonDict["direction2"]["times"][0:2]
    #manhattan bound 2 3
    print(jsonDict ["direction1"]["name"], "2/3:")
    for x in range(0,2):
        NextTrainsManhattan = ("There is a", manhattan[x]["route"], "train to", manhattan[x]["lastStation"],":", manhattan[x]["minutes"], "minutes away")
        print(*NextTrainsManhattan)
    print('---------')
    #brooklyn bound 2 3
    print(jsonDict["direction2"]["name"],"2/3:")
    for y in range(0,2):
        NextTrainsBrooklyn = ("There is a", brooklyn[y]["route"], "train to", brooklyn[y]["lastStation"],":", brooklyn[y]["minutes"], "minutes away")
        print(*NextTrainsBrooklyn) # Everything in here is the same as above, just for 2/3 trains. Only thing that changed is the URL.
def info(url): #Information that displays at top of GUI (station and last time updated)
    r = requests.get(url)
    soup = BeautifulSoup(r.text,'html.parser')
    json1 = soup.text
    json1 = json1.split('(')
    json1 = json1[1].split(')')
    json1 = json1[0]
    jsonDict = json.loads(json1)
    updateTime = jsonDict["lastUpdatedTime"]
    station = jsonDict["stationName"]
    print(station)
    print('----------')
    print(updateTime)
    print('___________')
def mainText(): #Runs all other functions to get info. This is run when the document is run from mainApp.py
    #f = open('/times/')
    info(twothreeURL) # gets info
    print("Upcoming 2 and 3 Trains:\n_______________") # Presents it nicely
    TwoThree(twothreeURL)
    print("_______________\nUpcoming 4 and 5 Trains:\n_______________")
    FourFive(fourfiveURL)
    print("")
mainText() # runs everything
