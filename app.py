def print_todo(list_of_todo):
    print(list_of_todo)
    return
def add_todo(list_of_todo,todo):
    list_of_todo.append(todo)
    print(list_of_todo)
    print_todo(list_of_todo)
    return
def del_todo(list_of_todo,todo):
    list_of_todo.append(todo)
    print_todo(list_of_todo)
    return

list_of_todo=[]


while True:
    a = input("Type add or show?\n")
    match a:
        case "add":
            todo=input("please add a Todo")
            add_todo(list_of_todo,todo)
            print(list_of_todo)
        case "show":
            print_todo(list_of_todo)
        case "exit":
            break





