import pandas as pd
import numpy as np
import random
from _datetime import datetime
import calendar

# Important Student Data Generation Variables
Years = {'1st': ['Mech', 'Etc', 'Civil', 'CS', 'E&TC', 'DS', 'AI'], '2nd': ['Mech', 'Etc', 'Civil', 'CS', 'E&TC', 'DS'], '3rd': ['Mech', 'Etc', 'Civil', 'CS', 'E&TC'], '4th': ['Mech', 'Etc', 'Civil', 'CS', 'E&TC']}
Branches = {'Mech': 180, 'Etc': 120, 'Civil': 60, 'CS': 180, 'DS': 60, 'AI': 60, 'E&TC': 120}
Cities = ['Pune', 'Mumbai', 'Shirpur', 'Chopda', 'Amalner', 'Parola', 'Bhadgaon', 'Pachora', 'Chalisgaon', 'Shindkheda', 'Dhule', 'Dharangaon']
Attendances = ['P', 'A', 'P', 'A', 'P', 'A', 'P', 'P', 'P', 'P']
Names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

class Data_Generator():
    def __init__(self, Years, Branches, Cities, Names):
        self.Years = Years
        self.Branches = Branches
        self.Cities = Cities
        self.Names = Names

    def Student(self):
        Student_Data = pd.DataFrame()
        ID = []
        Roll_No = []
        Name = []
        Year = []
        Branch = []
        Division = []
        UserName = []
        Password = []
        City = []
        for year in self.Years.keys():
            print(f"Creating {year} year Data...")
            for branch in self.Years[year]:
                print(f"Creating {branch} branch Data...")
                for student in range(self.Branches[branch]):
                    student += 1
                    ID.append(branch+'_'+str(student))
                    Roll_No.append(student)
                    Name.append(random.choice(self.Names)+random.choice(self.Names)+random.choice(self.Names))
                    Year.append(year)
                    Branch.append(branch)
                    if student <= 60 and student > 0:
                        Division.append('A')
                    elif student <= 120 and student > 60:
                        Division.append('B')
                    else:
                        Division.append('C')
                    UserName.append(year+'_'+branch+'_'+str(student))
                    Password.append(year+'_'+branch+'_'+str(student))
                    City.append(random.choice(self.Cities))
        Student_Data['ID'] = ID
        Student_Data['Roll_No'] = Roll_No
        Student_Data['Name'] = Name
        Student_Data['Year'] = Year
        Student_Data['Branch'] = Branch
        Student_Data['Division'] = Division
        Student_Data['UserName'] = UserName
        Student_Data['Password'] = Password
        Student_Data['City'] = City
        Student_Data.to_csv('Student.csv')

    def Attendance(self):
        # Important variables
        start_date = _datetime.date(2021, 8, 1)
        end_date = _datetime.date(2021, 12, 31)
        delta = _datetime.timedelta(days=1)
        Attendance_Data = pd.DataFrame()
        while start_date <= end_date:
            if Find_Day(start_date) == 'Sunday':
                pass
            else:
                for student in range(Student_Data['ID']):
                # start_date += delta


                
            
    @staticmethod
    def Find_Day(date):
        born = datetime.strptime(date, '%Y-%m-%d').weekday()
        return (calendar.day_name[born])
    
    @staticmethod
    def Data_Converter():
        


# Fixed Parameters


if __name__ == '__main__':

    Data = Data_Generator(Years, Branches, Cities, Names)
    Data.Student()
        