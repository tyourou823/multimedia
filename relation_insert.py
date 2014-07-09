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

def read_color(pic):
	list1 = [0.,0.,0.,0.,0.,0.,0.,0.,0.,0.]

	cur.execute("select red from landscape where landscape.name=%s;",[pic])
	element1=cur.fetchone()
#	print element1
	element1=ttoi(element1)
	list1[0]=element1
	cur.execute("select yellow from landscape where landscape.name=%s;",[pic])
	element1=cur.fetchone()
	element1=ttoi(element1)
	list1[1]=element1
	cur.execute("select yg from landscape where landscape.name=%s;",[pic])
	element1=cur.fetchone()
	element1=ttoi(element1)
	list1[2]=element1
	cur.execute("select green from landscape where landscape.name=%s;",[pic])
	element1=cur.fetchone()
	element1=ttoi(element1)
	list1[3]=element1
	cur.execute("select blue from landscape where landscape.name=%s;",[pic])
	element1=cur.fetchone()
	element1=ttoi(element1)
	list1[4]=element1
	cur.execute("select purple from landscape where landscape.name=%s;",[pic])
	element1=cur.fetchone()
	element1=ttoi(element1)
	list1[5]=element1
	cur.execute("select brown from landscape where landscape.name=%s;",[pic])
	element1=cur.fetchone()
	element1=ttoi(element1)
	list1[6]=element1
	cur.execute("select pink from landscape where landscape.name=%s;",[pic])
	element1=cur.fetchone()
	element1=ttoi(element1)
	list1[7]=element1
	cur.execute("select white from landscape where landscape.name=%s;",[pic])
	element1=cur.fetchone()
	element1=ttoi(element1)
	list1[8]=element1
	cur.execute("select bk from landscape where landscape.name=%s;",[pic])
	element1=cur.fetchone()
	element1=ttoi(element1)
	list1[9]=element1

	return list1

def compare(sample1,sample2):
	x=0
#	while x<=9:
#		cur.execute("select red from landscape where landscape.name=%s;",[sample1])
#		element1=cur.fetchone()
#		print element1
#		element1=ttoi(element1)
#		list1[x]=element1
#		x = x+1
	element1 = read_color(sample1)
	while x <= 9:
		element1[x] = float(element1[x])
		x = x +1
	array1 = np.array([element1[0]/10,element1[1]/10,element1[2]/10,element1[3]/10,element1[4]/10,element1[5]/10,element1[6]/10,element1[7]/10,element1[8]/10,element1[9]/10])
	array1_len = math.sqrt(np.dot(array1,array1))
	array1 = array1/array1_len
#	x=0
#	while x<=9:
#		cur.execute("select %s from landscape where landscape.name=%s;",(pic_color_list[x],sample2))
#		element1=cur.fetchone()
#		element1=ttoi(element1)
#		list1[x]=element1
#		x = x+1
	number = 0
	element1 = read_color(sample2)
	while number <= 9:
		element1[number] = float(element1[number])
		number = number +1
	array2 = np.array([element1[0]/10,element1[1]/10,element1[2]/10,element1[3]/10,element1[4]/10,element1[5]/10,element1[6]/10,element1[7]/10,element1[8]/10,element1[9]/10])
	print array2
#	while number <= 9:
#		array2[number] = long(array2[number])
#		print array2[number]
#
#		number = number + 1
#	number =0
#	while number <= 9:
#		test[number] = long(test[number])
#		test[number] = test[number]**2
#		print test
#		test[number] = math.sqrt(test[number])
#		number = number + 1
#	array2_len = math.sqrt(test)
	array2_len = math.sqrt(np.dot(array2,array2))
	array2 = array2/array2_len


	up = array1[0]*array2[0]+array1[1]*array2[1]+array1[2]*array2[2]+array1[3]*array2[3]+array1[4]*array2[4]+array1[5]*array2[5]+array1[6]*array2[6]+array1[7]*array2[7]+array1[8]*array2[8]+array1[9]*array2[9]
	down = math.sqrt(+array1[0]**2+array1[1]**2+array1[2]**2+array1[3]**2+array1[4]**2+array1[5]**2+array1[6]**2+array1[7]**2+array1[8]**2+array1[9]**2)*math.sqrt(array2[0]**2+array2[1]**2+array2[2]**2+array2[3]**2+array2[4]**2+array2[5]**2+array2[6]**2+array2[7]**2+array2[8]**2+array2[9]**2)
	cos = up/down
#	print(cos)

	return cos

conn = psycopg2.connect("dbname=multimedia host=localhost user=sae password=1233701sm")
cur = conn.cursor()

color_list = [u'red',u'yellow',u'yellow green',u'green',u'blue',u'purple',u'brown',u'pink',u'white',u'black']
pic_color_list= [u'red',u'yellow',u'yg',u'green',u'blue',u'purple',u'brown',u'pink',u'white',u'bk']
list1 = [0,0,0,0,0,0,0,0,0,0]
list2 = [0,0,0,0,0,0,0,0,0,0]
result_list = [0,0,0,0,0,0,0,0,0,0]
test = [0,0,0,0,0,0,0,0,0,0]

picture = raw_input('type the picture name : ')
print picture
num = 0
cur.execute("select name from landscape where not landscape.name=%s;",[picture])
name=cur.fetchall()
print name
#while num<=8: 
#	print name[num]
#	var = str(name[num])
#	var = var.replace("(","")
#	var = var.replace(")","")
#	var = var.replace(",","")
#	var = var.replace("'","")
#	print var
result_list[0] = compare(picture,'a')
cur.execute("insert into result(name,result) values(%s,%s)",['a',result_list[0]])
result_list[1] = compare(picture,'b')
cur.execute("insert into result(name,result) values(%s,%s)",['b',result_list[1]])
result_list[2] = compare(picture,'c')
cur.execute("insert into result(name,result) values(%s,%s)",['c',result_list[2]])
result_list[3] = compare(picture,'d')
cur.execute("insert into result(name,result) values(%s,%s)",['d',result_list[3]])
result_list[4] = compare(picture,'e')
cur.execute("insert into result(name,result) values(%s,%s)",['e',result_list[4]])
result_list[5] = compare(picture,'f')
cur.execute("insert into result(name,result) values(%s,%s)",['f',result_list[5]])
result_list[6] = compare(picture,'g')
cur.execute("insert into result(name,result) values(%s,%s)",['g',result_list[6]])
result_list[7] = compare(picture,'h')
cur.execute("insert into result(name,result) values(%s,%s)",['h',result_list[7]])
result_list[8] = compare(picture,'i')
cur.execute("insert into result(name,result) values(%s,%s)",['i',result_list[8]])
result_list[9] = compare(picture,'j')
cur.execute("insert into result(name,result) values(%s,%s)",['j',result_list[9]])

#	num = num +1
print result_list
max_result_list = max(result_list)
result_list.remove(max_result_list)
print result_list
cur.execute("select landscape.name,landscape.url,result.result from landscape,result where landscape.name=result.name order by result.result;")
result = fetchall()
print result
conn.commit()
cur.close()
conn.close()