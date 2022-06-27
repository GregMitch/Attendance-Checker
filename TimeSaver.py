import csv
import os
import operator
rootdir = './' #Current directory

attendance_dict = {"Paid by (name)" : 0}
for file in os.listdir(rootdir):
    if file != "TimeSaver.py" and file != "README.md" and file != "ExampleFormat.csv" and file != ".git":
        with open(file, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                if line[14] in attendance_dict:
                    if line[17] != "":
                        attendance_dict[line[14]] += 1
                else:
                    attendance_dict[line[14]] = 1
    else:
        exit

sorted_dict = dict(sorted(attendance_dict.items(), key=operator.itemgetter(1), reverse=True))

for x, y in sorted_dict.items():
    print(x, y)
