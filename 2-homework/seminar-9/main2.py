from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler
import func2 as f
import logic2 as l

if __name__ == '__main__':
    application = ApplicationBuilder().token('5284203236:AAFpIZTYWEbm0_dJq52cDeG-D0wKF-7iP8c').build()
    
    application.add_handler(CommandHandler('start', f.start)) 

    application.add_handler(CommandHandler('db', f.Menu))                                 #Меню с командами

    #application.add_handler(CommandHandler('view_up', f.DownloaderViewMenu))              #Пока неполностью рабочее
    #application.add_handler(MessageHandler(filters.Document.ALL, l.UserFileDownloader))   #Пока неполностью  рабочее

    application.add_handler(CommandHandler('view_0', f.PrintAll))                         #Вывод базы 

    application.add_handler(CommandHandler('view_1', f.FindMenuView))                     #Меню поиска по базе
    application.add_handler(CommandHandler('find', f.FindE))                              #Поиск по базе

    application.add_handler(CommandHandler('view_2', f.AddViewMenu))                      #Меню добавления в базу
    application.add_handler(CommandHandler('add', f.AddEmployee))                         #Добавление в базу

    application.add_handler(CommandHandler('view_3', f.RemoveViewMenu))                   #Меню удаления из базы
    application.add_handler(CommandHandler('remove', f.RemoveEmployee))                   #Удаление из базы

    application.add_handler(CommandHandler('view_4', f.JsonExportViewMenu))               #Экспорт JSON
    application.add_handler(CommandHandler('jsonexport', f.JsonExport))

    application.add_handler(CommandHandler('view_5', f.CsvExportViewMenu))                #Экспорт CSV
    application.add_handler(CommandHandler('csvexport', f.CsvExport))
    

    application.run_polling()