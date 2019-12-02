import math

def main():
    
    # Read the file
    f = open("input.txt")

    total_sum = 0
    # Iterate through the items
    for line in f:
        number = int(line)
        number = number/3
        number = math.floor(number)
        number -= 2
        total_sum += number
    f.close()
    # Print our final number
    print(total_sum)

if __name__ == "__main__":
    main()