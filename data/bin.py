import requests
def consultar(message,bot):
	cmd = (message.text).replace('/bin','').replace('/BIN','')
	print('Consulta por Binlist requisitada por {} {}'.format(message.chat.first_name,message.chat.last_name))
	headers = {"Accept-Version":"3","User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
	try:
		api = requests.get('https://lookup.binlist.net/{}'.format(cmd),headers = headers).json()
		msg='''
	Bandeira: {}
    Marca: {}
    Tipo: {}
    Pais: {}
    Latitude: {}
    Longitude: {}
    Moeda: {}
    Emoji: {}
'''.format(api['scheme'],api['brand'],api['type'],api['country']['name'],api['country']['latitude'],api['country']['longitude'],api['country']['currency'],api['country']['emoji'])
	except:
		msg='{} :BIN não encontrada'.format(cmd)
	bot.reply_to(message.chat.id,msg)