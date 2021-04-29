import requests
from bs4 import BeautifulSoup
import pandas as pd
import urllib3
import csv
import matplotlib.pyplot as plt
import numpy as np
import os

class historicdata():
    def __init__(self):
        self.hr_list = []
        self.new_dict= {}
        
        
    def get_climate_details(self,value):
         reqs = requests.get("https://www.metoffice.gov.uk/research/climate/maps-and-data/historic-station-data")
         soup = BeautifulSoup(reqs.text, 'html.parser')
         
         for link in soup.find_all('a'):
             hr = link.get('href')
             print hr
             if ".txt" in hr:
                 print hr
                 if value.lower() in hr:
                     return hr    
         
    def get_graph_details(self,value):
        print os.getcwd()+"\\" +value+".csv"
        if os.path.exists(os.getcwd()+"\\" +value+".csv"):
           os.remove(os.getcwd()+"\\" +value+".csv")
        if not os.path.exists(os.getcwd()+"\\" +value+".csv"):
            pass
        file1 = self.get_climate_details(value)
        self.new_list = []
        self.new_dict= {}
        content=requests.get(file1)
        data = content.text.encode("utf-8")
        for i ,line in enumerate(data.split("\n")):
                   new = []
                   line1 = line.split(" ")                   
                   while('' in line1):
                      line1.remove('')
                      for k,j in enumerate (line1):
                          line1[k] = j.strip()
                          if "*" in j:
                             line1[k] = j.replace("*","").strip()
                   if "yyyy" in line1:
                       line1.remove("tmax")
                       line1.remove("tmin")
                       line1[2] = "avgTemp"
                       print line1
                       self.new_list.append(line1)
                   if line1[0].startswith("20"):
                      if "---" in line[2] or "---" in line1[3]:
                          pass
                      else:
                         temp = float(line1[2])+float(line1[3])
                         temp1 = temp/2
                      new.append(line1[0])
                      new.append(line1[1])
                      new.append(temp1)
                      new.append(line1[-1])
                      new.append(line1[-2])
                      self.new_list.append(new)
        self.new_dict[file1.split("/")[-1].strip(".txt").capitalize()]=self.new_list
        self.create_graph(self.new_list,value)

    def create_graph(self,new_list,value):            
        with open(os.getcwd()+"\\" +value+".csv", 'w') as file1:
           writer = csv.writer(file1, delimiter='|')
           writer.writerows(new_list)
        data = np.genfromtxt(value+'.csv', delimiter='|',names=('yyyy','mm','avgTemp','af','sun'))
        x = data["mm"]
        y = data['avgTemp']
        plt.xlabel("Month")
        plt.ylabel("Temperature")
        plt.xticks(np.arange(1, 13, 1))
        plt.plot(x,y)
        plt.show()

       

if __name__ == "__main__":
    hs = historicdata()
    value = raw_input("Enter the Place for creating Climate Graph from the below List:\n 1.Aberporth\n 2.Armaghata\n 3.Ballypatrickdata\n 4.Bradforddata\n 5.Braemardata\n 6.Cambornedata\n 7.Cambridgedata\n 8.Cardiffdata\n 9.Chivenordata\n 10.Cwmystwythdata\n 11.Dunstaffnagedata\n 12.Durhamdata\n 13.Eastbournedata\n 14.Eskdalemuirdata\n 15.Heathrowdata\n 16.Hurndata\n 17.Lerwickdata\n 18.Leucharsdata\n 19.Lowestoftdata\n 20.Manstondata\n 21.Nairndata\n 22.Newtonriggdata\n 23.Oxforddata\n 24.Paisleydata\n 25.Ringwaydata\n 26.Rossonwyedata\n 27.Shawburydata\n 28.Sheffielddata\n 29.Southamptondata\n 30.Stornowaydata\n 31.Suttonboningtondata\n 32.Tireedata\n 33.Valleydata\n 34.Waddingtondata\n 35.Whitbydata\n 36.Wickairportdata\n 37.Yeoviltondata\n")
    hs.get_graph_details(value)
