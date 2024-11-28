# Remove First and Last Character
# It's pretty straightforward. Your goal is to create a function that removes the first and last characters of a string.

#1
def remove_char(s):
    return s[1:-1]


#2
def remove_char(s):
    s_list=[]
    new_s = ''
    
    for char in s:
        s_list.append(char)
        
    s_list.pop(0)
    s_list.pop(-1)
    
    for i in s_list:
        new_s += i
    return new_s