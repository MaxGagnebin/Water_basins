#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 08:59:33 2018

@author: Maxime Gagnebin

excercice of writing water_basins
"""
import numpy as np

class Square():
    
    def __init__(self,x,y,height):
        self.x = x
        self.y = y
        self.position = [x, y]
        self.height = height
        self.basin = None
        self.basin_size = 0
        
        
class Map():
    
    def __init__(self,size,heights):
        self.size = size
        self.squares = [Square(j,i,heights[i][j]) for i in range (self.size) for j in range(self.size)]
        
    def show_map(self):
        for i in range(self.size):
           print([(self.squares[j+self.size*i].height, self.squares[j+self.size*i].position) for j in range(self.size)])     
        
    def neighbors(self,square):
        i = square.x
        j = square.y
        neighbors = []
        if i != 0           : neighbors.append(self.squares[i-1+j*self.size])
        if i != self.size-1 : neighbors.append(self.squares[i+1+j*self.size])
        if j != 0           : neighbors.append(self.squares[i+(j-1)*self.size])
        if j != self.size-1 : neighbors.append(self.squares[i+(j+1)*self.size])
        return neighbors
    
    def lowest_neighbor(self,square):
        lowest_neighbor = square
        for neighbor in self.neighbors(square):
            if neighbor.height < lowest_neighbor.height:
                lowest_neighbor = neighbor
        return lowest_neighbor
    
    def is_sink(self,square):
        if square.height <= self.lowest_neighbor(square).height:
            return True
        else:
            return False
        
    def square_basin_assignment(self,square):
        if square.basin:
            return square.basin
        
        if self.is_sink(square):
            square.basin = square
        else:
            square.basin = self.square_basin_assignment(self.lowest_neighbor(square))
        return square.basin
    
    def basin_assignment(self):
        for square in self.squares:
            if not square.basin:
                self.square_basin_assignment(square)
    
    def show_basin_position(self):
        for i in range(self.size):
            print([self.squares[i*self.size+j].basin.position for j in range(self.size)])
            
    def basin_sizes(self):
        for square in self.squares:
            square.basin.basin_size += 1
            
    def list_basin_sizes(self):
        size_list = [square.basin_size for square in self.squares if square.basin_size != 0]
        size_list.sort()
        print(size_list)
        print(sum(size_list))
        
    
    
size = 5
heights = np.random.randint(30, size = (size,size))
print(heights)
map1 = Map(size, heights)
map1.basin_assignment()
map1.basin_sizes()
map1.list_basin_sizes()













