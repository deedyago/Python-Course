from telegram import Update
from telegram.ext import ContextTypes
import reading2 as r
import os
import func2 as f

dataFile = 'database.csv'
#���� �� ������ �������� ����� �������������, ��� ������� �������� �� ��������?(((((
#dataFile = '.'
#async def UserFileDownloader(update: Update, context: ContextTypes.DEFAULT_TYPE):
#    global dataFile
#    file_id = update.message.document
#    newFile = await context.bot.get_file(file_id)
#    await newFile.download()
#    f = str(newFile).split()
#    dataFile = os.path.basename(str(f[7]))
#    #await update.message.reply_text(f'{output}')

#for i in dataFile:
#    if '\'' in dataFile:
#        dataFile = dataFile.replace('\'','')

#for i in dataFile:
#    if '}' in dataFile:
#        dataFile = dataFile.replace('}','')


# �������� �� ��� �����
def CheckFileExtension():
    dataFileList = dataFile.split(".")
    if dataFileList[1] == "csv":
        dataBase = r.ReadCsv(dataFile)
    elif dataFileList[1] == "json":
        dataBase = r.ReadJson(dataFile)
    return dataBase
dataBase = CheckFileExtension()
