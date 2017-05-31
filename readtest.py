#!/usr/bin/env python
#-*- coding:utf-8 -*-
import re
import sys
f= open(r'D:\learning\pylearn\test531.csv','r')
fout= open(r'D:\learning\pylearn\test531_out.csv','w')
# fneg= open(r'D:\learning\pylearn\neg.txt','w')
# fout1= open(r'D:\learning\pylearn\testnot1.txt','w')
rule=['TCL','tcl','李东生','雷鸟','铁粉','t c l','Tcl','黑莓','TCLS960','TCL950','ＴＣＬ','TcL','TCl']
rule2=[
r'券http://',
r'[a-zA-Z0-9]+Tcl',
r'[a-zA-Z0-9]+tcl',
r'[a-zA-Z0-9]+tCl',
r'[a-zA-Z0-9]+tcL',
r'[a-zA-Z0-9]+tCL',
r'[a-zA-Z0-9]+TCL',
r'[a-zA-Z0-9]+TCl',
r'tcL[a-zA-Z0-9]+',
r'tCl[a-zA-Z0-9]+',
r'tcl[a-zA-Z0-9]+',
r'Tcl[a-zA-Z0-9]+',
r'tCL[a-zA-Z0-9]+',
r'TCL[a-zA-Z0-9]+',
r'TCl[a-zA-Z0-9]+',
r'[\w\W]+-[\w\W]+http',
]
rule3=[]
f3=open(r'D:\learning\pylearn\yuliao\neg_words0519.txt','r')
linesneg=f3.readlines()
for line in linesneg:
	rule3.append(line[:-1])

# lines=f.readlines()
# line=lines[333]
# print line
# for word2 in rule2:
# 	m2=re.search(word2,line)
# 	print m2
c=0
for i,line in enumerate(f):
	line1=line.split(',')
	label=line1[0]
	score=line1[1]
	weibo=line1[2]
	# weibo=line
	m1=None
	m2=None
	m3=None
	lab='0'	
	if m1==None:
		lab='2'
	for word1 in rule:
		m1=re.search(word1,weibo)
		if m1:
			lab='0'
			c=c+1
			break
	for word2 in rule2:
		m2=re.search(word2,weibo)
		if m2:
			lab='2'
			break	
	for word3 in rule3:
		m3=re.search(word3,weibo)
		if m3:
			lab='0'
			break
	fout.write(lab+','+line)
	
	
	if i%1000==0:
		print >> sys.stderr, 'loading %s(%s)' % ('test531.csv', i) 
print c
	
