# Part. 1
#=======================================
# Import module
#  csv -- fileIO operation
import csv
#=======================================

# Part. 2
#=======================================
# Read cwb weather data
cwb_filename = '106061123.csv'
data = []
header = []
with open(cwb_filename) as csvfile:
    mycsv = csv.DictReader(csvfile)
    header = mycsv.fieldnames
    for row in mycsv:
        data.append(row)
#=======================================

# Part. 3
#=======================================
# Analyze data depend on your group and store it to target_data like:
# Retrive all data points which station id is "C0X260" as a list.
# target_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))

i = -1
for row in data:
    i += 1
    if row["WDSD"] == "-99.000" or row["WDSD"] == "-999.000":
        row["WDSD"] = 0
    
header = ["C0A880", "C0F9A0", "C0G640", "C0R190", "C0X260"]

my_list = [[] for i in range(5)]
for row in data:
    if row["station_id"] == header[0]:
        my_list[0].append(float(row["WDSD"]))
    if row["station_id"] == header[1]:
        my_list[1].append(float(row["WDSD"]))
    if row["station_id"] == header[2]:
        my_list[2].append(float(row["WDSD"]))
    if row["station_id"] == header[3]:
        my_list[3].append(float(row["WDSD"]))
    if row["station_id"] == header[4]:
        my_list[4].append(float(row["WDSD"]))

data.clear()
data = [[]for i in range(5)]
        
for i in range(5):
    my_list[i].sort()
    my_list[i] = my_list[i][len(my_list[i]) - 1] - my_list[i][0]
    data[i].append(header[i])
    if my_list[i] == 0:
        data[i].append('None')
    else :
        data[i].append(my_list[i])
    

# Retrive ten data points from the beginning.
target_data = data[:5]

#=======================================

# Part. 4
#=======================================
# Print result
print(target_data)
#========================================