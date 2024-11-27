
#დაწერე ფუნქცია, რომელიც input()-ით იღებს ტემპერატურას ცელსიუსში და ბეჭდავს ფარენჰეიტში გადაყვანილ მნიშვნელობას.

def c_into_f():
    print("This is a celsius-into-fahrenheit converter.")
    C = int(input("Enter how many degrees celsius you'd like to convert into fahreinheit: "))
    
    #Celsius into fahrenheit formula --  °F = (9/5)°C+32.
    F = ((9/5) * C) + 32
    print(f"{C} degrees celsius is {F} degrees fahrenheit.")

c_into_f()

