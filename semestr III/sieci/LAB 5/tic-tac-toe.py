import socket  
import os
import re
import sys
import random

def is_board_filled(board):
    for x in board:
        if x == 0:
            return False
    return True

def find_move(board):
    for i in range(len(board)):
        if(board[i] == 0):
            return i             

board = [0 for x in range(25)]


s = socket.socket()
host = input()
port = int(input())

s.connect((host , port))
x = 0

while True:
    data = s.recv(1024)
 
    x += 1
    
    if (x == 1):
        print(data)
        index = input()
        s.sendto(index.encode(), (host, port))
        print(index,end='')
        response = s.recv(1024);
        print(response.decode(),end='')
        s.sendto("MOVE 0\n".encode(), (host, port))
        board[0] = 1
        continue
    else:
        print(data)
        data = data.decode().split()
        print(data)
        if (is_board_filled(board)):
            board = [0 for x in range(25)]
            board[0] = 1
            s.sendto("MOVE 0\n".encode(), (host, port))
            response = s.recv(1024);
            continue
        if(len(data) == 5):
            board = [0 for x in range(25)]
            board[0] = 1
            s.sendto("MOVE 0\n".encode(), (host, port))
            continue
        if (data[0] == "NEW" or data[0] == "WIN" or data[0] == "LOST"):
            board = [0 for x in range(25)]
            board[0] = 1
            s.sendto("MOVE 0\n".encode(), (host, port))
            continue
        if (data[0] == "OPPONENT"):
            opponent_move = data[1]
            board[int(opponent_move)] = 1
            move = find_move(board)
            if move == None:
                 msg = "MOVE " + str(random.randint(0,24)) + '\n'
                 s.sendto(msg.encode(), (host, port))
            else:
                board[move] = 1
                print(move)
                msg = "MOVE " + str(move) + '\n'
                s.sendto(msg.encode(), (host, port))
        elif (len(data) == 3):
            if(data[1] == "OPPONENT"):
                opponent_move = data[2]
                board[int(opponent_move)] = 1
                move = find_move(board)
                board[move] = 1
                print(move)
                msg = "MOVE " + str(move) + '\n'
                s.sendto(msg.encode(), (host, port))
        elif (data[0] == "ERROR"):
            msg = "MOVE " + str(random.randint(0,24)) + '\n'
            s.sendto(msg.encode(), (host, port))
            continue


print('closing')
s.close()

