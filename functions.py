# FILEPATH = "/Users/nicholas/Python_Projects/Udemy_Nov_2024/Exercises/Main_app/todos.txt"
#FILEPATH = "/Users/nicholas/Test Workspace/Todo_Web_App/todos.txt"



def get_todos():
    ''' Read a text file and return the todo items'''
    #todos.txt" = "/Users/nicholas/Python_Projects/Udemy_Nov_2024/Exercises/Main_app/todos.txt"
    with open("todos.txt", "r", encoding="utf-8") as file_local:
        todos_local = file_local.readlines()
        return todos_local

def write_todos(todos_arg):
    #todos.txt" = "/Users/nicholas/Python_Projects/Udemy_Nov_2024/Exercises/Main_app/todos.txt"
    with open("todos.txt", "w", encoding="utf-8") as file:
        file.writelines(todos_arg)
        
        
if __name__ == "__main__":
    print("Todos have been written to the file.")
    print(get_todos())