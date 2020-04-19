def make_pretty(func):
    def inner():
        print("I got Decorated.")
        func()
    return inner

@make_pretty

def ordinary():
    print("I am Decorated.")

ordinary()