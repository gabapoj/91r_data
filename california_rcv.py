import csv

city = input("Please enter the city you are interested in seeing the results of:\n")
with open(f'{city}.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    row_list = []

    for row in csv_reader:
      if row[2] == 'RCV' and row[8] == 'Y':
        row_list.append([row[1] + ' ' + row[0], row[4], row[5], row[6]])

with open(f'{city}_RCV.csv', 'w', newline='') as file:
  writer = csv.writer(file, delimiter=',')
  writer.writerows(row_list)

