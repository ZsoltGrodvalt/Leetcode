import pandas as pd

employee = pd.DataFrame({   'id':[1,2,3,4],
                            'name':['Joe','Henry','Sam','Max'],
                            'salary':[70000,80000,60000,90000],
                            'managerId':[3,4,'NaN','NaN']})

employee = pd.DataFrame({   'id':[1,2,3,4,5,6,7,8,9],
                            'salary':[100,200,300,100,500,600,400,200,800]})


users = pd.DataFrame({  'user_id':[1,2,3,4,5,6,7],
                        'name':['Winston','Jonathan','Annabelle','Sally','Marwan','David','Shapiro'],
                        'mail':['winston@leetcode.com','jonathanisgreat','bella-@leetcode.com',
                                'sally.come@leetcode.com','quarz#2020@leetcode.com','david69@gmail.com','.shapo@leetcode.com']})



person = pd.DataFrame({ 'personId':[1,2],
                        'firstName':['Allen','Bob'],
                        'lastName':['Wang','Alice']})

address = pd.DataFrame({'addressId':[1,2],
                        'personId':[2,3], 
                        'city':['New York City','Leetcode'], 
                        'state':['New York','California']})


employee = pd.DataFrame({   'id':[1,2,3,4,5],
                            'name':['Joe','Jim','Henry','Sam','Max'],
                            'salary':[70000,90000,80000,60000,90000],
                            'departmentId':[1,1,2,2,1]})
department = pd.DataFrame({   'id':[1,2],
                            'name':['IT','Sales']})

scores = pd.DataFrame({ 'id':[1,2,3,4,5,6],
                        'score':[3.50,3.65,4.00,3.85,4.00,3.65]})

activity = pd.DataFrame({   'player_id':[1,1,2,3,3],
                            'device_id':[2,2,3,1,4],
                            'event_date':['2016-03-01','2016-05-02','2017-06-25','2016-03-02','2018-07-03'],
                            'games_played':[5,6,1,0,5]})

teacher = pd.DataFrame({ 'teacher_id':[1,1,1,2,2,2,2],
                        'subject_id':[2,2,3,1,2,3,4],
                        'dept_id':[3,4,3,1,1,1,1]})


courses = pd.DataFrame({ 'student':['A','B','C','D','E','F','G','H','I'],
                        'class':['Math','English','Math','Biology','Math','Computer','Math','Math','Math']})

daily_sales = pd.DataFrame({   'date_id':['2020-12-8','2020-12-8','2020-12-8','2020-12-7','2020-12-7','2020-12-8',
                                          '2020-12-8','2020-12-7','2020-12-7','2020-12-7'],
                            'make_name':['toyota','toyota','toyota','toyota','toyota','honda',
                                          'honda','honda','honda','honda'],
                            'lead_id':[0,1,1,0,0,1,2,0,1,2],
                            'partner_id':[1,0,2,2,1,2,1,1,2,1]})
