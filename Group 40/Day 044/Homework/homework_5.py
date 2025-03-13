# Convert number to reversed array of digits

def digitize(n):
    digits = []
    for digit in str(n):
        digits.append(int(digit))
    
    digits_rvrs = []
    for i in range(-1, -(len(digits)+1), -1):
        digits_rvrs.append(digits[i])
        
    return digits_rvrs