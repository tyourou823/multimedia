# -*- coding: utf-8 -*-
import os, sys
import urllib
from xml.etree.ElementTree import *
import webbrowser
from PIL import Image

def rgb2hsv(r,g,b):
	r,g,b = map(float, (r,g,b))
	if r == g and g == b:
		ma = r
		mi = r
		h = 0
		v = r
	elif r > g and r > b:
		ma = r
		mi = min(g,b)
		h = 60 * (g-b) / (ma-mi)+0
	elif g > b and g >= r:
		ma = g
		mi = min(b,r)
		h = 60 * (b - r) / (ma - mi) + 120
	elif b >= r and b >= g:
		ma = b
		mi = min(r,g)
		h = 60 * (r-g)/(ma-mi)+240
	else:
		print "Error"
	if ma == 0:
	 	return 0,0,0
	s = (ma -mi) / ma
	v = ma
	return h,s,v

args = { 
            'has_geo' : 1,  # ジオタグがついているか
            'extras'  : "date_upload",
            'per_page': '1',
            'sort'    : 'date-posted-desc',
            'api_key' : '0bacbd797f523d2850bf3b9dd9377c39',           
            'method'  : 'flickr.photos.search'
}

url = "https://api.flickr.com/services/rest/?%s"%(urllib.urlencode(args) )
results = urllib.urlopen(url)
xml = fromstring(results.read())

for photo in xml.getiterator('photo'):
	pic_url = 'http://farm' + photo.get('farm') + '.static.flickr.com/' + photo.get('server') + '/' + photo.get('id') + '_' + photo.get('secret') + '_m.jpg'
#	print pic
	savepath = '../pic/'+photo.get('id')+'.jpg'
	urllib.urlretrieve(pic_url, savepath)
	pic = Image.open('../pic/'+photo.get('id')+'.jpg')
	pic.show()
	geo_url = 'https://www.flickr.com/services/rest/?method=flickr.photos.geo.getLocation&format=rest&api_key=' + args["api_key"] + '&photo_id=' + photo.get('id')
	geo_results = urllib.urlopen(geo_url)
	geo_xml = fromstring(geo_results.read())
	for geocode in geo_xml.getiterator('location'):
		webbrowser.open('https://www.google.com/maps/@' + geocode.get('latitude') + ',' + geocode.get('longitude') + ',13z')
#		print geocode.get('latitude') + ' , ' + geocode.get('longitude')


