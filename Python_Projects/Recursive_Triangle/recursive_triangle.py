def recursive_triangle(num):
    if num > 0:
        recursive_triangle(num-1,)
        print(num*'*')
    
recursive_triangle(4)    
