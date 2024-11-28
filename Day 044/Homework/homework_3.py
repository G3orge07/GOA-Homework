
#Kata - Century From Year
#Given a year, return the century it is in.


def century(year):
    if 0 < year <= 100:
        return 1
    

    elif len(str(year)) == 3:
        if year % 100 == 0:
            return int(str(year)[0:1])
        
        else:
            return int(str(year)[0:1]) +1

    elif len(str(year)) ==4:
        if year % 100 == 0:
            return int(str(year)[0:2])
        
        else:
            return int(str(year)[0:2]) + 1