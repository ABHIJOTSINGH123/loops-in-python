n=int(input("Enter the number"))
if n>1:
     if n==3:
           print(f"{n} is a prime")
     for i in range(2,int(n**0.5)+1):
        if n%i==00:
            print(f"{n} is not a prime number")
            break
       
        else:
         print(f"{n} is  a prime")
         break

else:
    print(f"{n} is not a prime number") 
