import requests
def gerar(message,bot):
	token='f01e0024a26baef3cc53a2ac208dd141'
	msg = 'Gerando CPF...'
	bot.reply_to(message,msg)
	print('Gerador de CPF requisitado')
	data =requests.get('http://geradorapp.com/api/v1/cpf/generate?token={}'.format(token)).json()
	cpf = (data['data']['number_formatted'])

	msg = f'''
	CPF gerado: {cpf}
	'''
	bot.reply_to(message,msg)