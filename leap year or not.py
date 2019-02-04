i=int(input())
if(i%400==0):
    print ("yes")
elif(i%4==0):
    print ("yes")
elif(i%100!=0):
    print ("yes")
else:
    print ("no")
