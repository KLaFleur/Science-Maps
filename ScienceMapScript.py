import bs4 as bs 
import urllib.request
import googlemaps
import csv

#loads a list of countries into a python dictonary 'dict'
def addCountries ():
	with open ("CountriesCoord.rtf", "r") as file:
		#readCSV = csv.reader(file, delimiter=',')

		for line in file:
			line = line.replace('\n' , '')
			tokens = [0] * 3
			i = 0
			for word in line.split(","):
				tokens[i] = word
				i = i + 1
			dict[tokens[2]] = str(tokens[0]) + "," + str(tokens[1])
	file.close()

#loads ~7000 cities into the dictionary 'dict'
def addCities(): 
	with open ("citiesCoor.rtf", "r") as cities:
		for line in cities:
			
			tokens = [0] * 15
			i = 0
			for word in line.split(","):
				tokens[i] = word
				i = i + 1
			pass
			
			dict[tokens[0]] = ( str(tokens[2]) + ","  + str(tokens[3])  )

		pass
	

	
	cities.close()



#given a search, returns the link to the search results page
#Show is set to 100 per page for simplicity 
def getSrc (mySearch, numResults , pageNum):
	#sourceLink is built in accordance with the conventions that science direct builds the first (technically 0th) page of results 
	if pageNum is 0:
		sourceLink = 'http://www.sciencedirect.com/search?qs=' + mySearch +  '&show=' + str(100) + '&sortBy=relevance&articleTypes=FLA&lastSelectedFacet=articleTypes'
		print(sourceLink)
		source = urllib.request.urlopen(sourceLink)
		return source
	#if we're not loading the first page of results, the 'offset' attribute defines how many results into the search the current page starts.
	#see the while loop in searchScrape()
	else :
		sourceLink = 'http://www.sciencedirect.com/search?qs=' + mySearch + '&authors=&pub=&volume=&issue=&page=&origin=home&zone=qSearch&show='+ str(100) + '&offset=' + str(100 * pageNum)
		print(sourceLink)
		source = urllib.request.urlopen(sourceLink)
		return source


def scrape (soup):
	i = 0
	
	f = open("abstracts.txt", "a")
	links = ' '
	for url in soup.find_all('a'):
		thisLink =  url.get('href')

		if "/science/article" not in thisLink:
			pass

		elif thisLink not in links and '.pdf' not in thisLink:
			
			print(thisLink)
			links = links + ' ' + thisLink
			
			try:
				source2 = urllib.request.urlopen("http://www.sciencedirect.com" + thisLink ).read()
				pass
			except Exception as e:
				
				#print(e)
				continue
			finally:
				pass
			
			
			soup2 = bs.BeautifulSoup(source2, 'lxml')
			
			title = soup2.title.string

			i = i + 1
			for paragraph in soup2.find_all('p'):
				
				abstract = paragraph.text


				try:
					
					f.write(title)
					#f.write("\n")
					f.write(abstract)
					#f.write("\n")
					pass
				except Exception as e:
					#print(e)
					continue
				

				#print(paragraph.text)

			pass




			#results[i] = url.get('href')
			
					#print(url.get('href'))

		# url.get('href').contains("/science/article") :
	pass
	f.close()
	return i


def findMatches (abstracts):
	matches = ' ' 
	j= 0
	for line in abstracts:

	        for word in line.split():
	    

	        	try:
	        		j = j + 1
	        		#if dict[word] is not null : #and dict[word] not in matches
	        		if dict[word] not in matches:
	        			
		        		print(dict[word])
		        		#dict[word].key()
		        		wordAtHand = word + ',' + dict[word]
		        		matches = matches + wordAtHand + ','
		        		matchKeys = matchKeys + word

	           		
	        		pass
	        	except Exception as e:
	        		continue
	print(j)
	return matches
	abstracts.close()


def writeCsv (matchesToken):
	with open ('results.csv' , 'a') as file:
	    fieldnames = ['place', 'lat', 'long']
	    writer = csv.DictWriter(file , fieldnames=fieldnames)
	    writer.writeheader()
	    i = 0
	    while i < len(matchesToken) - 3  :
	    	writer.writerow( {'place' : matchesToken[i] , 'lat' : matchesToken[i+1] , 'long' : matchesToken[i+2]})
	    	i = i + 3
	    	pass



#Given a search and a desired number of results to scrape from, scrapes the text of each abstract found 
def searchScrape (search, numResults): #numResults just supports multiples of 100 for now (numresults)
	counter = 0
	k = 0
	#Loops for (numResults/100) pages. For example searchScrape("mountains", 1200) runs 12 pages, each within 100 results. (see getSrc)
	while k < numResults/100:
		source = getSrc(search, str(numResults) , k)
		soup = bs.BeautifulSoup(source, 'lxml')
		counter = counter + scrape(soup)
		
		k = k + 1
	#prints the number of abstracts scraped from
	print("Counter" + str(counter))


	
#Creates a dictionary where the keys are location names (String) and the values are a String formmated as 'lat,long'
dict = {"United states" : '37.09024,-95.712891'}
addCountries()
print(dict)
addCities()


searchScrape('earthquakes', 600)	

#Write as function?
f = open("abstracts.txt", "r" )
matchesToken  = findMatches(f).split(",")
print(matchesToken)    	
writeCsv(matchesToken)
f.close()









