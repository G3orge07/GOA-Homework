#Kata - I love you, a little , a lot, passionately ... not at all

#https://www.codewars.com/kata/57f24e6a18e9fad8eb000296/train/python


def how_much_i_love_you(nb_petals):
    phrases = ['I love you', 'a little', 'a lot', 'passionately', 'madly', 'not at all']
    if nb_petals <= 6:
        return phrases[nb_petals-1]
    else:
        return phrases[nb_petals - 1 - 6 * int(nb_petals/6)]