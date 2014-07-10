# -*- coding: utf-8 -*-
from PIL import Image
import psycopg2
import numpy as np
import math

def ttoi(x):
	# tuple to integer
	x = str(x)
	x = x.replace('(','')
	x = x.replace(')','')
	x = x.replace(',','')
	x=int(x)
	return x

def compare(sample1,sample2):
	list1 = [0,0,0,0,0,0,0,0,0,0]
	list2 = [0,0,0,0,0,0,0,0,0,0]
	x=0
	while x<=9:
		cur.execute("select %s from landscape where landscape.name=%s;",(pic_color_list[x],sample1)
		element1=cur.fetchone()
		element1=ttoi(element)
		list1[x]=element
		x = x+1
	x=0
	while x<=9:
		cur.execute("select %s from landscape where landscape.name=%s;",(pic_color_list[x],sample2)
		element1=cur.fetchone()
		element1=ttoi(element)
		list1[x]=element
		x = x+1


def get_rgb(color):
	cur.execute("select r from colors where colors.name=%s;",[color])
	r=cur.fetchone()
	r = ttoi(r)
	cur.execute("select g from colors where colors.name=%s;",[color])
	g=cur.fetchone()
	g = ttoi(g)
	cur.execute("select b from colors where colors.name=%s;",[color])
	b=cur.fetchone()
	b = ttoi(b)
	r=float(r)
	g=float(g)
	b=float(b)
	array = np.array([r,g,b])
#	array_len = math.sqrt(np.dot(array,array))
	arraybase = array
#	array = array/array_len
#	return array, arraybase
	return arraybase

def pic_rgb(s):
	s = s.replace('(','')
	s = s.replace(')','')
	data = s.split(",")
	pic_r = int(data[0])
	pic_g = int(data[1])
	pic_b = int(data[2])
	pic_r = float(pic_r)
	pic_g = float(pic_g)
	pic_b = float(pic_b)
	array = np.array([pic_r,pic_g,pic_b])
	arraypic = array
#	array_len = math.sqrt(np.dot(array,array))
#	array = array/array_len
#	return array, arraypic
	return arraypic

#start program here -------------------------------------------------------------------

#f = open('test.txt','w')
#test.txt will update everytimes when analyze the picture.
image = Image.open('./samples/j')
#image=image.convert('RGBA')
#image = Image.open('a').convert('CMYK')
px = image.getdata()
print image.mode

conn = psycopg2.connect("dbname=multimedia host=localhost user=sae password=1233701sm")
cur = conn.cursor()
color_list = [u'red',u'yellow',u'yellow green',u'green',u'blue',u'purple',u'brown',u'pink',u'white',u'black']
pic_color_list= [u'red',u'yellow',u'yg',u'green',u'blue',u'purple',u'brown',u'pink',u'white',u'bk']
diff_list = [0,0,0,0,0,0,0,0,0,0]
color_pat = [0,0,0,0,0,0,0,0,0,0]
#print base
#base = np.array([r,g,b])

for s in px:
	s = str(s)
#	print s
	x = 0
#	pic, arraypic = pic_rgb(s)
	arraypic = pic_rgb(s)
	#the array of picture color
#	print arraypic
	while x<=9:
		color = color_list[x]
#		base, arraybase = get_rgb(color)
		arraybase = get_rgb(color)
		#the array of base color
#		print arraybase
#calculate how close the color
		diff = math.sqrt((arraypic[0]-arraybase[0])**2+(arraypic[1]-arraybase[1])**2+(arraypic[2]-arraybase[2])**2)
#		print diff
		diff_list[x]=diff
# calculate how close the vector
#		up = pic[0]*base[0]+pic[1]*base[1]+pic[2]*base[2]
#		down = math.sqrt(base[0]*base[0]+base[1]*base[1]+base[2]*base[2])*math.sqrt(pic[0]*pic[0]+pic[1]*pic[1]+pic[2]*pic[2])
#		cos = up/down
#		print(cos)
		x = x+1
#	print diff_list
	min_deff = min(diff_list)
#	print min_deff
	num = diff_list.index(min_deff)
	color_pat[num] = color_pat[num] + 1
#	print color_pat
#	count = count+1
#	if count == 100:
#		break
print color_pat
cur.execute("INSERT INTO landscape (id, name, url, red, yellow, yg, green, blue, purple, brown, pink, white, bk) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", [10, "j", "url", color_pat[0], color_pat[1], color_pat[2], color_pat[3], color_pat[4], color_pat[5], color_pat[6], color_pat[7], color_pat[8], color_pat[9]])
conn.commit()
cur.close()
conn.close()
#math about how much the 2 vectors same.
#for s in px:
#		s = str(s)
#		s = s.replace('(','')
#		s = s.replace(')','')
#		data = s.split(",")
#		datas = data[0]+","+data[1]+","+data[2]+"\n"
#		f.write(str(datas))
f.close()
