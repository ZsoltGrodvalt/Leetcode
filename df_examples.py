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
