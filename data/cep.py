import requests
def consultar(message,bot):
	cmd = (message.text).replace('/cep','').replace('/CEP','')
	print('Consulta por CEP requisitada por {} {}'.format(message.chat.first_name,message.chat.last_name))
	if len(cmd) != 8:
		msg="QUANTIDADE DE DIGITOS INVALIDA"
	else:
		api = requests.get('https://viacep.com.br/ws/{}/json/'.format(cmd)).json()
		if 'erro' not in api:
			msg=('''
			Cep: {}
			Logradouro: {}
            Complemento: {}
            Bairro: {}
            Cidade: {}
            Estado: {}
            IBGE: {}
            GIA: {}
            SIAFI: {}
            DDD: {}'''.format(api['cep'],api['logradouro'],api['complemento'],api['bairro'],api["localidade"],api['uf'],api['ibge'],api['gia'],api['siafi'],api['ddd']))
		else:
			msg='{}: CEP INVALIDO.'.format(cmd)
	bot.reply_to(message,msg)