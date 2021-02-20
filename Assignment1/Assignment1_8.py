##Code to print **

def printStar(number) :
    for x in range(number):
        print("*",end = " ")

if __name__ == "__main__" :
    number = int(input("Enter a number"))
    printStar(number)
