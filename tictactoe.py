# I N C O M P L E T E

board = [['X','X',''],['','O',''],['','S','']]

print (r'Use "mid/left/right + up/mid/down" to put ticks on the specified positions')

def printBoard(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            print('|'+str(board[i][j])+ '|', end = ' ')
        print()    
        print('--------')
        
def rowEqual (list):
    flag = list[0]
    for i in range(len(list)):
        if list[i] == flag: 
            continue
        else:
            flag = False
    return flag == list[0]




print(rowEqual(board[0]))
# def logic (board):
