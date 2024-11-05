
# დაწერე ფუნქცია, რომელიც იღებს ორ სტრინგს და მოახდინეთ კონკატენაცია

def str_concat():
    text1 = input("Write the first text and I'll combine it with the second: ")
    text2 = input("The second text: ")
    combined = text1 + text2
    return combined

print(str_concat())