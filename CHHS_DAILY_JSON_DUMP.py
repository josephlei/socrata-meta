
# coding: utf-8

# In[1]:

import csv, requests, datetime
import simplejson as json


# In[2]:

targeturl='http://chhs.data.ca.gov/' #change this to the SOCRATA portal you want to target, don't forget ending /
descriptor='CHHS OPEN DATA PORTAL'   #change this to a recognizable descriptor for yourself


# In[3]:

r=requests.get(targeturl+"api/dcat.json") #build string according to SOCRATA's convention, this is in json format
j=r.json() #parse the json into a dictionary named j, coincidentally j's KVPs are also dictionaries


# In[4]:

print r.url
today=datetime.date.today()
print str(today)


# In[5]:

with open("chhs-json-repo/chhs-dcat-"+str(today)+".json", 'w') as outfile:
    outfile.write(r.text.encode("utf-8"))

