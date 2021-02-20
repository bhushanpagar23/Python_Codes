##Code to print first 10 even numbers on screen

def PrintEven() :
    even = 2
    count = 0
    while count < 10 :
        print(even,end = " ")
        even = even +2
        count += 1

if __name__ == "__main__" :
    PrintEven()
