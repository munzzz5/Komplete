# from controller import intentExtractor


class Task:
    currTaskId = 0
    taskProfileList = ["Personal", "Professional"]
    taskTypeList = ["Do", "Work", "Transact", "Learn", "Communicate"]

    def __init__(self, taskTitle, usersInvolved, taskType, taskProfile):
        self.taskId = Task.createTaskId()
        self.startTime = None  # startTime of the task
        self.endTime = None  # end time of task
        self.taskProfile = taskProfile  # Is this a personal or professional task profile
        # chosen from a pre defined set of verbs which describes the action of this task
        self.taskType = taskType
        self.actionsList = None  # list of functions to execute according to tasks
        self.dependentTasks = None  # tasks that this task depends on before completion
        self.subTaskList = None  # subTasks of this task
        self.taskTitle = taskTitle  # String containing users input of task
        self.usersInvolved = usersInvolved  # usersInvolved in this task

    def createTaskId():
        sendingTaskId = Task.currTaskId
        Task.currTaskId += 1
        return sendingTaskId

    def addSubtasks(self, subtask):
        if(isinstance(subtask, list)):
            self.subTaskList.append(currSubtask for currSubtask in subtask)
        else:
            self.subTaskList.append(subtask)
        pass

    def addUsers(self):
        pass

    def addDependentTasks(self):
        pass

    def setStartTime(self):
        pass

    def setEndTime(self):
        pass

    def addActionToPerform(self, actions):
        if(isinstance(actions, list)):
            self.actionsList.append(currAction for currAction in actions)
        else:
            self.actionsList.append(actions)

    def changeTaskTitle(self, newTitle):
        self.taskTitle = newTitle
