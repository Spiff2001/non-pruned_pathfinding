from array import array
from multiprocessing import Array
import random

import time
from graphics import *

def generate_grid():
    rows=10
    cols=10
    grid = [[random.randint(1,100) for  i in range (rows)] for j in range(cols)]
    for i in grid:
        print(i)
    return grid
    

grid=generate_grid()


stable_grid=[[35, 7, 92, 66, 9], [27, 37, 44, 34, 93], [80, 8, 57, 51, 32], [26, 61, 38, 37, 60], [55, 34, 75, 76, 74]]

class path:
    possible_path =[]
    weight=0
    def __init__(self,input_path,input_weight):
        self.possible_path = input_path
        self.weight=input_weight

# what do you need this to do? 



# figure out an efficient way to store the weights of completed paths so that the system can prune.
paths_list=[]
def pathfinder(input_grid,input_moves=[],input_weight=0):
    # if len(input_grid)==5 and len(input_grid[0])==5:
    #     paths_list=[]
    right=[1]
    down=[3]
    diagonal=[2]
    current_weight=input_weight + input_grid[0][0]

    current_path = path(input_moves,current_weight)
    
    
    
    
    
    if len(input_grid[0]) == 1 and len(input_grid) == 1:      
        
        paths_list.append(current_path)

        
    
    #move diagonally possibility 
    if len(input_grid[0])>1 and len(input_grid)>1:
        grid_sans_row_and_column= [[ i for  i in input_grid[x][1:]] for x in range(len(input_grid))][1:]  
        move_diagonally=input_moves+diagonal
        pathfinder(grid_sans_row_and_column,move_diagonally,current_weight)

    #move down possibility 
    if len(input_grid)>1 and len(input_grid[0])>0:
        grid_sans_row = input_grid[1:]
        move_down=input_moves+down 
        pathfinder(grid_sans_row,move_down,current_weight)
    #move right possibility
    if len(input_grid[0])>1:
        grid_sans_column =  [[ i for  i in input_grid[x][1:]] for x in range(len(input_grid))]
        move_right=input_moves+right
        pathfinder(grid_sans_column,move_right,current_weight)

    

def sort_paths(input_grid):
    pathfinder(input_grid)
    lightest =0
    lightest_path=[]
    heaviest = 0
    heaviest_path=[]
    for path in paths_list:
        if path.weight>heaviest:
            heaviest=path.weight
            heaviest_path=path.possible_path
        if path.weight<lightest or lightest==0:
            lightest=path.weight
            lightest_path=path.possible_path
    print("weightiest:"+str(heaviest))
    print(heaviest_path)
    print("lightest:"+str(lightest))
    print(lightest_path)

    #graphics area
    grid_win = GraphWin("pathfinder", 400, 400)
    for y in range(len(input_grid)):
        row=input_grid[y]
        for x in range(len(row)):
            grid_square=Rectangle(Point(x*40,y*40), Point(x*40+40,y*40+40))
            grid_square.draw(grid_win)
            grid_square.setFill(color_rgb(255-row[x]*2,255-row[x]*2,255))
            
    # pathways
    graphical_pathways(lightest_path,grid_win,"green")
    time.sleep(2)
    graphical_pathways(heaviest_path,grid_win,"red")

    grid_win.getMouse()

def graphical_pathways(input_list,window,color,start_x=20,start_y=20):
    
    move=input_list[0]
    rest = input_list[1:]
        
    if move ==1:
        end_x=start_x+40
        end_y=start_y
    elif move ==2:
        end_x = start_x+40
        end_y = start_y+40
    else:
        end_x=start_x
        end_y=start_y+40

    move_line = Line(Point(start_x,start_y), Point(end_x,end_y))
    move_line.setArrow("last")
    move_line.setOutline(color)
    move_line.draw(window)

    if not len(rest)==0:
        graphical_pathways(rest,window,color,end_x,end_y)
        
# win = GraphWin("My Circle", 100, 100)
#     c = Circle(Point(50,50), 10)
#     c.draw(win)
#     win.getMouse() # pause for click in window
#     win.close()

sort_paths(grid)


# c = Circle(Point(100,100), 200)
# c.draw(win)
# win.getMouse() # pause for click in window



#win.close()

#def graphical_pathfinding(input_grid):
    
    # x_counter=0
    # y_counter=0
    # while x_counter<len(input_grid):
    #     x_counter+=1
    #     x_position=x_counter*10
    #     while y_counter<len(input_grid[x_counter]):
    #         y_counter+=1
    #         y_position = y_counter*10
    #         rect = Rectangle(Point(x_position,y_position),Point(x_position+10,y_position+10))
    #         rect.draw(win)










# win = GraphWin("My Circle", 100, 100)
# c = Circle(Point(50,50), 10)
# c.draw(win)
#win.getMouse() # pause for click in window


# for path in paths_list[50:]:
#     print(path.possible_path)


   # print(this_path.possible_path)


        # you need three branching recursions, a way to prune useless recursion, and a way to prune the grid by 1 row and 1 column each theoretical move.
