# Simple Functon


# Review:
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.
def greet():
    print("Hey Dude")
    print("Don't go this path again, it's very painful.")
    print(
        "Don't be hurry up. Remember the previus case and control your mind.")


#greet()

#Function that allows for input
#n = input("Enter Your name: ")


def greet_with_name(name):
    print(f"Hey {name}")
    print(f"{name} Don't go this path again, it's very painful.")
    print(
        "Don't be hurry up. Remember the previus case and control your mind.")


#greet_with_name(n)


#Function with more than 1 input
#n = input("Enter your name: ")
#dob = input("Enter your DOB: ")
def greet_with(name, time):
    print(f"Hey {name}, my strong girl")
    print(
        f"Don't focus on these distracting things, insted of that complete your target within {time}, your birthday and give your self a beautiful gift."
    )


#greet_with(n, dob)
greet_with("Dev", "2nd December")

#Function with keyword arguments
greet_with(time="27th August", name="Disha")
