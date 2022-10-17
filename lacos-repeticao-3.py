
def prime(number):

    if number == 1:
        return False

    if not (number % 2) or not (number % 3) or not (number % 5) or not (number % 7) :
        return True
    
    return False

def main():
    number =  int(input())

    flag = False

    for i in range(1,number+1):

        if not prime(i):
            continue

        for j in range(i, number + 1):

            if not prime(i):
                continue

            if i + j == number:
                print(i, j)
                flag = True

    if flag:
        print("É sim.")


if __name__ == "__main__":
    main()