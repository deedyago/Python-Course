import reading as r
import view as v

dataFile = "database.csv"

def CheckFileExtension(dataFile):
    dataFileList = dataFile.split(".")
    if dataFileList[1] == "csv":
        dataBase = r.ReadCsv(dataFile)
    elif dataFileList[1] == "json":
        dataBase = r.ReadJson(dataFile)
    return dataBase
dataBase = CheckFileExtension(dataFile)

def FindEmployee(input):
    output = [i for i in dataBase if input in i.values()]
    #print(output)
    return output

def RemoveEmployee(dataBase):
    inPut = int(input(("Input ID of employee to remove: ")))
    dataBase.remove(dataBase[inPut])
    #print(dataBase)
    return dataBase

def MainLogic(input):
    while input != 7:
        if input == 1:
            v.Print(FindEmployee(v.FindContact()))
            MainLogic(v.Menu())
        elif input == 0:
            v.Print(dataBase)
            MainLogic(v.Menu())
        elif input == 2:
            dataBase.append(v.AddContact())
            v.Print(dataBase)
            MainLogic(v.Menu())
        elif input == 3:
            RemoveEmployee(dataBase)
            v.Print(dataBase)
            MainLogic(v.Menu())
        elif input == 4:
            v.WriteJson(dataBase)
            MainLogic(v.Menu())
        elif input == 5:
            v.WriteCsv(dataBase)
            MainLogic(v.Menu())
        elif input == 6:
            break
