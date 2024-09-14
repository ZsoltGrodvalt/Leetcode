import pandas as pd

def combine_two_tables(person, address):
    combined = person.merge(address, on='personId', how='left')
    return combined[['firstName','lastName','city','state']]#.fillna('null')




person = pd.DataFrame({'personId':[1,2],'firstName':['Allen','Bob'],'lastName':['Wang','Alice']})
# print(person)

address = pd.DataFrame({'addressId':[1,2],'personId':[2,3], 'city':['New York City','Leetcode'], 'state':['New York','California']})
# print(address)

print(combine_two_tables(person, address))