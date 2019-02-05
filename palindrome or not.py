def main():
 i=int(input(""))
 temp=i
 rev=0
 while(i>0):
    dig=i%10
    rev=rev*10+dig
    i=i//10
 if(temp==rev):
    print("Yes")
 else:
    print("No")

if __name__ == '__main__':
    main()
