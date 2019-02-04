i=int(input())
if(i%400==0):
    print ("leapyear")
elif(i%4==0):
    print ("leapyear")
elif(i%100!=0):
    print ("leapyear")
else:
    print ("not leapyear")
