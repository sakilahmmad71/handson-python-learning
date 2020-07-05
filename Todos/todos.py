todos = []


def makeTodo(text):
    id = len(todos) + 1
    title = text
    completed = False

    todo = {"id": id, "title": title, "completed": completed}
    todos.append(todo)


def updateTodoTitle(text, updatedText):
    for todo in todos:
        if todo["title"] == text:
            todo["title"] = updatedText


def completeTodo(text):
    for todo in todos:
        if todo["title"] == text:
            todo["completed"] = True


def showCompletedTodo():
    filteredTodos = list(filter(lambda todo: todo["completed"] == True, todos))

    for todo in filteredTodos:
        print(todo["title"] + " - completed")


def showIncompletedTodo():
    filteredTodos = list(
        filter(lambda todo: todo["completed"] == False, todos))

    for todo in filteredTodos:
        print(todo["title"] + " - not completed")


def showAllTodos():
    for todo in todos:
        print(todo)


def deleteTodo(text):
    for todo in todos:
        if todo["title"] == text:
            index = todos.index(todo)
            todos.pop(index)


def searchTodo(text):
    for todo in todos:
        if todo["title"] == text:
            return print(todo)


# Making some todos
makeTodo("Program python for an hour")
makeTodo("Walk at leat 1 hour in a day")
makeTodo("Do lunch at time")
makeTodo("Make coffee before sitting for coding")
makeTodo("Design User Interface for project")

# Updating an todo title
updateTodoTitle("Do lunch at time", "Do dinner at time")

# Complete some todos
completeTodo("Walk at leat 1 hour in a day")
completeTodo("Design User Interface for project")

# Showing Imcomplete todos
showIncompletedTodo()

# Show completed todos
showCompletedTodo()

# Search for a specific todo
searchTodo("Make coffee before sitting for coding")

# Delete a todo from todo list
deleteTodo("Program python for an hour")

# Show all todos
showAllTodos()
