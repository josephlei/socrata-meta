
# coding: utf-8

# In[ ]:

#import the required libraries
import csv
import requests
import simplejson as json


# In[ ]:

targeturl='https://gavaobert.gavaciutat.cat/' #change this to the SOCRATA portal you want to target, don't forget ending /
descriptor='GAVA'   #change this to a recognizable descriptor for yourself


# In[ ]:

r=requests.get(targeturl+"api/dcat.json") #build string according to SOCRATA's convention

'''
SOCRATA has a limit to how many requests can be made every hour from a public pool without an application token.
This can especially be a problem if your portal has over 100 datasets. Every time this program is run, you are
making (x+1) request "pings" against SOCRATA servers, where x is the number of datasets on the target portal

If you are running into this, you will need to register an account with SOCRATA and append the following code
behind your API calls:

?$$app_token=INSERT-YOUR-APP-TOKEN-HERE
'''

j=r.json() #parse the json into a dictionary named j, coincidentally j's KVPs are also dictionaries


# In[ ]:

#if it fetched the data successfully, continue; otherwise stop
#this could probably be implemented more pythonically.. but it works for now
if r.status_code==200:
    print "\nsuccessfully fetched json data, http return code 200"
else:
    sys.exit()


# In[ ]:

#this cell retrieves the list of keywords from all datasets and loads them into one list named masterlist

masterlist=[] #dim masterlist as a empty list

for i in j:
    if len(i['identifier'])==9:
        unified=i['keyword'].replace(';',',')
        strlist=unified.split(',')
        for x in strlist:
            masterlist.append(x.lstrip())


# In[ ]:

masterlist.sort() #sort masterlist
print "master keyword list built:", len(masterlist),"elements" #print how many elements are in masterlist


# In[ ]:

keywords=open(descriptor+' - KEYWORDS.csv', 'wb') #open the csv file for writing
print "master keyword list file opened, starting to write rows"


# In[ ]:

for i in masterlist:
    csv.writer(keywords).writerow([i.encode("utf-8")])
#this may need to be tweaked to optimize encoding to handle errors


# In[ ]:

keywords.close() #close csv writing, release all locks
print "master keyword list file closed, all rows written \n"


# In[ ]:

#the below dumps out identifiers, views, titles and descriptions, created, modified and publisher
#this can be modified to produce specific metadata elements YOU want, examine /api/dcat.json as needed

metadata=open(descriptor+' - METADATA.csv', 'wb')
csv.writer(metadata).writerow(['identifier','views','title','description','created','modified'])


# In[ ]:

counter=0
for i in j:
    if len(i['identifier']) == 9:
        counter=counter+1
        try:
            if counter%10==0: #modify the modulus to change the frequency of printouts
                print counter,"of",len(j)-1,"rows written,",(len(j)-1)-counter,"remaining"
            metastring=targeturl+"api/views/"+i['identifier']+".json"
            x=requests.request('get',metastring).json()
            csv.writer(metadata).writerow([i['identifier'].encode("utf-8"),x['viewCount'], i['title'].encode("utf-8"), i['description'].encode("utf-8"),i['created'],i['modified']]) #write one line to csv file, list of elements only!
        except:
            print "error, continuing"


# In[ ]:

metadata.close() #Close the output file, release all locks
print len(j)-1,"of",len(j)-1,"rows written, 0 remaining" #print final completion notice

