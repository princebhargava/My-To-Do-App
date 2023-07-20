import functions
import PySimpleGUI as sg

label = sg.Text("Type in a To-Do:")
input_box = sg.InputText(tooltip="Enter todo",key="Todo")
add_button = sg.Button("ADD")

window = sg.Window('My To-Do App',
                   [[label],[input_box,add_button]],
                   font=("Helvetica",25))
while True:
    event,values = window.read()
    print(event)
    print(values)
    match  event:
        case "ADD":
            todos = functions.get_todos()
            new_todo = values["Todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WINDOW_CLOSED:
            break
window.close()