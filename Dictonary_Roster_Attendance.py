quit = 0
Num_Of_Students = int(input("How many students do you have in your class? "))
Roster = {}
for count in range(Num_Of_Students):
    student_name = str.lower(input("Enter the student's name \n"))
    Roster [student_name] = "Present"
def List():
    for k,v in Roster.items():
        print(k,v)

action = str.lower(input("What would you like to do \n Change - change attendance of a student \n remove - remove a student \n add- add a student \n print - print students with their attendance \n quit - quit the interface "))

while quit != 1:
    if action == "change":
        name = str.lower(input("Enter the student's name you wish to change " ))
        if name in Roster:
            attendance = str.lower(input("Enter their status (ex. absent, tardy, illness, hospitlized) " ))
            Roster[name] = attendance
        else:
            print("Student not found")
        action = str.lower(input("What would you like to do \n Change - change attendance of a student \n remove - remove a student \n add- add a student \n print - print students with their attendance \n quit - quit the interface ") )

    elif action == "remove":
        remove = str.lower(input("Who would you like to remove from your roster? " ))
        confirm = str.upper(input("Type delete to remove"))
        if confirm == "DELETE":
            del Roster[remove]
            print(Roster)
        else:
            print("Canceled")
        action = str.lower(input("What would you like to do \n Change - change attendance of a student \n remove - remove a student \n add- add a student \n print - print students with their attendance \n quit - quit the interface " ))


        del Roster
    elif action == "add":
        student_name = str.lower(input("Enter the student's name " ))
        Roster [student_name] = "Present"
        action = str.lower(input("What would you like to do \n Change - change attendance of a student \n remove - remove a student \n add- add a student \n print - print students with their attendance \n quit - quit the interface " ))

    elif action == "print":
        for k,v in Roster.items():
            print(k,v)
            print()
        action = str.lower(input("What would you like to do \n Change - change attendance of a student \n remove - remove a student \n add- add a student \n print - print students with their attendance \n quit - quit the interface "))

    elif action == "quit":
        quit = 1
print("Have a good day!")
exit

