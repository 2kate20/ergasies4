#-*- coding: utf-8 -*-
openning=open("ergb3.py","r")
lines=openning.readlines()
openning.close()

for line in lines:
        if "#" in line:  
            #Αν αρχίζει με "#"
            l=line.strip()
            if l[0]!="#":
                stg=line.split("#")
                n1=stg[0].count("'")
                n2=stg[0].count('"')
                if n1%2==1 or n2%2==1:
                    #Σε αλφαριθμητικό
                    print line
                else:
                    print line.split("#")[0]
        else:
            print list 
