'''import pandas as pd

delete_file = pd.read_csv('delete_later.csv')
data_file = pd.read_csv('Output_files/nature.csv')

#print(data_file['Place Name'].tolist())
#delete_list = delete_file['Place Name'].tolist()

mergedStuff = pd.merge(delete_file, data_file,  on=["Place Name"])["Place Name"]

print(mergedStuff)
#pan = pd.DataFrame([delete_list, data_list])
#pan.to_csv('Output_files/delete_later.csv')



'''

categories = ['Melbourne City Council', 'North Melbourne', 'Clubs']

tags = categories[2:3]

print(tags)
print(categories)


