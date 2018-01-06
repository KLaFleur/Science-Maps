#from urllib.request import urlopen as uReq
#from bs4 import BeautifulSoup as soup 

import bs4 as bs 
import urllib.request
import googlemaps
import csv

mySearch = "volcanoes"



dict = {"United states" : 0}

gmaps = googlemaps.Client(key='AIzaSyD514l8769WgSlvobVZsOtBVbok5MfGWOE')



def addCountries1 ():
	with open ("CountriesCoord.rtf", "r") as file:
		#readCSV = csv.reader(file, delimiter=',')

		for line in file:
			line = line.replace('\n' , '')
			tokens = [0 ] * 3
			i = 0
			for word in line.split(","):
				tokens[i] = word
				i = i + 1
			dict[tokens[2]] = str(tokens[0]) + "," + str(tokens[1])
	file.close()


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


#addCountries1()
print(dict)
addCities()



#dict["in"] = null
#countrySrc = urllib.request.urlopen('https://www.searchify.ca/wp-content/uploads/2016/09/country-keyword-list.csv').read():

	#soup0 = bs.BeautifulSoup(countrySrc, 'lxml')
	#for paragraph in soup0.find_all('p'):
		#print (paragraph.text)
		#for word in paragraph.text
		#	dict [word] = word

#link to the search results. Generalized to allow for change in query, (but not author/vol/issue/page)
#source = urllib.request.urlopen('http://www.sciencedirect.com/search?qs=' + (mySearch) + '&authors=&pub=&volume=&issue=&page=&origin=home&zone=qSearch&show='+ numResults).read()

try:
	print(dict['a'])

	pass
except Exception as e:
	#print (e)
	print(dict.values())


#given a search, returns the link to the search results page
def getSrc (mySearch, numResults , pageNum):
	if pageNum is 0:
		source = urllib.request.urlopen('http://www.sciencedirect.com/search?qs=' + mySearch +  '&show=' + numResults + '&sortBy=relevance&articleTypes=FLA&lastSelectedFacet=articleTypes')
		return source
	else :
		source = urllib.request.urlopen('http://www.sciencedirect.com/search?qs=' + mySearch + '&authors=&pub=&volume=&issue=&page=&origin=home&zone=qSearch&show='+ numResults + '&offset=' + str(pageNum * numResults))
		return source



def scrape ():
	print("START")
	f = open("abstracts.txt", "a")
	i = 0
	for url in soup.find_all('a'):

		if "/science/article" not in url.get('href'):
			pass
		else:
			thisLink =  url.get('href')
			print(thisLink)
			
			try:
				source2 = urllib.request.urlopen("http://www.sciencedirect.com" + thisLink ).read()
				pass
			except Exception as e:
				
				print(e)
				continue
			finally:
				pass
			
			i = i + 1
			soup2 = bs.BeautifulSoup(source2, 'lxml')
			
			title = soup2.title.string
			for paragraph in soup2.find_all('p'):
				
				abstract = paragraph.text

				try:

					f.write("TITLE " + title +" title ")
					f.write(abstract)
					pass
				except Exception as e:
					print(e)
					continue
				

				#print(paragraph.text)

			pass




			#results[i] = url.get('href')
			
					#print(url.get('href'))

		# url.get('href').contains("/science/article") :
	pass
	f.close()



source = getSrc(mySearch, str(100) , 0)
soup = bs.BeautifulSoup(source, 'lxml')
scrape()

source = getSrc(mySearch, str(100), 1)
soup = bs.BeautifulSoup(source, 'lxml')
scrape()

source = getSrc(mySearch, str(100), 2)
soup = bs.BeautifulSoup(source, 'lxml')
scrape()



def findMatches (abstracts):
	matches = ' ' 
	

	for line in abstracts:
	        for word in line.split():
	        	try:

	        		#if dict[word] is not null : #and dict[word] not in matches
	        		if dict[word] not in matches:
	        			print(word)
		        		print(dict[word])
		        		#dict[word].key()
		        		wordAtHand = word + ',' + dict[word]
		        		matches = matches + wordAtHand + ", "
		        		matchKeys = matchKeys + word

	           		
	        		pass
	        	except Exception as e:
	        		continue
	return matches


f = open("abstracts.txt", "r" )

matchesToken  = findMatches(f).split(",")        		


print(matchesToken)

def writeCsv ():
	with open ('results.csv' , 'w') as file:
	    fieldnames = ['place', 'lat', 'long']
	    writer = csv.DictWriter(file , fieldnames=fieldnames)
	    writer.writeheader()
	    i = 0
	    while i < len(matchesToken) - 3  :
	    	writer.writerow( {'place' : matchesToken[i] , 'lat' : matchesToken[i+1] , 'long' : matchesToken[i+2]})
	    	i = i + 3
	    	pass
	   
	    	
			
			
			

    	

		
		
writeCsv()


print("matches" + findMatches(f))
amtAbtstracts= str(i)

print('scraped from ' + amtAbtstracts + 'articles')

f.close()





# 



# f = open("abstracts.txt", "r+")


# i = 0
# for url in soup.find_all('a'):

# 	if "/science/article" not in url.get('href'):
# 		pass
# 	else:
# 		thisLink =  url.get('href')
# 		print(thisLink)
		
# 		try:
# 			source2 = urllib.request.urlopen("http://www.sciencedirect.com" + thisLink ).read()
# 			pass
# 		except Exception as e:
# 			i = i + 1
# 			print(e)
# 			continue
# 		finally:
# 			pass
		
		
# 		soup2 = bs.BeautifulSoup(source2, 'lxml')
		
# 		title = soup2.title.string
# 		for paragraph in soup2.find_all('p'):
			
# 			abstract = paragraph.text

# 			try:

# 				f.write("TITLE " + title +" title ")
# 				f.write(abstract)
# 				pass
# 			except Exception as e:
# 				print(e)
# 				continue
			

# 			#print(paragraph.text)

# 		pass




# 		#results[i] = url.get('href')
		
# 				#print(url.get('href'))

# 	# url.get('href').contains("/science/article") :
# pass
# f.close()







