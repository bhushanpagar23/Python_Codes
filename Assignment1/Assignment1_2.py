##Code to check if given number is even or odd

def chkNum(number) :
    if (number%2 == 0):
        print("even number")
    else :
        print("odd number")

if __name__ == "__main__" :
    number = int(input("Enter a number"))
    chkNum(number)
