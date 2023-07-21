import functions
import PySimpleGUI as sg

label = sg.Text("Type in a To-Do:")
input_box = sg.InputText(tooltip="Enter todo",key="Todo")
add_button = sg.Button("ADD")
listbox = sg.Listbox(values=functions.get_todos(),key="todos",
                     enable_events=True, size=[45,10])
edit_button = sg.Button("Edit")
window = sg.Window('My To-Do App',
                   [[label],[input_box,add_button],[listbox,edit_button]],
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
            window['todos'].update(values=todos)
        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values["Todo"]

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "todos":
            window['Todo'].update(value=values['todos'][0])
        case sg.WINDOW_CLOSED:
            break
window.close()