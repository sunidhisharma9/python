board=[' ',' ',' ',' ',' ',' ',' ',' ',' ']

def check():
    for i in range(0,3,3):
        if board[i]==board[i+1]==board[i+2]!=' ':
            return board[i]
    for i in range(0,3):
        if board[i]==board[i+3]==board[i+6]!=' ':
            return board[i] 
    if board[0]==board[4]==board[8]!=' ':
        return board[0]
    elif board[2]==board[4]==board[6]!=' ':
        return board[0]
    else:
        return 'N'

def play(turn):
    index=int(input("Player %s:" %(turn)))
    while index not in range(0,9):
        print "Invalid index, please specify between 0-8"
        index=int(input("Player %s:" %(turn)))
    if board[index]==' ':
        board[index]=turn
    else:
        print "Position occupied :p"
        play(turn)
        
def toggle(turn):
    if turn=='X':
        return 'O'
    else:
        return 'X'
#display board
def display_board():
    print " %s  | %s  | %s  " %(str(board[0]),str(board[1]),str(board[2]))
    print "____|____|____"
    print " %s  | %s  | %s  " %(str(board[3]),str(board[4]),str(board[5]))
    print "____|____|____"
    print " %s  | %s  | %s  " %(str(board[6]),str(board[7]),str(board[8]))
    print "    |    |"
    
    
def main():
    win='N'
    turn='X'
    count=0
    while win=='N' and count<8:
        play(turn)
        display_board()
        turn=toggle(turn)
        win=check()
        count+=1
    if win!='N' :   
        print "Congratulations!!! Player %s wins :)" %win
    else :
        print "It's a tie!!!"
        
'''
main()
'''
        
