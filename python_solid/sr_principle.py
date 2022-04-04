

# region anti pattern

class SimpleTaskList:
    def __init__(self, initTask=[]) -> None:
        self.taskList = initTask

    def AddTask(self, task: str) -> int:
        self.taskList.append(task)

    def PrintTask(self) -> str:
        return self.taskList

    def SaveToFile(self):
        file = open("demo_sr.txt", "w")
        file.write(str(self.PrintTask()))
        file.close()


taskObject = SimpleTaskList()
taskObject.AddTask("hello1")
taskObject.AddTask("hello2")
taskObject.AddTask("hello3")
strTask = taskObject.PrintTask()
taskObject.SaveToFile()

# endregion

# region Single responsibility


class SimpleTaskListV2():
    # Just Like SimpleTaskList but this will use design pattern
    def __init__(self, initTask=[]) -> None:
        self.taskList: list(str) = initTask

    @staticmethod
    def TestMethod():
        return "Ok"


class SimpleTaskAddObj():
    def AddObj(SimpleTask: SimpleTaskListV2, task: str):
        SimpleTask.taskList.append(task)

    def AddObjWithPrefix(SimpleTask: SimpleTaskListV2, task: str, prefix: str):
        SimpleTask.taskList.append(prefix + task)


class SimpleTaskToFile():
    def SaveToFile(SimpleTask: SimpleTaskListV2, fileName: str):
        file = open(fileName, "w")
        file.write(str(SimpleTask.taskList))
        file.close()


taskObjectV2 = SimpleTaskListV2()
SimpleTaskAddObj.AddObj(taskObjectV2, "Hello1")
SimpleTaskAddObj.AddObj(taskObjectV2, "Hello2")
SimpleTaskAddObj.AddObj(taskObjectV2, "Hello3")
SimpleTaskAddObj.AddObjWithPrefix(taskObjectV2, "Hello3", "Ok_")

check = taskObjectV2.TestMethod()

SimpleTaskToFile.SaveToFile(taskObjectV2, "demo_sr2.txt")

# endregion
exit(0)
