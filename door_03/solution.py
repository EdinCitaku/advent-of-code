import math
from collections import defaultdict

def solve_part_1(first_path : list, second_path: list) -> (int, int):
    
    center_point = [0,0]
    current_coordinate = center_point.copy()
    board = defaultdict(bool)
    #Let's iterate through the first path
    for instruction in first_path:
        for idx in range(int(instruction[1:])):
            update_coordinate(current_coordinate, instruction[0])
            board[(current_coordinate[0],current_coordinate[1])] = True
    
    current_coordinate = center_point.copy()
    min_md = -1
    for instruction in second_path:
        #Either R, L, U, D
        for idx in range(int(instruction[1:])):
                #Change the x_coordinate
                update_coordinate(current_coordinate, instruction[0])
                #Update our board
                if(board[(current_coordinate[0],current_coordinate[1])]):
                    md = calculate_manhattan_distance(center_point, current_coordinate)
                    if min_md == -1 or md < min_md:
                        min_md = md
    return min_md

def solve_part_2(first_path : list, second_path: list) -> (int, int):
    
    center_point = [0,0]
    steps = 0
    current_coordinate = center_point.copy()
    board = defaultdict(int)
    #Let's iterate through the first path
    for instruction in first_path:
        for idx in range(int(instruction[1:])):
            update_coordinate(current_coordinate, instruction[0])
            steps +=1
            board[(current_coordinate[0],current_coordinate[1])] = steps
    
    steps = 0
    current_coordinate = center_point.copy()
    min_md = -1
    for instruction in second_path:
        #Either R, L, U, D
        for idx in range(int(instruction[1:])):
                #Change the x_coordinate
                update_coordinate(current_coordinate, instruction[0])
                #Update our board
                steps +=1
                #board is 0 when it was not visited
                steps_first_wire = board[(current_coordinate[0],current_coordinate[1])]
                if( steps_first_wire != 0):
                    md = steps + steps_first_wire
                    if min_md == -1 or md < min_md:
                        min_md = md
    return min_md



def update_coordinate(coordinate, instruction):
    if instruction == 'R':
        coordinate[0] += 1
    if instruction == 'L':
        coordinate[0] -= 1
    if instruction == 'U':
        coordinate[1] += 1
    if instruction == 'D':
        coordinate[1] -= 1

def calculate_manhattan_distance(c1, c2):
    
    return (abs(c1[0]-c2[0]) + abs(c1[1]-c2[1]))

def main():
    f = open("input.txt")
    first_path = f.readline().split(',')
    second_path = f.readline().split(',')
    md = solve_part_2(first_path, second_path)
    print(md)

if __name__ =="__main__":
    main()