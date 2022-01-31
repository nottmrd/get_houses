#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 16:41:28 2021
"""

import time

#requests is for scraping HTML
import requests

#pandas is for data anlysis
import pandas as pd

#headers: Makes the website think I'm NOT a bot
headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',}

#creating a list of links to download, putting the respective numbers into the url
locs = {"30818": "Austin", "48030": "South Austin", "351579": "East Austin", "177559": "West Austin", "164521": "North Austin", "35781": "Corpus Christi"}
    
def run():
    urls = []
    for loc in locs.keys():
        urls.append("https://www.redfin.com/stingray/api/gis-csv?al=1&market=rio-grande-valley&min_stories=1&num_homes=3500&ord=redfin-recommended-asc&page_number=1&region_id=%s&region_type=6&sf=1,2,3,5,6,7&status=9&uipt=1,2,3,4,5,6&v=8" % loc)
    
    #Creating the request to pull the download from the website. Headers is not necessarily needed, but it is for avoiding being thought a robot
    myfiles = []
    for url in urls:
        myfiles.append(requests.get(url, headers=headers))
    
    #Telling it where to write, to the Downloads folder with the file name being unique town name
    saves = []
    for loc in locs.values():
        saves.append('E:\Documents\Python\house_scrape\%s.csv' % loc)
    
    #Zipping the unique save file name and unique URL corresponding to said location, together.
    #Bringing them together into the open function, write the file pulled to the save location.
    #Running with a sleep timer
    for save, myfile in zip(saves, myfiles):
        open(save, 'wb').write(myfile.content)
        time.sleep(11)

def add_city(city, code):
    """
    Parameters
    ----------
    city : string
    code : int

    Returns
    -------
    None.

    """
    locs["%s" % code] = city
    

run()

houses = pd.read_csv('E:\Documents\Python\house_scrape\corpus.csv')

##ROI = 6% cost of selling house / avg net rental income
##or
##ROI = downpayment / avg net rental income
    
