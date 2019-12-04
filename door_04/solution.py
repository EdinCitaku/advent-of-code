def solve_part1(input_range : (int,int)) -> int:
    range_l, range_r = input_range
    counter = 0
    for n in range(range_l, range_r):
        if(check_digit_part1(n)):
            counter +=1
    return counter
            
def solve_part2(input_range : (int,int)) -> int:
    range_l, range_r = input_range
    counter = 0
    for n in range(range_l, range_r):
        if(check_digit_part2(n)):
            counter +=1
    return counter
            

def check_digit_part1(n: int) -> bool:
    previous_digit = -1
    double_digit = False
    for digit in str(n):
        if(int(digit)) > previous_digit:
            previous_digit = int(digit)
        elif int(digit) == previous_digit:
            double_digit = True
        else:
            return False
    return double_digit


def check_digit_part2(n: int) -> bool:
    previous_digit = -1
    previous_previous_digit = -1
    double_digit = False
    ret = False
    for digit in str(n):
        if(int(digit)) > previous_digit:
            previous_previous_digit = previous_digit
            previous_digit = int(digit)
            if double_digit:
                ret = True
        elif int(digit) == previous_digit:
            if(previous_previous_digit == int(digit)):
                double_digit = False
            else:
                double_digit = True
                previous_previous_digit = previous_digit
        else:
            return False
    return ret or double_digit



def main():
    count = solve_part1((125730,579381))
    print(count)

if __name__ =="__main__":
    main()