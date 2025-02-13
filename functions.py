FILEPATH = "/Users/nicholas/Python_Projects/Udemy_Nov_2024/Exercises/Main_app/todos.txt"


def get_todos(filepath=FILEPATH):
    ''' Read a text file and return the todo items'''
    #filepath = "/Users/nicholas/Python_Projects/Udemy_Nov_2024/Exercises/Main_app/todos.txt"
    with open(filepath, "r", encoding="utf-8") as file_local:
        todos_local = file_local.readlines()
        return todos_local

def write_todos(todos_arg, filepath=FILEPATH):
    #filepath = "/Users/nicholas/Python_Projects/Udemy_Nov_2024/Exercises/Main_app/todos.txt"
    with open(filepath, "w", encoding="utf-8") as file:
        file.writelines(todos_arg)
        
        
if __name__ == "__main__":
    print("Todos have been written to the file.")
    print(get_todos())