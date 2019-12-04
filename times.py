from bs4 import BeautifulSoup
import requests
import re
import json
twothreeURL = 'http://traintimelb-367443097.us-east-1.elb.amazonaws.com/getTime/2/232?callback=angular.callbacks._0'
fourfiveURL = 'http://traintimelb-367443097.us-east-1.elb.amazonaws.com/getTime/4/423?callback=angular.callbacks._0'
def twothreeJson(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text,'html.parser')
    #json1 since need to call an actual json funtion later on
    json1 = soup.text
    json1 = json1.split('(')
    json1 = json1[1].split(')')
    json1 = json1[0]
    jsonDict = json.loads(json1)
    #uptown and downtown train number + last stop + min away
    manhattan = jsonDict["direction1"]["times"][0:2]
    brooklyn = jsonDict["direction2"]["times"][0:2]
def fourfiveJson(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text,'html.parser')
    #json1 since need to call an actual json funtion later on
    json1 = soup.text
    json1 = json1.split('(')
    json1 = json1[1].split(')')
    json1 = json1[0]
    jsonDict = json.loads(json1)
    #uptown and downtown train number + last stop + min away
    manhattan = jsonDict["direction1"]["times"][0:2]
    brooklyn = jsonDict["direction2"]["times"][0:2]
def FourFive():
    fourfiveJson(fourfiveURL)
    #manhattan bound 4 5
    print(jsonDict ["direction1"]["name"])
    for i in range(0,2):
        NextTrainsManhattan = ("There is a", manhattan[i]["route"], "train to", manhattan[i]["lastStation"],":", manhattan[i]["minutes"], "minutes away")
        print(*NextTrainsManhattan)
    print('---------')
    #Brooklyn bound 4 5
    print(jsonDict["direction2"]["name"])
    for j in range(0,2):
        NextTrainsBrooklyn = ("There is a", brooklyn[j]["route"], "train to", brooklyn[j]["lastStation"],":", brooklyn[j]["minutes"], "minutes away")
        print(*NextTrainsBrooklyn)
def TwoThree():
    #manhattan bound 2 3
    twothreeJson(twothreeURL)
    print(jsonDict ["direction1"]["name"])
    for i in range(0,2):
        NextTrainsManhattan = ("There is a", manhattan[i]["route"], "train to", manhattan[i]["lastStation"],":", manhattan[i]["minutes"], "minutes away")
        print(*NextTrainsManhattan)
    print('---------')
    #brooklyn bound 2 3
    print(jsonDict["direction2"]["name"])
    for j in range(0,2):
        NextTrainsBrooklyn = ("There is a", brooklyn[j]["route"], "train to", brooklyn[j]["lastStation"],":", brooklyn[j]["minutes"], "minutes away")
        print(*NextTrainsBrooklyn)
def main(): #updates times
    #f = open('/times/')
    print("Upcoming 2 and 3 Trains:\n_______________")
    TwoThree()
    print("_______________\nUpcoming 4 and 5 Trains:\n_______________")
    FourFive()
    print("")
    #FourFive()
main() # set time limit
