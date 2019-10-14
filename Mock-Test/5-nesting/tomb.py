dead_end = 0
mummies = 0 
print("Escaping the tomb...")
print()
print("What lies before me?")
user_response = input()
if user_response == str("dead end"):
    dead_end = +1
    print("Time to turn back.")
elif user_response == str("mummy"):
    mummies = +1
    print("Better find another way.")
else:
    print("Let's move around it." )
print("Encountered " ,dead_end, "dead ends and" ,mummies, "mummies.")