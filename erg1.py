#-*- coding: utf-8 -*-
def sumIntervals(n):
    a=[] #Η αρχη καθε διαστήματος
    b=[] #το τέλος κάθε διαστήματος
    new1=[] # αρχη του διαστηματος
    new2=[]#το τελος του διαστηματος
    s=0
    i=0
    j=0
    g=0
    for i in n:
        if (i%2==0):
            a[j]=n[i]
        else:
            b[j]=n[i]
        j=j+1
    k=0
    for k in a:
        if (a[k]==a[k+1]):
            l=max(b[k],b[k+1])
            minim=a[k]
            maxim=l
        elif (b[k]==b[k+1]):
            l=min(a[k],a[k+1])
            nimin=l
            maxim=b[k]
        else:
            d1=a[k]
            h=0
            while (d1<b[k]):
                new1[h]=d1+1
            d2=a[k+1]
            h=0
            while (d2<b[k+1]):
                new2[h]=d2+1
            i=0
            flag=true
            while (flag==true and i<=h):
                if new1 in new2:
                    flag=false
                else:
                    i=i+1
            if (flag==false):
                minim=min(a[k],a[k+1])
                maxim=max(b[k],b[k+1])
    s=maxim-minim
    print s


n=input("Give me a list")
sumIntervals(n)
                
                
            
            
