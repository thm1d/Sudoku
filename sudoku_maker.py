# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 09:29:11 2021

@author: tahmi
"""


base  = 3
side  = base*base

# pattern for a baseline valid solution
def pattern(r,c): return (base*(r%base)+r//base+c)%side

# randomize rows, columns and numbers (of valid base pattern)
from random import sample
def shuffle(s): return sample(s,len(s)) 
rBase = range(base) 
rows  = [ g*base + r for g in shuffle(rBase) for r in shuffle(rBase) ] 
cols  = [ g*base + c for g in shuffle(rBase) for c in shuffle(rBase) ]
nums  = shuffle(range(1,base*base+1))

# produce board using randomized baseline pattern
board_original = [ [nums[pattern(r,c)] for c in cols] for r in rows ]
#print(board_original)

board_temp = board_original

#for line in board_original: print(line)

squares = side*side
empties = squares * 4//6
for p in sample(range(squares),empties):
    board_temp[p//side][p%side] = 0

board = board_temp

#print_board(board)
