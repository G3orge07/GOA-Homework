# Kata - Counting Duplicates

#https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1/train/python

def duplicate_count(text):
    text = text.upper()
    
    count = []
    for i in range(len(text)):
        for n in range(i+1, len(text)):
            if text[i] == text[n] and text[i] not in count:
                count.append(text[i])
                break
                
    return len(count)