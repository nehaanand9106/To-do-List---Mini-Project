#main file with menu
import Tasksfunc
print("To-Do-List Manager")
status=True
while status:
  print('''1,View Task
           2,Add Tasks
           3,Mark Task As Done
           4,Delete Task
           5,Exit''')
  choice=input("Choose the Task to Perform:").strip()
  match choice:
    case "1":
      Tasksfunc.view()
    case "2":
       Tasksfunc.add()
    case "3":
       Tasksfunc.mark()
    case "4":
       Tasksfunc.delete()
    case "5":
      status=False
      print("Exiting... Good Bye!!!")
    case _:
      print("Invalid Option")
  
