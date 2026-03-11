def print_todo(list_of_todo):
    print(list_of_todo)
    return
def add_todo(list_of_todo,todo):
    list_of_todo.append(todo)

    return
def del_todo(list_of_todo,todo):
    list_of_todo.append(todo)
    print_todo(list_of_todo)
    return

list_of_todo=[]


while True:
    a = input("Type add | show | edit?\n")
    a=a.strip()
    match a:
        case "add" | "Add":
            todo=input("please add a Todo")
            add_todo(list_of_todo,todo)
            print_todo(list_of_todo)
        case "show":
            print_todo(list_of_todo)
        case "edit":
            number=int(input("please enter your number\n"))
            list_of_todo[(number-1)]=input("please enter new todo\n")

        case "exit":
            break
        case _:
            print("Error")

print("Bye")



