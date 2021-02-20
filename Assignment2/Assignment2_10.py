def sumDigits(number) :
    sum = 0;
    while(number > 0) :
        sum += int(number%10)
        number = number /10
    print(sum)

if __name__ == "__main__":
    number = int(input("Enter a number"))
    sumDigits(number)
