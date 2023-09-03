try:
	import telebot
	import requests
	
	from os import system
except:
	system('pip install pyTelegramBotAPI==3.7.7')
	system('pip install mechanize')
	system('pip install PyTelegramBotApi')
	system('pip install telebot')
	system('pip install requests')
token=input('token :')
bot=telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start(message):
	bot.reply_to(message,'مرحبا بك في بوت معلومات حساب تيك توك ...... @D_C_F')
	bot.send_message(message.chat.id,'اليوزر ')
	
	@bot.message_handler(func=lambda message:True)
	def yahya(message):
		user=(message.text)

		url=f'https://api.dlyar-dev.tk/info-tiktok.json?user={user}'
		try:
			req=requests.get(url).json()
			id=req['id']
			name=req['name']
			fol=req['followers']
			fols=req['following']
			uid=req['uid']
			likes=req['likes']
			ima=req['img']
			ya=(f'TikTok account information\nname: {name}\nuser: {user}\nfollowers: {fol}\nfollowing: {fols}\nuid: {uid}\nlikes: {likes}\nid: {id}\
programmer:@D_C_F ')
		
		
		
		
			bot.send_photo(message.chat.id,ima,ya)
		except:
			bot.send_message(message.chat.id,'اليوزر غير موجود او مبند تأكد وحاول مره ثانيه')
				
bot.polling(True)
#Rick	