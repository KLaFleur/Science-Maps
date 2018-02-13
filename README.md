# Science-Maps




## Overview
This project takes as input a search for something that would be the 
subject of scientific research and a number of articles to scrape from, and returns a csv of locations found in the abstracts of the articles returned by the desired search (using [sciencedirect.com](sciencedirect.com) ). 
These locations are determined by checking the text of all abstracts found against a dictionary of ~7,000 cities and countries. The user 
imports the csv to google maps. An example map with a few different 
searches can be found [here](https://drive.google.com/open?id=1uSapi_Us20bfaV65zegpFPFT6kr9oFDk&usp=sharing).

##Potential applications







## Next Steps  

Integrate a named entity recognition tool, such as the [Stanford Natural Language Processing group's](https://nlp.stanford.edu/) [Named Entity Recognizer](https://nlp.stanford.edu/software/CRF-NER.html) coupled with the geocoding function of the [Google Maps API](https://developers.google.com/maps/) to detect and get coordinates for locations that aren't loaded into the dictionary. 

Add support for protected areas, mountain ranges, and forests around the world(only U.S. National parks are supported as of now)

Look into an issue where the scraper returns 404 errors on ~25% of links it runs 

Link location results to the title of the article that they came from 


​	







