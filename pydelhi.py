from telegram.ext import Updater,CommandHandler
from telegram import ChatAction
from datetime import datetime, timedelta
from pytz import timezone
from time import sleep
import logging,requests,pytz,re,ast

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

updater=Updater(token='Telegram-Bot-API-Token')
dispatcher=updater.dispatcher

meetupApi={'sign':'true','key':'Meetup-API-Token'}

utc = pytz.utc

volunteer={}

admins=['list-of-people-who-can-modify-teams']

with open('volunteer.json', 'r') as fp:
    volunteer = ast.literal_eval(fp.read())
    #print(volunteer)

print("I'm here..!!")

def start(bot, update, args):
        bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING)
        sleep(0.2)
        bot.sendMessage(chat_id=update.message.chat_id,text='''
Hi! I have been trained for serving the PyConf Hyderabad Community only!
Use /help to get /help''')

def mailing_list(bot, update):
        bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING)
        sleep(0.2)
        bot.sendMessage(chat_id=update.message.chat_id,text='https://mail.python.org/mm3/mailman3/lists/hydpy.python.org')

def website(bot, update):
        bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING)
        sleep(0.2)
        bot.sendMessage(chat_id=update.message.chat_id,text='https://http://pyconf.hydpy.org/')

#def irc(bot, update):
 #       bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING)
  #      sleep(0.2)
   #     bot.sendMessage(chat_id=update.message.chat_id,text='http://bit.ly/pydelhi-irc')

def twitter(bot, update):
        bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING)
        sleep(0.2)
        bot.sendMessage(chat_id=update.message.chat_id,text='https://twitter.com/hydPython')

def meetup(bot, update):
        bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING)
        sleep(0.2)
        bot.sendMessage(chat_id=update.message.chat_id,text='https://www.meetup.com/Hyderabad-Python-Meetup-Group/')

def nextmeetup(bot, update):
        bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING)
        sleep(0.2)
        r=requests.get('http://api.meetup.com/Hyderabad-Python-Meetup-Group/events', params=meetupApi)
        #print(r.json()[0])
        event_link=r.json()[0]['link']
        date_time=r.json()[0]['time']//1000
        utc_dt = utc.localize(datetime.utcfromtimestamp(date_time))
        indian_tz = timezone('Asia/Kolkata')
        date_time=utc_dt.astimezone(indian_tz)
        date_time=date_time.strftime('%Y-%m-%d %H:%M:%S %Z%z')
        if 'venue' in r.json()[0]:
                venue=r.json()[0]['venue']['address_1']
                bot.sendLocation(chat_id=update.message.chat_id, latitude=r.json()[0]['venue']['lat'],longitude=r.json()[0]['venue']['lon'])
        else:
                venue='Venue is still to be decided'
        bot.sendMessage(chat_id=update.message.chat_id, text='''
Next Meetup
Date/Time : %s
Venue : %s
Event Page : %s
'''%(date_time, venue, event_link))

def nextmeetups(bot, update):
        bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING)
        sleep(0.2)
        r=requests.get('http://api.meetup.com/pydelhi/events', params=meetupApi)
        #print(re.sub('</a>','',re.sub('<a href="','',re.sub('<br/>',' ',re.sub('<p>',' ',re.sub('</p>','\n',r.json()[0]['description']))))))
        bot.sendMessage(chat_id=update.message.chat_id, text='''
Next Meetup Schedule
%s
'''%(re.sub('</a>','',re.sub('<a href="','',re.sub('<br/>',' ',re.sub('<p>',' ',re.sub('</p>','\n',r.json()[0]['description'])))))),parse_mode='HTML')

def facebook(bot, update):
        bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING)
        sleep(0.2)
        bot.sendMessage(chat_id=update.message.chat_id, text='http://bit.ly/pydelhi-facebook')

def github(bot, update):
        bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING)
        sleep(0.2)
        bot.sendMessage(chat_id=update.message.chat_id, text='http://github.com/pydelhi')

def invitelink(bot,update):
        bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING)
        sleep(0.2)
        bot.sendMessage(chat_id=update.message.chat_id, text='https://telegram.me/joinchat/B90LyQVj1nswbAk2x4tJ6g')

def socialmediateam(bot,update):
    m=update.message.to_dict()
    username=m['from']['username']
    if True:
        v=[x[1:] for x in volunteer['socialmedia'].split('-')]
        team='  '.join(v)
        if team!='':
                bot.sendMessage(chat_id=update.message.chat_id, text="""Social Media team
"""+team+"""
Please use '@' at the start of each username to ping them.""")
        else:
                bot.sendMessage(chat_id=update.message.chat_id, text='No one in this team yet.')

def designteam(bot,update):
    m=update.message.to_dict()
    username=m['from']['username']
    if True:
        v=[x[1:] for x in volunteer['design'].split('-')]
        team='  '.join(v)
        if team!='':
                bot.sendMessage(chat_id=update.message.chat_id, text="""Design Team
"""+team+"""
Please use '@' at the start of each username to ping them.""")
        else:
                bot.sendMessage(chat_id=update.message.chat_id, text='No one in this team yet.')

def logisticsteam(bot,update):
    m=update.message.to_dict()
    username=m['from']['username']
    if True:
        v=[x[1:] for x in volunteer['logistics'].split('-')]
        team='  '.join(v)
        if team!='':
                bot.sendMessage(chat_id=update.message.chat_id, text="""Logistics Team
"""+team+"""
Please use '@' at the start of each username to ping them.""")
        else:
                bot.sendMessage(chat_id=update.message.chat_id, text='No one in this team yet.')
        

def websiteteam(bot,update):
    m=update.message.to_dict()
    username=m['from']['username']
    if True:
        v=[x[1:] for x in volunteer['website'].split('-')]
        team='  '.join(v)
        if team!='':
                bot.sendMessage(chat_id=update.message.chat_id, text="""Website Team
"""+team+"""
Please use '@' at the start of each username to ping them.""")
        else:
                bot.sendMessage(chat_id=update.message.chat_id, text='No one in this team yet.')

def vendorteam(bot,update):
    m=update.message.to_dict()
    username=m['from']['username']
    if True:
        v=[x[1:] for x in volunteer['vendor'].split('-')]
        team='  '.join(v)
        if team!='':
                bot.sendMessage(chat_id=update.message.chat_id, text="""Vendor Team
"""+team+"""
Please use '@' at the start of each username to ping them.""")
        else:
                bot.sendMessage(chat_id=update.message.chat_id, text='Noone on this team yet.')

def sponsorshipteam(bot,update):
    m=update.message.to_dict()
    username=m['from']['username']
    if True:
        v=[x[1:] for x in volunteer['sponsorship'].split('-')]
        team='  '.join(v)
        if team!='':
                bot.sendMessage(chat_id=update.message.chat_id, text="""Sponsorship Team
"""+team+"""
Please use '@' at the start of each username to ping them.""")
        else:
                bot.sendMessage(chat_id=update.message.chat_id, text='Noone on this team yet.')

def modifyteam(bot,update,args):
        m=update.message.to_dict()
        username=m['from']['username']
        if username in admins:
                if m['chat']['type']=='private':
                                if m['chat']['id']==-90429051:
                                        bot.sendMessage(chat_id=update.message.chat_id, text='You can only make changes from inside PyDelhi Group')
                                else:
                                        if len(args)<3:
                                                bot.sendMessage(chat_id=update.message.chat_id, text='Please type /modifyteam<space>add/remove<space>socialmedia/design/website/vendor/logistics<space>space seperated usernames.')
                                        else:
                                                if args[0]=='add' or args[0]=='remove':
                                                        if args[1]=='socialmedia' or args[1]=='website' or args[1]=='vendor' or args[1]=='logistics' or args[1]=='design':
                                                                team=volunteer[args[1]].split('-')
                                                                if args[0]=='add':
                                                                        for x in args[2:]:
                                                                                if x.startswith('@')==False:
                                                                                        bot.sendMessage(chat_id=update.message.chat_id, text="Username '"+x+"' is invalid, please use @ properly.")
                                                                                        return
                                                                                elif x in team:
                                                                                        args.remove(x)
                                                                                        bot.sendMessage(chat_id=update.message.chat_id, text="Username '"+x+"' already exists on "+args[1]+" team, ignoring.")
                                                                        if len(args[2:])!=0:
                                                                                team.extend(args[2:])
                                                                                volunteer[args[1]]='-'.join(team)
                                                                                try:
                                                                                        v=open('volunteer.json', 'w')
                                                                                        v.write(str(volunteer))
                                                                                        v.close()
                                                                                        bot.sendMessage(chat_id=update.message.chat_id, text="Team Modified")
                                                                                except:
                                                                                        bot.sendMessage(chat_id=update.message.chat_id, text="Their might be some problem with the server, please try again later or contact @realslimshanky.")
                                                                        else:
                                                                                        bot.sendMessage(chat_id=update.message.chat_id, text="Nothing to modify in team.")
                                                                else:
                                                                                for x in args[2:]:
                                                                                        if x.startswith('@')==False:
                                                                                                bot.sendMessage(chat_id=update.message.chat_id, text="Username '"+x+"' is invalid, please use @ properly.")
                                                                                                return
                                                                                        elif x not in team:
                                                                                                args.remove(x)
                                                                                                bot.sendMessage(chat_id=update.message.chat_id, text="Username '"+x+"' doesn't exists on "+args[1]+" team, ignoring.")
                                                                                if len(args[2:])!=0:
                                                                                        for x in args[2:]:
                                                                                                        if x in team:
                                                                                                                team.remove(x)
                                                                                        volunteer[args[1]]='-'.join(team)
                                                                                        try:
                                                                                                v=open('volunteer.json', 'w')
                                                                                                v.write(str(volunteer))
                                                                                                v.close()
                                                                                                bot.sendMessage(chat_id=update.message.chat_id, text="Team Modified")
                                                                                        except:
                                                                                                bot.sendMessage(chat_id=update.message.chat_id, text="Their might be some problem with the server, please try again later or contact @realslimshanky.")
                                                                                else:
                                                                                                bot.sendMessage(chat_id=update.message.chat_id, text="Nothing to modify in team.")
                                                        else:
                                                                bot.sendMessage(chat_id=update.message.chat_id, text="Please use on of these teams, socialmedia/design/website/vendor/logistics")
                                                else:
                                                        bot.sendMessage(chat_id=update.message.chat_id, text="Please 'add' or 'remove'")
                else:
                        bot.sendMessage(chat_id=update.message.chat_id, text='You cannot edit team members in a private chat.')		

def help(bot, update):
	bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING)
	sleep(0.2)
	bot.sendMessage(chat_id=update.message.chat_id, text='''
Use one of the following commands
/mailinglist - to get PyDelhi Mailing List link
/irc - to get a link to Pydelhi IRC channel
/twitter - to get Pydelhi Twitter link
/meetuppage - to get a link to PyDelhi Meetup page
/nextmeetup - to get info about next Meetup
/nextmeetupschedule - to get schedule of next Meetup
/facebook - to get a link to PyDelhi Facebook page
/github - to get a link to PyDelhi Github page
/invitelink - to get an invite link for PyDelhi Telegram Group of Volunteers

To contribute to|modify this bot : https://github.com/realslimshanky/PyDelhi-Bot
''')

dispatcher.add_handler(CommandHandler('start', start, pass_args=True))
dispatcher.add_handler(CommandHandler('mailinglist', mailing_list))
dispatcher.add_handler(CommandHandler('website', website))
dispatcher.add_handler(CommandHandler('irc', irc))
dispatcher.add_handler(CommandHandler('twitter', twitter))
dispatcher.add_handler(CommandHandler('meetuppage', meetup))
dispatcher.add_handler(CommandHandler('nextmeetup', nextmeetup))
dispatcher.add_handler(CommandHandler('nextmeetupschedule', nextmeetups))
dispatcher.add_handler(CommandHandler('facebook', facebook))
dispatcher.add_handler(CommandHandler('github', github))
dispatcher.add_handler(CommandHandler('invitelink', invitelink))
dispatcher.add_handler(CommandHandler('socialmediateam', socialmediateam))
dispatcher.add_handler(CommandHandler('logisticsteam', logisticsteam))
dispatcher.add_handler(CommandHandler('websiteteam', websiteteam))
dispatcher.add_handler(CommandHandler('designteam', designteam))
dispatcher.add_handler(CommandHandler('sponsorshipteam', sponsorshipteam))
dispatcher.add_handler(CommandHandler('vendorteam', vendorteam))
dispatcher.add_handler(CommandHandler('modifyteam', modifyteam, pass_args=True))
dispatcher.add_handler(CommandHandler('help', help))

updater.start_polling()
