
def main():
    number = int(input())

    for i in range(number + 1):
        print(" " * (number - i) , end="")

        for j in range(i):
            print(f"{i:2}", end="")
        
        print()

if __name__ == "__main__":
    main()