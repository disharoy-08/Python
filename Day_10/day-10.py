#Function with outputs
# def format_name(f_name, l_name):
#   f_name = f_name.capitalize()
#   l_name = l_name.capitalize()
#   return f_name, l_name

def format_name(f_name, l_name):
  if f_name == "" or l_name == "":
    return "You didn't provide valid inputs."
  full_name = f_name +" " + l_name
  full_name = full_name.title()
  #return full_name
  return f"Updated name format is: \n{full_name}"
  
name = format_name(input("What is your first name? "), input("What is your last name? "))
print(name)