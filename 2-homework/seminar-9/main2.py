from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler
import func2 as f
import logic2 as l

if __name__ == '__main__':
    application = ApplicationBuilder().token('5284203236:AAFpIZTYWEbm0_dJq52cDeG-D0wKF-7iP8c').build()
    
    application.add_handler(CommandHandler('start', f.start)) 

    application.add_handler(CommandHandler('db', f.Menu))                                 #���� � ���������

    #application.add_handler(CommandHandler('view_up', f.DownloaderViewMenu))              #���� ����������� �������
    #application.add_handler(MessageHandler(filters.Document.ALL, l.UserFileDownloader))   #���� �����������  �������

    application.add_handler(CommandHandler('view_0', f.PrintAll))                         #����� ���� 

    application.add_handler(CommandHandler('view_1', f.FindMenuView))                     #���� ������ �� ����
    application.add_handler(CommandHandler('find', f.FindE))                              #����� �� ����

    application.add_handler(CommandHandler('view_2', f.AddViewMenu))                      #���� ���������� � ����
    application.add_handler(CommandHandler('add', f.AddEmployee))                         #���������� � ����

    application.add_handler(CommandHandler('view_3', f.RemoveViewMenu))                   #���� �������� �� ����
    application.add_handler(CommandHandler('remove', f.RemoveEmployee))                   #�������� �� ����

    application.add_handler(CommandHandler('view_4', f.JsonExportViewMenu))               #������� JSON
    application.add_handler(CommandHandler('jsonexport', f.JsonExport))

    application.add_handler(CommandHandler('view_5', f.CsvExportViewMenu))                #������� CSV
    application.add_handler(CommandHandler('csvexport', f.CsvExport))
    

    application.run_polling()