from telegram.ext import *
import telegram
import requests
#import configparser
import os

class telbot:
    def __init__(self):
        self.read_token()
        self.host="http://mnist:5000"

    def read_token(self):
       #self.config = configparser.ConfigParser()
       #self.config.read('config.ini')
       self.token=os.environ.get('tel_token')
       

    def startbot(self):
        # 初始化bot
        self.updater = Updater(token=self.token,use_context=False)
        self.dispatcher = self.updater.dispatcher
        self.dispatcher.add_handler(CommandHandler('hi', self.hi))
        self.dispatcher.add_handler(CommandHandler('set_host', self.set_host))
        self.dispatcher.add_handler(CommandHandler('feed_back', self.feedBack))
        self.dispatcher.add_handler(MessageHandler(Filters.photo, self.photo_handler))
        

    def hi(self,bot, update): # 新增指令/start
        message = update.message
        chat = message['chat']
        update.message.reply_text(text='HI  ' + str(chat['first_name'])+' '+str(chat['last_name']))
    
    def feedBack(self,bot,update):
        message = update.message
        feedback= update.message['text']
        defult_host=self.host
        filename=str(update.message['chat']['first_name'])+".jpg"
        with open("./"+filename,"rb") as f:
            r=requests.post(defult_host,files={"img":f,"feedback":feedback})
            print(r.text)
        update.message.reply_text(text="Thank you for your feed back")


    def set_host(self,bot,update):
        message = update.message
        newhost=update.message['text']
        chat = message['chat']
        print(str(chat['first_name'])+' '+str(chat['last_name'])+" setup new host as: ",newhost)
        self.host=newhost
        update.message.reply_text(text='new host is :'+str(self.host))

    def off(self,bot,update):
        print("turn off")
        self.updater.stop()

    def photo_handler(self,bot, update):
        print("recive Photo")
        file = update.message.photo[0].get_file()
        #print(file)
        filename=str(update.message['chat']['first_name'])+".jpg"
        path = file.download("./"+filename)
        #print(path)

        defult_host=self.host
        with open("./"+filename,"rb") as f:
            r=requests.post(defult_host,files={"img":f})
            print(r.text)
        update.message.reply_text(text='The number is '+r.text)

if __name__=='__main__':
    mybot=telbot()
    mybot.startbot()
    mybot.updater.start_polling()
    
"""     while True:
        text = input()
        # Gracefully stop the event handler
        if text == 'stop':
            mybot.updater.stop()
            break

        # else, put the text into the update queue to be handled by our handlers
        elif len(text) > 0:
            mybot.update_queue.put(text) """