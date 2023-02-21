from tkinter import *

def callback(r,c,cell):
    sudoku_grid[r][c][cell].configure(text='Clicked')
    

sudoku_grid = [[[cell for cell in range(1,10)]for c in range(3)] for r in range(3)]
sudoku_grid_copy = [[[cell for cell in range(1,10)]for c in range(3)] for r in range(3)]
    

root=Tk()

column_count=0
row_count=0
for i in range(3):
    for j in range(3):
        if j==0:
            column_count=0
        else:
            column_count=j*3
        if i==0:
            row_count=0
        else:
            row_count=i*3            
        for k in range(0,7,+3):            
            sudoku_grid[i][j][k]=Button(font=('Verdana', 12),text='{}'.format(sudoku_grid_copy[i][j][k]),background='grey',width=5,height=3,command= lambda r=i,c=j,cell=k:callback(r,c,cell))
            sudoku_grid[i][j][k].grid(row=row_count, column=column_count)            
            sudoku_grid[i][j][k+1]=Button(font=('Verdana', 12),text='{}'.format(sudoku_grid_copy[i][j][k+1]),background='grey',width=5,height=3,command= lambda r=i,c=j,cell=k+1:callback(r,c,cell))
            sudoku_grid[i][j][k+1].grid(row=row_count, column=column_count+1)      
            sudoku_grid[i][j][k+2]=Button(font=('Verdana', 12),text='{}'.format(sudoku_grid_copy[i][j][k+2]),background='grey',width=5,height=3,command= lambda r=i,c=j,cell=k+2:callback(r,c,cell))
            sudoku_grid[i][j][k+2].grid(row=row_count, column=column_count+2)   
            row_count+=1
    

mainloop()

