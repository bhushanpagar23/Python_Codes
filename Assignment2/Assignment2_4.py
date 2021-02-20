##Code to print addition of all factors of a number

def AddFactors(number):
    sum = 0
    factor = 1
    while(factor < number) :
        if((number % factor) == 0) :
            sum += factor
        factor = factor +1
    print("Addition of factors is :: ",sum)

if __name__ == "__main__" :
    number = int(input("Enter a number"))
    AddFactors(number)
