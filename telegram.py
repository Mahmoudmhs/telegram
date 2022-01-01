import telepot
#https://www.youtube.com/watch?v=67SH6tCuyLQ        explain the code
token='put here your token'
receiver_id='id number get from --->' # after send 'Hi' message in bot  open https://api.telegram.org/bot<token>/getUpdates


bot=telepot.Bot(token)
bot.sendMessage(receiver_id,'This is an automated test message')   # example for sending text
bot.sendPhoto(receiver_id,photo=open('./MyLibrary/images/green_circle.PNG','rb'))   # example for sending photo