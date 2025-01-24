from time import ctime


class toDoList:
    
    def __init__(self):
        try:
            with open("ToDoList.txt","r") as info:
                self.information = {}
                for line in info:
                    if ":" in line:
                        key,value = line.strip().split(":",1)
                        self.information[key.strip()] = value.strip()
        except FileNotFoundError:
            self.information = {}

    def addTasks(self,taskName,taskDescription,dateCreated,dateCompleted = "Incomplete",status = "Pending"):

        data = {}
        data[taskName] = {"Description":taskDescription,"Date created":dateCreated,"Date completed":dateCompleted,"Status":status}

        if "Incomplete Tasks" not in self.information.keys():
            self.information["Incomplete Tasks"]=data
        else:
            if taskName not in self.information["Incomplete Tasks"]:
                self.information["Incomplete Tasks"].update(data)
            else:
                return("Data already exists")

    def deleteTask(self,taskName,status):
        Task = self.information[status]

        for name in Task:
            if name == taskName:
                del Task[taskName]
                return
    def completeTask(self,taskName):
        Tasks = self.information["Incomplete Tasks"]
        completedTask = None
        if taskName in self.information["Incomplete Tasks"]:
            for name in Tasks:
                if name == taskName:
                    Tasks[taskName]["Date completed"] = ctime()
                    Tasks[taskName]["Status"] = "Complete"
                    completedTask = Tasks.pop(taskName)
                    break
            if "Completed Tasks" not in self.information.keys():
                self.information["Completed Tasks"]=completedTask
            else:
                if taskName not in self.information["Completed Tasks"]:
                    self.information["Completed Tasks"].update(completedTask)
                else:
                    self.deleteTask(taskName,"Completed Tasks")
                    self.information["Completed Tasks"].update(completedTask)

    def viewTasks(self)->str:
        data = ""
        for tasks in self.information:

            data +=tasks +"\n:"+ str(self.information[tasks])+"\n"
        return(data)

    def saveData(self):
        with open("ToDoList.txt","w") as info:
            info.write(str(self.information))

if __name__ == "__main__":

    list = toDoList()

    while True:
        print("Select one of the following options:")
        print("____________________________________")
        print("1. Add a task")
        print("2. Delete a task")
        print("3. Complete a task")
        print("4. View all tasks")
        print("5. Exit")

        choice = int(input("Enter your option: "))

        match choice:
            case 1:
                taskName = input("What is the name of the task: ")
                taskDescription = input("Describe the task: ")
                dateCreated = ctime()

                list.addTasks(taskName,taskDescription,dateCreated)
            case 2:
                task = input("What is the name of the task: ")
                list.deleteTask(task,"Incomplete Tasks")
            case 3:
                task = input("What is the name of the task you have completed?")
                list.completeTask(task)

            case 4:
                print(list.viewTasks())
            case 5:
                list.saveData()
                print("goodbye")
                break
            case _:
                print("invalid option")

