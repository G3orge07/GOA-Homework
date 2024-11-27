
# Kata - Hello, Name or World!

def hello(name=None):
    if not name:
        return 'Hello, World!'
    else:
        return 'Hello, ' + name.capitalize() + '!'