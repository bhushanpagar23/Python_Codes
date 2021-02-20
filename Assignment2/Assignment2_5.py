##check if a number is prime or not

def checkPrime(number) :
    if (number <= 1) :
        print("Not prime")
        return
    for i in range(2,number) :
        if((number % i) == 0 ) :
            print("Not Prime")
            return 

    print("Prime")
if __name__ == "__main__" :
    number = int(input("Enter a number"))
    checkPrime(number)
        
