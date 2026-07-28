#single fact, representaion of one label data/ one value
#robot_location = "Room 3"
#print(robot_location)

#rooms = ["Room1", "Room2", "Room3"]
#print(rooms)
#print(len(rooms))


#robot_status ={
#    "location" : "Room3",
#    "battery " : 80,
#    "carry_item": False,
#}

#print(robot_status["location"])



#state = "off" #states is the storage of the system

#def toogle(state):
#    return "on" if state == "off" else "off" #rules

#state = toogle(state) #action
#print (state)


#connections = { #rules
#    "rooms 1" : ["room 1"],
#    "rooms 2" : ["room 1", "room 2"],
#    "rooms 3" : ["room 3", "room 4"],
#    "rooms 4" : ["room 3"],
#}

#current_state = "rooms 2" #states
#print("possible actions", connections[current_state]) #action


#def can_dispense(balance, price): #rule
#    return balance >= price

#balance, price = 20, 15 #state
#if can_dispense(balance, price):
#    balance -=price #actiom
#    print("Dispensed. Remaining:", balance)
#else:
#    print("Blocked: insufficient balance")   





#path_so_far = ["room 1", "room 2"]
#print("Visited so far:", path_so_far)

#path_so_far.append("room3")
#print("update path:", path_so_far)

#DICTIONARY/LIST
#maze ={"A": ["B"], "B": ["A", "C"], "C": ["B","D"], "D": ["A","C"]}
#print(maze)
#print(maze["B"])

#student = [{"name": "Marco", "score": 88}, {"name": "Diane", "score": 90}]
#for s in student:
#    print(s["name"], "scored", s["score"])
#main topic: searching the problems

#maze ={"A": ["B"], "B": ["A", "C"], "C": ["B","D"], "D": ["A","C"]}

#start, goal ="A", "D"
#frontier = maze[start]
#search_space = list(maze.keys())

    #node = "C" -me
    #frontier = maze[node] -me


#print(frontier)
#print(search_space)
#print(goal in frontier)

#current = start
#path = [current]

#while current != goal:
#    frontier = maze[current]
#    for neighbor in frontier:
#        if neighbor not in path:
#            current = neighbor
#            path.append(current)
#            break
#print(path)
#print(current == goal)

#maze ={
#    "A": ["B", "C"], 
#    "B": ["A", "D", "F"], 
#    "C": ["A", "F"], 
#    "D": ["B"],
#    "E": ["B"],
#    "F": ["C", "G"],
#    "G": ["F"]
#    }

#def dfs_find_path(maze, start, goal, path=None):
#    if path is None:
#        path = [start]
#    else:
#        path = path + [start]
#   print("visiting:", start, "| Path so far:", path)

#    if start == goal:
#        return path
#    for neighbor in maze[start]:
#       if neighbor not in path:
#           result = dfs_find_path(maze, neighbor, goal, path)
#            if result:
#                return result
#    return None
#print(dfs_find_path(maze,"A", "G"))

from collections import deque
maze = {
    "A": ["C", "D"], 
    "B": ["A", "C", "B"], 
    "C": ["D", "E"], 
    "D": ["A", "B"],
    "E": ["G"],
    "F": ["D", "F"],
    "G": ["A"]
    }

def bfs_find_maze(maze, start, goal):
    queue = deque([[start]])
    visited = set ()

    while queue:
        path = queue.popleft()
        node = path[-1]

        print("Exploring:", path)

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)
            for neighbor in maze[node]:
                queue.append (path + [neighbor])
    return None
print(bfs_find_maze(maze, "A", "G"))