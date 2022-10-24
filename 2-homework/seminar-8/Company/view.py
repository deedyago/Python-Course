# —оздать информационную систему позвол€ющую работать с сотрудниками некой компании \ студентами вуза \ учениками школы

import json
import csv

def Menu():
    print("\n" + "=" * 20)
    print("0. Print: ")
    print("1. Find employee: ")
    print("2. Add employee: ")
    print("3. Remove employee: ")
    print("4. Export to json: ")
    print("5. Export to csv: ")
    print("6. Close the programm: ")
    userInput = int(input("Input: "))
    if -1 < userInput < 7:
        return userInput
    else:
         print("Incorrect number! Please check you are inputing correct number of opperation and retry again")

def FindContact():
    find = input("Input contact's name: ")
    return find

def AddContact():
    names = ["ID","Lastname", "Firstname", "Position", "Phone number", "Salary"]
    dataOut = []
    newContact = [0]*7
    newContact[0] = input('Input ID: ')
    newContact[1] = input('Input Secondname: ')
    newContact[2] = input('Input Firstname: ')
    newContact[3] = input('Input Position: ')
    newContact[4] = input('Input Phone Number: ')
    newContact[5] = input('Input Salary: ')
    for i in range(len(newContact)):
        dataOut = dict(zip(names, newContact))
    return dataOut


def Print(dataToPrint):
    names = ["ID","Lastname", "Firstname", "Position", "Phone number", "Salary"]
    dataOut = []
    for i in range(len(dataToPrint)):
        #dataOut.append(dataToPrint[i].values())
        dataOut = dict(zip(names, dataToPrint[i].values()))
        print(dataOut.values())
    #print(dataOut)
    

def WriteJson(employees: list):
    nameOfFIle = str(input("Name of file: "))
    with open(f'{nameOfFIle}.json', 'w', encoding='utf-8') as databaseOut:
        for employee in employees:
            databaseOut.write(json.dumps(employee) + '\n')

def WriteCsv(employees: list):
    nameOfFIle = str(input("Name of file: "))
    with open(f'{nameOfFIle}.csv', 'w', encoding='utf-8') as databaseOut:
        csv_writer = csv.writer(databaseOut)
        for employee in employees:
            csv_writer.writerow(employee.values())