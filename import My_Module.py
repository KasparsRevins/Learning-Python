import My_Module 
# could do import my_module as greeting
# module name are case sensitive
My_Module.greeting("markson")
club_choice = int(input("Select a number for a club 0 t0 2"))
result = My_Module.select_club(club_choice)
print(result)