def Pattern(number) :
    temp = 1
    for i in range(number) :
        for j in range(temp) :
            print(j+1,end = " ") 
        temp = temp +1
        print("")

if __name__ == "__main__" :
    number = int(input("Enter a number : "))
    Pattern(number);
