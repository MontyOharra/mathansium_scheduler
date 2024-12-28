from typing import List

from .Student import Student

class Instructor:
    def __init__(self, firstName : str, lastName : str, gradeLevelsTaught : List[str], cellColor : str, timeStart : int, timeEnd : int):
        self.firstName : str = firstName
        self.lastName : str = lastName
        self.gradeLevelsTaught : List[str] = gradeLevelsTaught
        self.cellColor : str = cellColor
        self.timeStart : int = timeStart
        self.timeEnd : int = timeEnd
        
    def canTeachStudent(self, student : Student) -> bool:
        return student.gradeLevel in self.gradeLevelsTaught
    
    def isInstructorAviable(self, timeInt : int) -> bool:
        return self.timeStart <= timeInt <= self.timeEnd