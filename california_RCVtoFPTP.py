import csv

city = input("Please enter the city you are interested in seeing the results of:\n")
with open(f'{city}.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    row_list = []

    for row in csv_reader:
      if row[2] == 'RCV':
        row_list.append([row[0], row[1], row[3], row[4], row[5], row[6], row[9]])

print(len(row_list))
winner = {}

for i in range(len(row_list) - 1):
  highest = 0.0
  for j in range(len(row_list) - 1):
    if row_list[j][0] == row_list[i][0] and row_list[j][1] == row_list[i][1] and float(row_list[j][6]) >= highest:
      highest = float(row_list[j][6])
      winner[row_list[j][0] + row_list[j][1]] = [row_list[j][3], row_list[j][6], row_list[j][4], row_list[j][5]]

fptplist = []
for key in winner:
  fptplist.append([key, winner[key][0], winner[key][1], winner[key][2], winner[key][3]])

with open(f'{city}_RCV_to_FPTP.csv', 'w', newline='') as file:
  writer = csv.writer(file, delimiter=',')
  writer.writerows(fptplist)
