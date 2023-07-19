from functions import get_todos,write_todos
import time

now = time.strftime("%b %d, %y %H:%M:%S")
print("It is ",now)
while True:
    user_action = input("Type add , exit , edit , complete & show")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo + '\n')
        write_todos(todos)

    elif user_action.startswith('show'):
        todos = get_todos()
        new_todos = []

        for index,item in enumerate(todos):
            item=item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)
    elif user_action.startswith('exit'):
        break
    elif user_action.startswith('edit'):
        number = int(user_action[5:])
        number = number - 1

        todos = get_todos()

        new_todo = input("Enter a new Todo:")
        todos[number] = new_todo + '\n'

        write_todos(todos)

    elif user_action.startswith(''):
        number = int(user_action[9:])

        todos = get_todos()
        index = number - 1
        todo_removed = todos[index]
        todos.pop(index)

        write_todos(todos)

        message = f"Todo { todo_removed} was removed from the list."
        print(message)

    else:
        print('command is not valid.')

print("Bye!!!")

