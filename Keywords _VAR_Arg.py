def show_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
        
show_details(name="Jazir", age=25, city="New York")

def display(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

display(10, 20, name="John", age=30)