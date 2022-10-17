
def main():
    
    contArmstrong = 0

    for i in range(1, 501):
        stri = str(i)
        valuei = 0
        for digit in stri:
            valuei += int(digit)**3
        
        if valuei == i:
            contArmstrong += 1
            print(i)
    
    print(f"{contArmstrong}")

if __name__ == "__main__":
    main()