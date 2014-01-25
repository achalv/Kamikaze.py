
import urllib2
import json

def Kamikaze(cocktailArray):
	searchSlug = slugify(cocktailArray)
	drinks = fetchCocktails(searchSlug)
	return drinks	

def slugify(cocktailArray):
	urlPrefix = 'http://kamikaze.herokuapp.com/cocktails.json?ingredients='
	cocktailSearchTerm = '+'.join(cocktailArray)
	cocktailURL = urlPrefix+cocktailSearchTerm
	print cocktailURL
	return cocktailURL 

def fetchCocktails(cocktailURL):	
	cocktailData = urllib2.urlopen(cocktailURL)
	cocktailJSON = json.load(cocktailData)
	return cocktailJSON

if __name__ == '__main__':

#Coming Soon!