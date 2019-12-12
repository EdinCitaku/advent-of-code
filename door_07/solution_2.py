import itertools
import threading
import time
def execute_opcode(inputlist: list, position: int, e: threading.Event, main_thread: threading.Event) -> int:
    "Executes the OPCode on position p"
    op = inputlist[position]
    print(op)
    parameters = []
    if len(op) >2 :
        # Parameter mode 1
        # We have to make a distincion because of leading zeros!
        mode = "1"
        get_parameter = {}
        get_parameter[1]  =lambda p: int(inputlist[p])
        get_parameter[0] = lambda p : int(inputlist[int(inputlist[p])])
        input_parameters = inputlist[position][:-2]
        op = int(inputlist[position][-2:])
        # Extract the parameters
        # We first need to add leading zeroes 
        # We expect a length of 3 for if opcode 1,2 and length 1 for opcode 3,4
        if op in (1,2,7,8):
            # Expect length 3
            input_parameters = input_parameters.zfill(3)
        if op in (3,4):
            # Expect length 1
            input_parameters = input_parameters.zfill(1)
        if op in (5,6):
            # Expect lenght 2
            input_parameters = input_parameters.zfill(2)
        input_parameters = input_parameters[::-1]
        for i in range(len(input_parameters)):
            parameters.append(get_parameter[int(input_parameters[i])](position+i+1))
    else:
        # Parameter mode 0
        mode = "0"
        get_parameter = lambda p : int(inputlist[int(inputlist[p])])
        op = int(inputlist[position])
        if op in (1,2,7,8):
            parameters.append(get_parameter(position+1))
            parameters.append(get_parameter(position+2))
            parameters.append(get_parameter(position+3))
        if op in (3,4):
            parameters.append(get_parameter(position+1))
        if op in (5,6):
            parameters.append(get_parameter(position+1))
            parameters.append(get_parameter(position+2))




    # Fill a list with parameters 
    def set_result(p, value):
        if p <1:
            raise Exception("Trying to write to wrong field")
        if mode == "0":
            inputlist[int(inputlist[position + p])] = str(value)
            return
        if int(input_parameters[p-1]) == 0:
            inputlist[int(inputlist[position + p])] = str(value)
        if int(input_parameters[p-1]) == 1:
            inputlist[position + p] = str(value)
    
    # Here we execute the actual operation
    if(op == 1):
        # Addition
        left, right, goal = parameters
        result = left + right
        set_result(3,result)
        return position + 4
    if(op == 2):
        # Multiplikation
        left,right,goal = parameters
        result = left * right
        set_result(3,result)
        return position + 4
    
    if(op == 3):
        # Save input
        set_result(1, call_input_instruction())
        return position + 2

    if(op == 4):
        # Print output
        parameter = parameters[0]
        call_output(parameter)
        print(f"Output: {parameter}") 

        main_thread.set()
        e.clear()
        e.wait()
        
        return position + 2
    
    if(op == 5):
        # Jump if true
        parameter = parameters[0]
        if parameter != 0:
            return parameters[1]
        else:
             return position + 3

    if(op == 6):
        # Jump if false
        parameter = parameters[0]
        if parameter == 0:
            return parameters[1]
        else:
             return position + 3
    
    if(op == 7):
        # Less than
        left, right, goal = parameters
        result = (0,1 ) [left < right]
        set_result(3, result)
        return position + 4
    
    if(op == 8):
        # equals
        left, right, goal = parameters
        result = (0,1 ) [left == right]
        set_result(3, result)
        return position + 4



    if(op==99):
        #Program End
        return -1
    raise Exception(f"OP Code {op} not recognized")


def call_input_instruction():
    print("popped input")
    return input_p.pop(0)

def call_output(n):
    global output
    output = n

def execute_instructions(positions, e, main_thread):    
    #Current position of the program counter
    pc = 0

    while (pc < len(positions) and pc != -1):
        pc = execute_opcode(positions, pc, e, main_thread)
    print("clearing")
    main_thread.set()
    return positions[0]


def solve_part_1(positions):
    global input_p
    global output

    ret = -1
    for permutation in list(itertools.permutations([5,6, 7, 8,9])):
        print(permutation)
        output = 0
        thread_list = []
        e_list = []
        main_thread = threading.Event()
        for el in permutation:
            e_list.append(threading.Event())

        for idx,el in enumerate(permutation):

            iter_positions = positions.copy()
            t = threading.Thread(target=execute_instructions, name=f"thread_{idx}", args=(iter_positions, e_list[idx], main_thread) )
            thread_list.append(t)
        first_iteration = True
        while(thread_list[-1].is_alive() or first_iteration):
            for idx, t in enumerate(thread_list):
                if first_iteration:
                    input_p = [permutation[idx],output]

                    t.start()
                    main_thread.wait()
                    main_thread.clear()
                else:
                    #Now we need to wait until our thread is finished
                    input_p.append(output)
                    e_list[idx].set()
                    main_thread.wait()
                    main_thread.clear()
            print('first_iteration_over')
            first_iteration = False
        print("cleared")

        if output > ret:
            ret = output
    return ret





if __name__ == "__main__":
    f = open("input.txt",'r')
    positions = f.read().split(',')


    solution = solve_part_1(positions)
    print(solution)
