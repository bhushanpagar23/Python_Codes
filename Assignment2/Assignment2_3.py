def Factorial(number) :
    res = 1
    while number > 0 :
        res = res * number
        number = number - 1
    print("Factorial is ", res)

if __name__ == "__main__" :
    number = int(input("Enter a number"))
    Factorial(number)
