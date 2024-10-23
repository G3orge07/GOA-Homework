
#შექმენი ფუნქცია, რომელიც შემოატანინებს მომხარებელს ტექსტს და დააბრუნებს ტექსტის სიგრძეს.

def text_length_counter():
    text = input("Type any kind of text here and I will tell you the length of it: ")
    characters = len(text)
    print(f"There are {characters} characters in your text! Including spaces.")

text_length_counter()

