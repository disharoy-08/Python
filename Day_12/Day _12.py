################### Scope ####################

# enemies = 1

# def increase_enemies():
#   enemies = 2
#   print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")

# Local Scope
# def drink_potion():
#   potion_strength = 2
#   print(potion_strength)

# drink_potion()
# print(potion_strength) // will give error 

# Global Scope
# player_health = 10

# def drink_potion():
#   potion_strength = 2
#   print(player_health)

# drink_potion()

# There is no block space in python.

# Modifying Global Scope

# enemies = 1

# def increase_enemies():
#   global enemies
#   enemies += 2
#   print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")

# Modifying Global scope is a bad thing instead of that do this

enemies = 1

def increase_enemies():
  print(f"enemies inside function: {enemies}")
  return enemies + 1

enemies = increase_enemies()
print(f"enemies outside function: {enemies}")

# Global Constants

PI = 3.14  #every variable name which is written into uppercase is a constant which means You should not modify this value in anywhere (in function or anaywhere else) in your code.