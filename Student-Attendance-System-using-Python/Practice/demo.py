import pandas as pd
import numpy as np
import random
import _datetime


# Years = {'1st': ['Mech', 'Etc', 'Civil', 'CS', 'E&TC', 'DS', 'AI'], '2nd': ['Mech', 'Etc', 'Civil', 'CS', 'E&TC', 'DS'], '3rd': ['Mech', 'Etc', 'Civil', 'CS', 'E&TC'], '4th': ['Mech', 'Etc', 'Civil', 'CS', 'E&TC']}
# Branches = {'Mech': 180, 'Etc': 120, 'Civil': 60, 'CS': 180, 'DS': 60, 'AI': 60, 'E&TC': 120}
# Student_Columns = ['ID', 'Roll_No', 'Name', 'Year', 'Branch', 'Division', 'UserName', 'Password', 'City']
# Cities = ['Pune', 'Mumbai', 'Shirpur', 'Chopda', 'Amalner', 'Parola', 'Bhadgaon', 'Pachora', 'Chalisgaon', 'Shindkheda', 'Dhule', 'Dharangaon']
Attendances = ['P', 'A', 'P', 'A', 'P', 'A', 'P', 'P', 'P', 'P']
# Names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


Data = pd.DataFrame()

# ID = []
# Roll_No = []
# Name = []
# Year = []
# Branch = []
# Division = []
# UserName = []
# Password = []
# City = []
Attendance = []

# for year in Years.keys():
#     print(f"Creating {year} year Data...")
#     for branch in Years[year]:
#         print(f"Creating {branch} branch Data...")
#         for student in range(Branches[branch]):
#             student += 1
#             ID.append(branch+'_'+str(student))
#             Roll_No.append(student)
#             Name.append(random.choice(Names)+random.choice(Names)+random.choice(Names))
#             Year.append(year)
#             Branch.append(branch)
#             if student <= 60 and student > 0:
#                 Division.append('A')
#             elif student <= 120 and student > 60:
#                 Division.append('B')
#             else:
#                 Division.append('C')
#             UserName.append(year+'_'+branch+'_'+str(student))
#             Password.append(year+'_'+branch+'_'+str(student))
#             City.append(random.choice(Cities))
#             Attendance.append(random.choice(Attendances))

# Important variables
start_date = _datetime.date(2020, 1, 1)
end_date = _datetime.date(2020, 1, 4)
delta = _datetime.timedelta(days=1)


while start_date <= end_date:
    print(start_date)
    start_date += delta