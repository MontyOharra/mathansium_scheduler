class Student:
    def __init__(self, firstName : str, lastName : str, gradeLevel : str, isHomeworkHelp : bool, startTime : int, endTime : int):
        self.isHomeworkHelp : bool = isHomeworkHelp
        self.startTime : int = startTime
        self.endTime : int = endTime
        self.firstName : str = firstName,
        self.lastName : str = lastName,
        self.gradeLevel : str = gradeLevel
        self.scheduleColumn : int = 0
        self.scheduleRow : int = 0
        
    def isStudentScheduled(self, timeInt : int) -> bool:
        return self.startTime <= timeInt < self.endTime
    