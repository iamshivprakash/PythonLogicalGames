# Simple Function
# def greet():
#     print("hello")
#     print("how do you do?")
#     print("Isn't it too hot today?")
# greet()

# Function that allows Input
# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"how do you do {name}?")
# greet_with_name("Shiv")

# Function with more than one Input
def greet_with(name,location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")
# greet_with("Shiv","Samastipur")
# greet_with("Samastipur",'Shiv')
greet_with(name="Shiv",location="Samastipur")



# Functions with outputs

def format_name(f_name,l_name):
    """Docs String: Write a brief description about the function"""
    if f_name=="" or l_name=="":
        return "You didn't provide valid inputs."
    formatted_f_name=(f_name.title())
    formatted_l_name=(l_name.title())
    return f"{formatted_f_name} {formatted_l_name}"

print(format_name(input("What is your First Name?"),input("What is your last name?")))