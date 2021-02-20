def Pattern(number) :
    for i in range(number) :
        for j in range(number) :
            print(j+1,end = " ")
        print("")

if __name__ == "__main__" :
    number =  int(input("Enter a number"))
    Pattern(number)
