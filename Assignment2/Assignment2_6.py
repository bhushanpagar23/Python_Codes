def Pattern(number) :
    for i in range(number) :
        for j in range(i,number) :
            print("*",end = " ")
        print("")

if __name__ == "__main__":
    number = int(input("Enter a number"))
    Pattern(number)
