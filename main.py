# from functions import get_todos, write_todos
import time

from modules import functions

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    # match user_action:
    #if "add" in user_action or "new" in user_action:
    if user_action.startswith("add"):


        todo = user_action[4:].strip() + "\n"



        # file = open("todos.txt", "r")
        # todos = file.readlines()
        # file.close()

        todos = functions.get_todos()

        todos.append(todo)

        # file = open("todos.txt", "w")
        # file.writelines(todos)
        # file.close()

        functions.write_todos(filepath="todos.txt", todos_arg=todos)

    # case "show" | "display":
        # file = open("todos.txt", "r")
        # todos = file.readlines()
        # file.close()
    #elif "show" in user_action:
    if user_action.startswith("show"):

        todos = functions.get_todos()




        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1} - {item}"
            print(row)

    # case "edit":
    #elif "edit" in user_action:
    if user_action.startswith("edit"):
        try:

            #number = int(input("Number of todo to edit: "))

            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos()
            print("Here is todos existing", todos)

            new_todo = input("Enter your new todo: ")
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)

        except ValueError:
            print("Your command is not valid.")
            continue



    # case "complete":
    #elif "complete" in user_action:
    if user_action.startswith("complete"):
        try:
            #number = int(input("Number of todo to complete: "))

            number = int(user_action[9:])

            todos = functions.get_todos()

            indexik = number - 1
            todo_to_remove = todos[indexik].strip('\n')
            todos.pop(indexik)

            functions.write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)
        except IndexError:
            print("There is no number with that number.")
            continue

    # case "exit":
    #elif "exit" in user_action:
    if user_action.startswith("exit"):


        break

    else:
        print("Command is not valid.")


print("Bie")
