def solve_part_1(inputlist : list) -> int:
    
    #Current position of the program counter
    pc = 0

    while (pc < len(inputlist) and pc != -1):
        pc = execute_opcode(inputlist, pc)
    
    return inputlist[0]

def execute_opcode(inputlist: list, position: int) -> int:
    "Executes the OPCode on position p"
    op = inputlist[position]
    left = inputlist[inputlist[position+1]]
    right = inputlist[inputlist[position+2]]
    # Here we execute the actual operation
    if position + 4 >= len(inputlist):
        raise Exception("List to short")
    if(op==1):
        # Addition
        result = left + right
        inputlist[inputlist[position+3]] = result
        return position + 4
    if(op==2):
        # Multiplikation
        result = left * right
        inputlist[inputlist[position+3]] = result
        return position + 4
    if(op==99):
        #Program End
        return -1
    raise Exception("OP Code not recognized")





if __name__ == "__main__":
    f = open("input.txt",'r')
    positions = f.read().split(',')
    positions = list(map(int,positions))
    positions[1] = 12
    positions[2] = 2
    print(positions)
    solution = solve_part_1(positions)
    print(solution)
