#!/usr/bin/env python3
# Author ID: [seneca_id]

def add(number1, number2):
    try:
        
        return float(number1) + float(number2)
    except (ValueError, TypeError):
        
        return 'error: could not add numbers'

def read_file(filename):
    try:
        f = open(filename, 'r')
        return f.readlines()  
    except IOError:
        
        return 'error: could not read file'

if __name__ == '__main__':
    print(add(10, 5))                        # Works, should return 15
    print(add('10', 5))                      # Works, should return 15
    print(add('abc', 5))                     # Error case, should return 'error: could not add numbers'
    print(read_file('seneca2.txt'))         # Works if the file exists, should return list of lines
    print(read_file('file10000.txt'))       # Error case, should return 'error: could not read file'
