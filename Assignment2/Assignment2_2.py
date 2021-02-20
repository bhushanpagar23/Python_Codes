#Code to print * pattern

def Pattern(number) :
    for x in range(number):
        for y in range(number):
            print("*",end = " ")
        print("")

if __name__ == "__main__" :
    number = int(input("Enter a number ::"))
    Pattern(number)
