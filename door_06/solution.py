# We need the right data structure to accomodate for this!
# Worst case we need to search the tree every time!
# Idea save everythin in a tree! putting it all in a tree should be straight forward!
# Problem how can we do the insert efficiently? Do we need to save a point with every planet in a dictionary so we can acess it quicker? => Most probably, and this only takes linear space, since its only pointers!
# Let's do this

from collections import defaultdict
def solve_part_1(orbit_list):
    all_pointers = defaultdict(list)
    #This does not need to be a defaultdict since we will only iterate through it
    start_pointers = {}
    for el in orbit_list:
        left_planet, right_planet = el.split(")")
        if all_pointers[left_planet] == []:
            if all_pointers[right_planet] == []:
                all_pointers[right_planet] = {}
            new_dic = {}
            new_dic[right_planet] = all_pointers[right_planet]
            all_pointers[left_planet] = new_dic
            start_pointers[left_planet] = all_pointers[left_planet]
        else:
            if all_pointers[right_planet] == []:
                all_pointers[right_planet] = {}

            all_pointers[left_planet][right_planet] = all_pointers[right_planet]
        
        # Delete so start_pointers only has planest that are not orbiting anything else
        try:
            del start_pointers[right_planet] 
        except:
            pass
    # Now lets calculate the number
    # We can do this recursively, which is easier to program
    print(all_pointers)
    print(start_pointers.items())
    return calculate_orbit_number(start_pointers, 0)

    

def solve_part_2(orbit_list):
    # TODO
    # Give each node a list of the nodes they are connected to
    # Implement depth first search
    # 1. Get it to run without depth first search and just the new data structure 
    all_pointers = defaultdict(list)
    #This does not need to be a defaultdict since we will only iterate through it
    start_pointers = {}
    for el in orbit_list:
        left_planet, right_planet = el.split(")")
        if all_pointers[left_planet] == []:
            if all_pointers[right_planet] == []:
                all_pointers[right_planet] = ({},left_planet)
            else:
                all_pointers[right_planet] = all_pointers[right_planet][0], left_planet 
            new_dic = {}
            new_dic[right_planet] = (all_pointers[right_planet][0],left_planet)
            all_pointers[left_planet] = (new_dic,"")
            start_pointers[left_planet] = all_pointers[left_planet]
        else:
            if all_pointers[right_planet] == []:
                all_pointers[right_planet] = {},left_planet
            else:
                all_pointers[right_planet] = all_pointers[right_planet][0], left_planet 

            all_pointers[left_planet][0][right_planet] = all_pointers[right_planet]
        
        # Delete so start_pointers only has planest that are not orbiting anything else
        try:
            del start_pointers[right_planet] 
        except:
            pass
    # Now lets calculate the number
    # We can do this recursively, which is easier to program
    fr = all_pointers["YOU"][1]
    to = all_pointers["SAN"][1]
    print(to)
    return depth_search(fr, to, defaultdict(bool), all_pointers)




def calculate_orbit_number(planet: dict, depth):
    if planet == {}:
        return 0
    ret = 0
    for (name, dic) in planet.items():
        print(f"{name},{depth}")
        ret = ret + calculate_orbit_number(dic, depth+1) + depth
    return ret

def calculate_orbit_number_2(planet: dict, depth):
    if planet == {}:
        return 0
    ret = 0
    for (name, dic) in planet.items():
        print(f"{name},{depth}")
        ret = ret + calculate_orbit_number_2(dic[0], depth+1) + depth
    return ret

def depth_search( fr, to, visited, all_pointers ):
    if fr == to:
        return 0
    if fr == '':
        return -1
    visited[fr] = True
    ret = -1
    print(fr)
    print(all_pointers[fr])
    for name,dic in all_pointers[fr][0].items():
        if not visited[name]:
            ret = depth_search(name, to, visited, all_pointers)
        if ret != -1:
            return ret +1
    name = all_pointers[fr][1]
    if not visited[name]:
            ret = depth_search(name, to, visited, all_pointers)
    if ret != -1:
        return ret +1
    return -1



def main():
    f = open("input.txt","r")
    lines = f.read().splitlines()
    solve = solve_part_2(lines)
    print(solve)


if __name__ == "__main__":
    main()


