def recursive_triangle(num, char):
    if num > 0:
        recursive_triangle(num-1, char)
        print(char*num)
    
recursive_triangle(4,'*')    