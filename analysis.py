import csv
import numpy as np
import matplotlib.pyplot as plt

city = input("Please enter the city you are interested in seeing the results of:\n")
with open(f'{city}.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    # Initalizing variables
    line_count = 0
    race_RCV = []
    gender_RCV = []
    years_RCV = []
    numLatinosRCV = 0
    numMiddleEasternRCV = 0
    numAsiansRCV = 0
    numAfricanAmericansRCV = 0
    numNativeAmericansRCV = 0

    years_Else = []
    gender_Else = []
    race_Else = []
    numLatinosElse = 0
    numAsiansElse = 0
    numAfricanAmericansElse = 0
    numMiddleEasternElse = 0
    numNativeAmericansElse = 0


    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
          if row[2] == 'RCV':
            years_RCV.append(row[0])
            gender_RCV.append(row[5])
            race_RCV.append(row[6])
          else:
            years_Else.append(row[0])
            gender_Else.append(row[5])
            race_Else.append(row[6])

          line_count += 1

    firstRCV = int(years_RCV[0])
    recentRCV = int(years_RCV[0])
    for i in range(len(years_RCV)):
      years_RCV[i] = int(years_RCV[i])
      if firstRCV > years_RCV[i]:
        firstRCV = years_RCV[i]
      if recentRCV < years_RCV[i]:
        recentRCV = years_RCV[i]

    firstElse = int(years_Else[0])
    recentElse = int(years_Else[0])
    for i in range(len(years_Else)):
        years_Else[i] = int(years_Else[i])
        if firstElse > years_Else[i]:
            firstElse = years_Else[i]
        if firstElse < years_Else[i]:
            recentElse = years_Else[i]

    # Counting the number of RCV minority candidates for the minorities found in the spreadsheet
    for i in range(len(race_RCV)):
      if (race_RCV[i] == 'Asian' or race_RCV[i] == 'Pacific Islander (Asian)'):
        numAsiansRCV += 1
      if race_RCV[i] == 'African American':
        numAfricanAmericansRCV += 1
      if race_RCV[i] == 'Latino':
        numLatinosRCV += 1
      if race_RCV[i] == 'Middle Eastern':
        numMiddleEasternRCV += 1
      if race_RCV[i] == 'Native American':
        numNativeAmericansRCV += 1

    if len(race_RCV) != 0:
      print(f'Asians RCV between 2010 - 2014 (5 years):', numAsiansRCV, '\n')
      print(f'African Americans RCV between 2010 - 2014 (5 years):', numAfricanAmericansRCV, '\n')
      print(f'Latinos RCV between 2010 - 2014 (5 years):', numLatinosRCV, '\n')
      print(f'Middle Easterners RCV between 2010 - 2014 (5 years):', numMiddleEasternRCV, '\n')
      print(f'Native Americans RCV between 2010 - 2014 (5 years):', numNativeAmericansRCV, '\n')
      print(f'Total number of candidates RCV between 2010 - 2014 (5 years):', len(race_RCV), '\n')

    for i in range(len(race_Else)):
      if (race_Else[i] == 'Asian' or race_Else[i] == 'Pacific Islander (Asian)'):
        numAsiansElse += 1
      if race_Else[i] == 'African American':
        numAfricanAmericansElse += 1
      if race_Else[i] == 'Latino':
        numLatinosElse += 1
      if race_Else[i] == 'Native American':
        numNativeAmericansElse += 1

    if len(race_Else) != 0:
      print(f'Asians General Election:', numAsiansElse, '\n')
      print(f'African Americans General Election:', numAfricanAmericansElse, '\n')
      print(f'Latinos General Election:', numLatinosElse, '\n')
      print(f'Middle Easterners General Election:', numMiddleEasternElse, '\n')
      print(f'Native Americans General Election:', numNativeAmericansElse, '\n')
      print(f'Total number of candidates General Election:', len(race_Else), '\n')

N = 2
asians = (numAsiansRCV, numAsiansElse)
africanamericans = (numAfricanAmericansRCV, numAfricanAmericansElse)
latinos = (numLatinosRCV, numLatinosElse)
nativeamericans = (numNativeAmericansRCV, numNativeAmericansElse)

rcvYears = "RCV (" + str(firstRCV) + "-" + str(recentRCV) + ")"
generalYears = "General (" + str(firstElse) + "-" + str(recentElse) + ")"

ind = np.arange(N)
width = 0.2
plt.bar(ind, asians, width, label='Asian Americans')
plt.bar(ind + width, africanamericans, width,
    label='African Americans')
plt.bar(ind + 2*width, latinos, width,
    label='Latinos')
plt.bar(ind + 3*width, nativeamericans, width,
    label='Native Americans')

plt.ylabel('Number of Candidates')
plt.title(city)

plt.xticks(ind + 0.1 + width, (rcvYears, generalYears))
plt.legend(loc='best')
plt.show()
