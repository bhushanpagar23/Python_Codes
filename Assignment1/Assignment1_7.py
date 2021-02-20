#check if a number is divisible by 5

def DivideFive(number):
    if(number%5 == 0) :
        print("number is divisible by 5")
    else :
        print("Number is not divisible by 5")

if __name__ == "__main__":
    number = int(input("Enter a number"))
    DivideFive(number)
