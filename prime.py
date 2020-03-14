n = int(input("Enter a number"))
i = 2
for i in range(2,int((n+1)/2)):
    if(n%i == 0):
        print("it is not prime number")

if i == int(n/2):
    print("it is prime number")
        
        
    
    