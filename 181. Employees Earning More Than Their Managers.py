# merging from 2 SIDES
import pandas as pd

def find_employees(employee):
    emp = employee.merge(employee, left_on='managerId', right_on='id', suffixes=('_emp','_man'))
    good_earners = emp[emp['salary_emp'] > emp['salary_man']]
    # renaming the columns 
    good_earners.rename(columns={'name_emp':'Employee'}, inplace=True)
    return good_earners[['Employee']]






employee = pd.DataFrame({'id':[1,2,3,4],'name':['Joe','Henry','San','Max'],'salary':[70000,80000,60000,90000],'managerId':[3,4,'NaN','NaN']})
# print(employee)

print(find_employees(employee))