# Hello World program in Python
    
import csv as csv
import numpy as np
csv_file_object = csv.reader(open('train.csv','rb'))
header = csv_file_object.next()
data = []
for row in csv_file_object:
     data.append(row)
data = np.array(data)
print data
print data[0]
print data[-1]
print data[0,3]
print data[0::,4]
data[0::,2].astype(np.float)
number_passengers = np.size(data[0::,1].astype(np.float))
number_survived = np.sum(data[0::,1].astype(np.float))
proportion_survivors = number_survived / number_passengers
print number_passengers
print number_survived
print proportion_survivors
women_only_stats = data[0::,4] == "female"
men_only_stats = data[0::,4] != "female" 
women_onboard = data[women_only_stats,1].astype(np.float)     
men_onboard = data[men_only_stats,1].astype(np.float)
print women_only_stats
print women_onboard
print np.size(women_only_stats,0)
print np.size(women_onboard,0)
proportion_women_survived = np.sum(women_onboard) / np.size(women_onboard)
proportion_men_survived = np.sum(men_onboard) / np.size(men_onboard)
print proportion_women_survived
print proportion_men_survived
test_file = open('test.csv', 'rb')
test_file_object = csv.reader(test_file)
header = test_file_object.next()
