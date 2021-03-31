import requests
def consultar(message,bot):
	cmd = message.text[4:]
	print('Consulta de ip requisitada')
	api=requests.get('http://ipwhois.app/json/{}'.format(cmd)).json()
	try:
		msg='''
    IP: {}
    TIPO: {}
    CONTINENTE: {}
    CÓDIGO DO CONTINENTE: {}
    PAIS: {}))
    CAPITAL DO PAIS: {}
    CÓDIGO TELEFÔNICO DO PAÍS: {}
    PAISES VIZINHOS: {}
	REGIÃO: {}
    CIDADE: {}
    LATITUDE: {}
    LONGITUDE: {}
    ASN: {}
    ORG: {}
    ISP: {}
    HORÁRIO PADRÃO: {}
    NOME DO HORÁRIO PADRÃO: {}
    GMT: {}
    MOEDA: {}
    CÓDIGO DA MOEDA: {}
    SIMBOLO DA MOEDA: {}
'''.format(api['ip'],api['type'],api['continent'],api['continent_code'],api['country'],api['country_capital'],api['country_phone'],api['country_neighbours'],api['region'],api['city'],api['latitude'],api['longitude'],api['asn'],api['org'],api['isp'],api['timezone'],api['timezone_name'],api['timezone_gmt'],api['currency_code'],api['currency'],api['currency_symbol'])
	except:
		msg='Não encontrado'
	bot.reply_to(message,msg)