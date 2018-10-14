#!/usr/bin/env python3

"""
Basic framework for developing 2048 programs in Python

Author: Hung Guei (moporgic)
        Computer Games and Intelligence (CGI) Lab, NCTU, Taiwan
        http://www.aigames.nctu.edu.tw
"""
def IndextoValue(i):
    if i>=3:
        return 3*(2**(i-3))
    else:
       return i  
class board:
    """ simple implementation of 2048 puzzle """
    
    def __init__(self, state = None):
        self.state = state[:] if state is not None else [0] * 16
        return
    
    def __getitem__(self, pos):
        return self.state[pos]
    
    def __setitem__(self, pos, tile):
        self.state[pos] = tile
        return
    
    def place(self, pos, tile):
        """
        place a tile (index value) to the specific position (1-d form index)
        return 0 if the action is valid, or -1 if not
        """
        if pos >= 16 or pos < 0:
            return -1
        if tile != 1 and tile != 2 and tile != 3:
            return -1
        self.state[pos] = tile
        return 0
    
    def slide(self, opcode):
        """
        apply an action to the board
        return the reward of the action, or -1 if the action is illegal
        """
        if opcode == 0:
            return self.slide_up()
        if opcode == 1:
            return self.slide_right()
        if opcode == 2:
            return self.slide_down()
        if opcode == 3:
            return self.slide_left()
        return -1
    '''    
    def slide_left(self):
        move, score = [], 0
        for row in [self.state[r:r + 4] for r in range(0, 16, 4)]:
            buf = sorted(row, key = lambda t: not t) + [0]
            while buf[0]:
                if buf[0] == buf[1]:
                    buf = buf[1:] + [0]
                    buf[0] += 1
                    score += 1 << buf[0]
                move += [buf[0]]
                buf = buf[1:]
            move += buf[1:]
        if move != self.state:
            self.state = move
            return score
        return -1
    
    #state=[5,2,1,0]*4
    def slide_left(self):
        move, score = [], 0
        for row in [self.state[r:r + 4] for r in range(0, 16, 4)]:
            #r=0
            #row=state[r:r + 4]
            #buf = sorted(row, key = lambda t: not t) + [0]   #sort what move o to right 
            buf=row+ [0] 
            a=1
            while buf[0]:        
                if buf[0]>=3 and buf[1]>=3: 
                    if buf[0] == buf[1] and a:  #only merge once
                        buf = buf[1:] + [0]
                        buf[0] += 1
                        a=0
                        score += 1 << buf[0]
                else:
                     if ((buf[0]==1 and buf[1]==2) or (buf[0]==2 and buf[1]==1)) and a:
                        buf = buf[1:] + [0]
                        buf[0] = 3
                        a=0
                        score += 1 << buf[0]
                move += [buf[0]]
                buf = buf[1:]
            move += buf[1:]
        if move != self.state:
             self.state = move
             return score
        return -1
    ''' 
    
    def slide_left(self):
        state=[3,3,0,2]*4
        move, score = [], 0
        for buf in [self.state[r:r + 4] for r in range(0, 16, 4)]:
            while 1:  
                if buf[0]==0:
                   buf = buf + [0]
                   move +=buf[1:]
                   break
                else:                   
                    if buf[0]>=3 and buf[1]>=3: 
                        if buf[0] == buf[1] :  #only merge once
                            move += [buf[0]+1]
                            buf = buf + [0]
                            move +=buf[2:]
                            break
                            score += 1 << buf[0]
                    else:
                         if ((buf[0]==1 and buf[1]==2) or (buf[0]==2 and buf[1]==1)):
                            move += [3]
                            buf = buf + [0]
                            move +=buf[2:]
                            break
                            score += 1 << buf[0]
                move += [buf[0]]
                buf = buf[1:]
                if len(buf)==1: 
                    move+=[buf[0]]
                    break
        if move != self.state:
             self.state = move
             return score
        return -1
 
    def slide_right(self):
        self.reflect_horizontal()
        score = self.slide_left()
        self.reflect_horizontal()
        return score
    
    def slide_up(self):
        self.transpose()
        score = self.slide_left()
        self.transpose()
        return score
    
    def slide_down(self):
        self.transpose()
        score = self.slide_right()
        self.transpose()
        return score
    
    def reflect_horizontal(self):
        self.state = [self.state[r + i] for r in range(0, 16, 4) for i in reversed(range(4))]
        return
    
    def reflect_vertical(self):
        self.state = [self.state[c + i] for c in reversed(range(0, 16, 4)) for i in range(4)]
        return
    
    def transpose(self):
        self.state = [self.state[r + i] for i in range(4) for r in range(0, 16, 4)]
        return
    
    def rotate(self, rot = 1):
        rot = ((rot % 4) + 4) % 4
        if rot == 1:
            self.rotate_right()
            return
        if rot == 2:
            self.reverse()
            return
        if rot == 3:
            self.rotate_left()
            return
        return
    
    def rotate_right(self):
        """ clockwise rotate the board """
        self.transpose()
        self.reflect_horizontal()
        return
    
    def rotate_left(self):
        """ counterclockwise rotate the board """
        self.transpose()
        self.reflect_vertical()
        return
    
    def reverse(self):
        self.reflect_horizontal()
        self.reflect_vertical()
        return
       
    def __str__(self):
        state = '+' + '-' * 24 + '+\n'
        for row in [self.state[r:r + 4] for r in range(0, 16, 4)]:
            #state += ('|' + ''.join('{0:6d}'.format((1 << t) & -2) for t in row) + '|\n')
            state += ('|' + ''.join('{0:6d}'.format(IndextoValue(t)) for t in row) + '|\n')
        state += '+' + '-' * 24 + '+'
        return state
    
    
if __name__ == '__main__':
    print('2048 Demo: board.py\n')
    
    state = board()
    state[10] = 3
    print(state)
    #format((1) & -2)

    def IndextoValue(i):
        if i>=3:
            return 3*(2**(i-3))
        else:
           return i 
       
    state2=[0,1,2,3,4,5,7,0,0,0,0,0,0,0,0,0]    
    state = '+' + '-' * 24 + '+\n'
    for row in [state2[r:r + 4] for r in range(0, 16, 4)]:
        state += ('|' + ''.join('{0:6d}'.format(IndextoValue(t)) for t in row) + '|\n')
    state += '+' + '-' * 24 + '+'    
    print(state)    

    r=0    
    row=state2[r:r + 4]    
     

   