#-*- coding: utf-8 -*-
import random

maxSequence(n)
k=len(n)
p=[]
j=0
l=0
maxim=0
num=[]
for i in range (0,k):
    num[i]=i
random.suffle(num)
for j in n:
    for l in num:
        s=0
        for z in range(0,l):
            s=s+n[z]
        p[j][0]=n[j]
        p[j][0]=n[z]
        p[j][2]=s
for j in p:
    if (maxim<p[j][2]):
        maxim=p[j][2]
i=0
l=0
for i in p:
    if (maxim==p[i][2]):
        thesa=p[i][0]
        thest=p[i][1]
        for l in n:
            if (thesa==p[l][0]):
                tha=l
            if (thesb==p[l][1]):
                thb=l
        for j in range (tha,thb):
            print n[j]


n=input ("Give me a list of integers:")
maxSequence(n)





            
            
    
    
    
        

    
    
