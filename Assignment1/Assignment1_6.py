##Code to print if a number is positive , nevgative or a zero

def chech(number):
    if(number > 0) :
        print("positive")
        return
    if(number < 0):
        print("negative")
        return
    else :
        print("ZERO")

if __name__ == "__main__" :
    number = int(input("Enter a number"))
    chech(number)
