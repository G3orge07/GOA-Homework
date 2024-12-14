#Kata - Cat years, Dog years
#https://www.codewars.com/kata/5a6663e9fd56cb5ab800008b/train/python

def human_years_cat_years_dog_years(human_years):
    if human_years == 1:
        return [1,15,15]
        
    elif human_years ==2:
        return [2, 24,24]
        
    elif human_years ==3:
        return [3, 28, 29]
        
    else:
        return [human_years, 
                
                28 + 4 * len(range(4, human_years+1)), 
                
                29 + 5 * len(range(4, human_years+1))]
    
print(range(3, 20))
