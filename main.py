#!/usr/bin/env python

import os,subprocess,sys,time,re
#MODE 1=CPF 2=TEL 3=NAME
#API MODULE FOR TEL,NAME AND CPF 

info = [
'RobinHood bot',
'v0.2',
'beta',
'YATO',
'http://t.me/RobinHoodBRBot'
]

fogo = u'\U0001F525'


def clear():
		os.system('clear')
clear()
try:
	from data import cpf as api
	#from data import JLconsultas as api
	#from data import hollibot as api
	from data import about
	from data import ip
	from data import placa
	from data import yt
	from data import bin
	from data import banks
	from data import cep
	from data import gerarcpf
except:
	print('Data corrompida')
	sys.exit()
if os.path.exists('telebot'):
	pass
else:
	print('Sem pyTelegramBotAPI,baixe-o no github')
	print('https://github.com/eternnoir/pyTelegramBotAPI')
	sys.exit()

try:
	import requests,pytube,telebot
	from pytube import YouTube
	from telebot import TeleBot
except:
	choice = input('Deseja instalar as dependências? [s/n]')
	if choice == 's' or choice == 'S':
		os.system('pip3 install pyTelegramBotAPI requests pytube')
		import requests,pytube,telebot
		from telebot import TeleBot
	else:
		sys.exit()
		
file = open('token','r')
token = str(file.read())
file.close()
clear()
bot = telebot.TeleBot(token,parse_mode='markdown')

@bot.message_handler(commands=['command'])
def example_command(message):
	cmd = message.text[9:]
	msg = "Command received: {}".format(cmd)

	bot.reply_to(message,msg)

@bot.message_handler(commands=['gerarcpf', 'GERARCPF'])
def GERARCPF(message):
	gerarcpf.gerar(message,bot)

@bot.message_handler(commands=['ip', 'IP'])
def consip(message):
	ip.consultar(message,bot)

@bot.message_handler(commands=['placa', 'PLACA'])
def consplaca(message):
	placa.consultar(message,bot)

@bot.message_handler(commands=['yt', 'YT'])
def youtube(message):
	yt.download(message,bot)

@bot.message_handler(commands=['ytmp3', 'YTMP3'])
def youtubemp3(message):
	yt.downloadmp3(message,bot)

@bot.message_handler(commands=['cpf','CPF'])
def consultacpf(message):
	mode = 1
	print('Consulta por CPF requisitada por {} {}'.format(message.chat.first_name,message.chat.last_name))
	api.consultar(message,bot,mode)

@bot.message_handler(commands=['nome','NOME'])
def consultanome(message):
	mode = 3
	print('Consulta por nome requisitada por {} {}'.format(message.chat.first_name,message.chat.last_name))
	api.consultar(message,bot,mode)

@bot.message_handler(commands=['bin', 'BIN'])
def BIN(message):
	bin.consultar(message,bot)

@bot.message_handler(commands=['banco', 'BANCO'])
def BANCOS(message):
	banks.consultar(message,bot)

@bot.message_handler(commands=['cep', 'CEP'])
def CEP(message):
	cep.consultar(message,bot)


@bot.message_handler(commands=['tel', 'TEL'])
def telefone(message):
	mode=2
	print('Consulta por telefone requisitada por {} {}'.format(message.chat.first_name,message.chat.last_name))
	api.consultar(message,bot,mode)

@bot.message_handler(commands=['sobre','SOBRE'])
def sobre(message):
	about.about(message,bot,info)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	print('Mensagem de ajuda requisitada por {} {}'.format(message.chat.first_name,message.chat.last_name))
	f=open('robinhood2.jpeg','rb')
	msg= f'''
	{fogo}	*{info[0]} {info[1]} {info[2]}* {fogo}
	
	*Lista de comandos disponiveis:*
	
	_Funcionando atualmente:_
	*/gerarcpf :* Gera um numero de CPF
	*/ip :* Consulta por IP
	*/bin :* Consulta de BIN
	*/banco :* Consulta de código bancário
	*/placa :* Consulta por placa
	*/cep :* Consulta por CEP
	*/yt :* Download de video pelo youtube
	*/tel :* Consulta por telefone
	*/cpf :* Consulta por CPF
	*/ytmp3 :* Download de musica pelo youtube
	*/nome:* Consulta por nome

	_Projetos para o futuro:_
	*/sobre :* Mostra como obter o bot

	Criador:{info[3]}

	{info[4]}

	'''
	bot.send_photo(message.chat.id,f)
	bot.reply_to(message,msg)
	f.close()

while True:
    try:
    	bot.polling(none_stop=True)

    except Exception as e:
        telebot.logger.error(e)
        time.sleep(5)