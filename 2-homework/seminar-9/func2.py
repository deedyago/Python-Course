from telegram import Update, InlineKeyboardButton
from telegram.ext import ContextTypes
import logic2 as l
import csv
import json

dataBase = l.CheckFileExtension() # Подгрузка файла

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Hello! {update.effective_user.first_name}, I am a DataBase Bot, let\'s start')
    return

async def Menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"\n" + "=" * 20 + "\n Input desired operation \n0. Print: \n1. Find employee: \n2. Add employee: \n3. Remove employee: \n4. Export to json: \n5. Export to csv: \n6. Close the programm: ")
    await update.message.reply_text(f'\nInput /view_ number of operation:')
    return

async def DownloaderViewMenu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"/upload (attach your file) ")
    return

async def FindMenuView(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("\n/find (Input contact's info)")
    return
    
async def FindE(update: Update, context: ContextTypes.DEFAULT_TYPE):
    userInputStr = update.message.text.split()
    findWho =  userInputStr[1]
    findWhere = FindEmployee(findWho)
    names = ["ID","Lastname", "Firstname", "Position", "Phone number", "Salary"]
    dataOut = []
    for i in range(len(findWhere)):
       dataOut = dict(zip(names, findWhere[i].values()))
       await update.message.reply_text(f"{dataOut.values()}")
    return

def FindEmployee(input):
    output = [i for i in dataBase if input in i.values()]
    return output

async def PrintAll(update: Update, context: ContextTypes.DEFAULT_TYPE):
    names = ["ID","Lastname", "Firstname", "Position", "Phone number", "Salary"]
    dataOut = []
    for i in range(len(dataBase)):
        dataOut = dict(zip(names, dataBase[i].values()))
        await update.message.reply_text(f"{dataOut.values()}")
    return                
   
async def AddViewMenu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"(/add ...) \nInput ID: \nInput Secondname: \nInput Firstname: \nInput Position: \nInput Phone Number: \nInput Salary: ")
    return

async def AddEmployee(update: Update, context: ContextTypes.DEFAULT_TYPE):
    names = ["ID","Lastname", "Firstname", "Position", "Phone number", "Salary"]
    dataOut = []
    newContact = [0]*6
    userInputStr = update.message.text.split()
    newContact[0] = int(userInputStr[1])
    newContact[1] = userInputStr[2]
    newContact[2] = userInputStr[3]
    newContact[3] = userInputStr[4]
    newContact[4] = userInputStr[5]
    newContact[5] = userInputStr[6]
    for i in range(len(newContact)):
        dataOut = dict(zip(names, newContact))
    dataBase.append(dataOut)
    return 

async def RemoveViewMenu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"/remove (Input ID) ")
    return

async def RemoveEmployee(update: Update, context: ContextTypes.DEFAULT_TYPE):
    userInput = update.message.text.split()
    userInputInt = int(userInput[1])-1
    IdToRemove = []
    b = False
    for i in dataBase:
        if int(userInput[1]) in i.values():
            IdToRemove = dict(i)
            b = True
            break
    if b:
        dataBase.remove(IdToRemove)
        return
    else:
        await update.message.reply_text(f"There is no such ID, retry again...")
        return 


# Блок с выводом(отправлением файла ботом в чат с пользователем с указанием имени файла самим пользоветелем)
 
async def CsvExportViewMenu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"/csvexport (name of file) ")
    return

async def CsvExport(update: Update, context: ContextTypes.DEFAULT_TYPE):
    userInput = update.message.text.split()
    nameOfFIle = userInput[1]
    with open(f'{nameOfFIle}.csv', 'w', encoding='utf-8') as databaseOut:
        csv_writer = csv.writer(databaseOut)
        for employee in dataBase:
            csv_writer.writerow(employee.values())
    chat_id = update.message.chat_id
    with open (f'{nameOfFIle}.csv', 'rb') as databaseOut:
        await context.bot.send_document(chat_id, document = databaseOut, filename = f'{nameOfFIle}.csv')

async def JsonExportViewMenu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"/jsonexport (name of file) ")
    return

async def JsonExport(update: Update, context: ContextTypes.DEFAULT_TYPE):
    userInput = update.message.text.split()
    nameOfFIle = userInput[1]
    with open(f'{nameOfFIle}.json', 'w', encoding='utf-8') as databaseOut:
        for employee in dataBase:
            databaseOut.write(json.dumps(employee) + '\n')
    chat_id = update.message.chat_id
    with open (f'{nameOfFIle}.json', 'rb') as databaseOut:
        await context.bot.send_document(chat_id, document = databaseOut, filename = f'{nameOfFIle}.json')    
    

