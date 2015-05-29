# Socrata Meta Data Extractor, by Joseph Lei
### Purposed for use at 2015 National Day of Civic Hacking (NDoCH) events

####This python script targets ONE of the over 100 SOCRATA Open Data Portal websites (specified by you the user) and retrieves the meta data for the entire portal.  

Specifically, each dataset on a SOCRATA site has keywords and tags phrases associated with it describing at a high level what the dataset is about.  This code will retrieve a list of *every* keyword/tag for *every* data set on a SOCRATA portal and create a csv file containing the results.

Additionally, this code then pulls SOME of the metadata available through SOCRATA's SODA API and populates it into a csv file.  Currently the elements I have chosen to pull are listed below, though with some minor modifications almost any meta data element could be retrieved:
* Unique 8 digit identifier
* View count
* Title
* Description
* Created Date
* Modified Date
* Publisher (this may be specific to CA CHHS, if it is causing errors, remove it from the code)

###Requirements
* Python 2.x

1. Open SOCRATA_GET_KEYWORDS_ONE_SITE.py with your favorite text editor (or .ipynb if you want to play with the code blocks)
2. Change the values of the two variables targeturl and descriptor
3. Save and close the code
4. Run the file with "$ python SOCRATA_GET_KEYWORDS_ONE_SITE.py"
