import requests
def consultar(message,bot):
	cmd = (message.text).replace('/banco','').replace('/BANCO','')
	print('Consulta por bancos requisitada por {} {}'.format(message.chat.first_name,message.chat.last_name))
	api = requests.get('https://brasilapi.com.br/api/banks/v1/{}'.format(cmd)).json()
	if 'message' not in api:
		msg='''
		Código bancário: {}
        Nome: {}
        Nome completo: {}
        ISPB: {}
'''.format(api['code'],api['name'],api['fullName'],api['ispb'])
	else:
		msg='{} : Código bancário inválido'.format(cmd)
	bot.reply_to(message,msg)