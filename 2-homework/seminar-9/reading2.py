import csv
import json

def ReadCsv(dataFile):
    employee = []
    with open(f'{dataFile}', 'r', encoding='utf-8') as databaseIn:
        csv_reader = csv.reader(databaseIn)
        for row in csv_reader:
            temp = {}
            temp["ID"] = int(row[0])
            temp["Lastname"] = row[1]
            temp["Firstname"] = row[2]
            temp["Position"] = row[3]
            temp["Phone number"] = row[4]
            temp["Salary"] = row[4]
            employee.append(temp)
    return employee
    
def ReadJson(dataFile):
    employee = []
    with open(f'{dataFile}', 'r', encoding='utf-8') as databaseIn:
        for line in databaseIn:
            temp = json.loads(line.strip())
            employee.append(temp)
    return employee


