
# Kata - Take a Ten Minutes Walk

#https://www.codewars.com/kata/54da539698b8a2ad76000228/train/python

def is_valid_walk(walk):
    if len(walk) == 10:
        
        start = [ 0, 0 ]
        finish = [ 0, 0 ]
        
        for dir in walk:
            if dir == 'n':
                finish[1] += 1
            elif dir == 's':
                finish[1] -= 1
            elif dir == 'w':
                finish[0] -= 1
            elif dir == 'e':
                finish[0] += 1
            
        return finish == start
        
    else:
        return False