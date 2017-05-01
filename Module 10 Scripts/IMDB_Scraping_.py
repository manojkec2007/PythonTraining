__author__ = 'Vineet'

import urllib2
from BeautifulSoup import BeautifulSoup

url = 'http://www.imdb.com/search/title?sort=num_votes,desc&start=1&title_type=feature&year=2005,2014'

test_url = urllib2.urlopen(url)
readHtml = test_url.read()
test_url.close()

soup = BeautifulSoup(readHtml)
# Using it track the number of Movie
count = 0
# Fetching the value present within tag results
movies = soup.findChildren('table', 'results')
# Changing the movie into an iterator
itermovie = iter(movies[0].findChildren('tr'))
# Skipping the first value of the iterator as it does have the required info
next(itermovie)

# Finding tr in itermovie. Every tr tag contains information of a movie
for tr in itermovie:

    # Fetching image Url for the movie
    imgSource = tr.findChildren('td', 'image')[0].find('img')['src'].split('._V1.')[0] + '._V1_SX214_AL_.jpg'
    # Fetching the title and year of the movie
    movie = tr.findChildren('td', 'title')
    title = movie[0].find('a').contents[0] + movie[0].find('span', 'year_type').contents[0]
    # Fetching Genres
    genres = movie[0].find('span', 'genre').findAll('a')
    genres = [g.contents[0] for g in genres]
    # Fetching Movie RunTime
    runtime = movie[0].find('span', 'runtime').contents[0]
    # Fetching Movie Rating
    rating = movie[0].find('span', 'value').contents[0]

    print '*******************************IMDB MOVIE***********************************'
    # Printing the S.No of the movie
    print 'S.No. --> ',
    count += 1
    print count
    # Printing the Title of the movie
    print 'Title --> ' + title
    # Printing the Genres of the movie
    print 'Genres --> ',
    for item in genres:
        if genres.index(item) == len(genres)-1:
            print(item.decode('UTF-8', 'strict'))
        else:
            print(item.decode('UTF-8', 'strict')+','),
    # Printing the Runtime of the movie
    print 'Runtime --> ' + runtime
    # Printing the Rating of the movie
    print 'Rating --> ' + rating
    # Printing the Image Source of the movie
    print 'Image Source --> ', imgSource





