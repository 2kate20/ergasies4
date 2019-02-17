#-*- coding: utf-8 -*-
num=input("Give me an integer:")
while (num<=1 or num>1000000):
   num=input("Give me an integer:") 
i=2
a=[]#οι πρωτοι αριθμοι
b=[]#οι επαναληψεις των πρωτων αριθμων
j=0
p=[]
while (i<=num and num>1):
    k=0
    while (num%i==0):
        num=num/i
        k=k+1
    if (k!=0):
       #διαιρειται πληρως και το πληθος των επαναληψεων
       b.append(k)
       a.append(i)
       j=j+1
    i=i+1
i=0
for i in range (0,j):
    if (b[i]==1):
        p.append( a[i] )
    elif (b[i]!=0):
        p.append( a[i])
        p.append( '**' )
        p.append(b[i])
                  
print (p)
    

#Το αποτελεσμα θα ειναι της μορφης [χ,'**',ψ,ζ,'**',π]
#και εννοειται ως (χ^ψ)*(ζ^π)
    
