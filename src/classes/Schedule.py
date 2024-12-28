from typing import List, Dict
import datetime

from .Instructor import Instructor
from .Student import Student


class Schedule:
    def __init__(self, 
        date : datetime.date,
        timeStart : int,
        timeEnd : int, 
        intervalLength : int = 30, 
        instructors : List[Instructor] = [], 
        students : List[Student] = []
    ):
        self.date : int = date
        self.instructors : List[Instructor] = instructors
        self.students : List[Student] = students
        self.timeStart : int = timeStart
        self.timeEnd : int = timeEnd
        self.intervalLength : int = intervalLength
        
        self.timeSlots : Dict[int, List[Dict[str, Instructor | Student]]] = {
            timeStepCount : []  
            for timeStepCount in range(timeStart, timeEnd, intervalLength)
        }
        self.setStudents()
        
        
        
    def __str__(self):
        return f"{self.timeSlots}"
    
    def getScheduleWeekday(self) -> str:
        return self.date.strftime("%A")
    
    def outputSpreadsheet
    
    def setStudents(self):
        for time in self.timeSlots:
            for student in self.students:
                if student.isStudentScheduled(time):
                    self.timeSlots[time].append({'student' : student})

    def assignInstructors(self):
        for time in self.timeSlots:
            
        
    
    