from src.classes.Schedule import Schedule
from src.classes.Student import Student

from src.data.schedule1 import schedule1Data
from src.data.students1 import students1Data

def main():
    students = [Student(**student) for student in students1Data]
    schedule1 = Schedule(**schedule1Data, students=students)
    
    print(schedule1)
        
if __name__ == '__main__': main()   