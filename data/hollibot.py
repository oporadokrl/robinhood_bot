import requests
#&key=122345
def consultar(message,bot,mode):
	not_found=0
	if mode == '1':
		try:
			print('Consulta por CPF requisitada por {} {}'.format(message.chat.first_name,message.chat.last_name))
			cmd = (message.text).replace('/cpf','').replace('/CPF','')
			api = requests.get('https://hollibot.com/0006hacker/cpf.php?cpf={}'.format(cmd)).json()
		except:
			pass
	if mode == '2':
		try:
			print('Consulta por telefone requisitada por {} {}'.format(message.chat.first_name,message.chat.last_name))
			cmd = (message.text).replace('/tel','').replace('/TEL','')
			api = requests.get('https://hollibot.com/0006hacker/tel.php?tel={}'.format(cmd)).json()
		except:
			pass
			#bot.reply_to(message,'Erro na API')
	try:
		cpf=(int(api["result"][0]["pessoa"]["cadastral"]["CPF"]))
		pnome=api["result"][0]["pessoa"]["cadastral"]["nomePrimeiro"]
		nomem=api["result"][0]["pessoa"]["cadastral"]["nomeMeio"]
		unome=api["result"][0]["pessoa"]["cadastral"]["nomeUltimo"]
		panome=api["result"][0]["pessoa"]["cadastral"]["nomeParentesco"]
		sexo=api["result"][0]["pessoa"]["cadastral"]["sexo"]
		nasc=api["result"][0]["pessoa"]["cadastral"]["dataNascimento"]
		statrecei=api["result"][0]["pessoa"]["cadastral"]["statusReceitaFederal"]
		dtattrecei=api["result"][0]["pessoa"]["cadastral"]["dataAtualizacaoStatusReceitaFederal"]
		numrg=api["result"][0]["pessoa"]["cadastral"]["rgNumero"]
		orgaorg=api["result"][0]["pessoa"]["cadastral"]["rgOrgaoEmissor"]
		ufrg=api["result"][0]["pessoa"]["cadastral"]["rgUf"]
		teleit=api["result"][0]["pessoa"]["cadastral"]["tituloEleitoral"]
		obito=api["result"][0]["pessoa"]["cadastral"]["obito"]
		nat=api["result"][0]["pessoa"]["cadastral"]["nacionalidade"]
		menor=api["result"][0]["pessoa"]["cadastral"]["menorDeIdade"]
		pep=api["result"][0]["pessoa"]["cadastral"]["pep"]
		estcivil=api["result"][0]["pessoa"]["cadastral"]["estadoCivil"]
		maeCPF=api["result"][0]["pessoa"]["cadastral"]["maeCPF"]
		maepnome=api["result"][0]["pessoa"]["cadastral"]["maeNomePrimeiro"]
		maenomem=api["result"][0]["pessoa"]["cadastral"]["maeNomeMeio"]
		maeunome=api["result"][0]["pessoa"]["cadastral"]["maeNomeUltimo"]
		maepanome=api["result"][0]["pessoa"]["cadastral"]["maeNomeParentesco"]
		escolaridade=api["result"][0]["pessoa"]["cadastral"]["escolaridade"]
		cns=api["result"][0]["pessoa"]["cadastral"]["cns"]
		bolsa=api["result"][0]["pessoa"]["beneficiarioProgramaSocial"]["bolsaFamilia"]
		#conpnome=api["result"][0]["pessoa"]["contato"]["conjugue"]["nomePrimeiro"]
		#connomem=api["result"][0]["pessoa"]["contato"]["conjugue"]["nomeMeio"]
		#conunome=api["result"][0]["pessoa"]["contato"]["conjugue"]["nomeUltimo"]
		#conparentesco=api["result"][0]["pessoa"]["contato"]["conjugue"]["parentesco"]

		msg=f'''
		CPF: {cpf}
		Nome: {pnome} {nomem} {unome}
		Parentesco: {panome}
		Sexo: {sexo}
		Data de nascimento: {nasc}
		Status na Receita Federal: {statrecei}
		Data de atualização da Receita Federal: {dtattrecei}
		RG: {numrg}
		Orgão Emissor do RG: {orgaorg}
		UF do RG: {ufrg}
		Titulo eleitoral: {teleit}
		Faleceu: {obito}
		Nacionalidade: {nat}
		Menor de Idade: {menor}
		Profilaxia: {pep}
		Estado civil: {estcivil}
		CPF da mãe: {maeCPF}
		Nome da mãe: {maepnome} {maenomem} {maeunome}
		Nome de parentesco da mãe: {maepanome}
		Escolaridade: {escolaridade}
		CNS: {cns}
		Bolsa Familia: {bolsa}
		'''
		#CONJUGUE:
		#Nome do conjugue: {conpnome} {connomem} {conunome}
		#Parentesco: {conparentesco}
	except:
		msg='*Número não encontrado ou sistema instável*'
		not_found=1
		
		
		
		#except:
	if not_found == 0:
		msg = msg + '\n ENDEREÇOS:\n'
	try:
		mensagem = f'''
		Tipo de logradouro: {api["result"][0]["pessoa"]["contato"]["endereco"][0]["tipoLogradouro"]}
		Logradouro: {api["result"][0]["pessoa"]["contato"]["endereco"][0]["logradouro"]}
		Numero: {api["result"][0]["pessoa"]["contato"]["endereco"][0]["numero"]}
		Complemento: {api["result"][0]["pessoa"]["contato"]["endereco"][0]["complemento"]}
		Bairro: {api["result"][0]["pessoa"]["contato"]["endereco"][0]["bairro"]}
		Cidade: {api["result"][0]["pessoa"]["contato"]["endereco"][0]["cidade"]}
		UF :{api["result"][0]["pessoa"]["contato"]["endereco"][0]["uf"]}
		CEP: {api["result"][0]["pessoa"]["contato"]["endereco"][0]["cep"]}
		'''
		msg = msg + mensagem
	except:
		pass
	try:
		mensagem = f'''
		Tipo de logradouro: {api["result"][0]["pessoa"]["contato"]["endereco"][1]["tipoLogradouro"]}
		Logradouro: {api["result"][0]["pessoa"]["contato"]["endereco"][1]["logradouro"]}
		Numero: {api["result"][0]["pessoa"]["contato"]["endereco"][1]["numero"]}
		Complemento: {api["result"][0]["pessoa"]["contato"]["endereco"][1]["complemento"]}
		Bairro: {api["result"][0]["pessoa"]["contato"]["endereco"][1]["bairro"]}
		Cidade: {api["result"][0]["pessoa"]["contato"]["endereco"][1]["cidade"]}
		UF :{api["result"][0]["pessoa"]["contato"]["endereco"][1]["uf"]}
		CEP: {api["result"][0]["pessoa"]["contato"]["endereco"][1]["cep"]}
		'''
		msg = msg + mensagem
	except:
		pass
	try:
		mensagem = f'''
		Tipo de logradouro: {api["result"][0]["pessoa"]["contato"]["endereco"][2]["tipoLogradouro"]}
		Logradouro: {api["result"][0]["pessoa"]["contato"]["endereco"][2]["logradouro"]}
		Numero: {api["result"][0]["pessoa"]["contato"]["endereco"][2]["numero"]}
		Complemento: {api["result"][0]["pessoa"]["contato"]["endereco"][2]["complemento"]}
		Bairro: {api["result"][0]["pessoa"]["contato"]["endereco"][2]["bairro"]}
		Cidade: {api["result"][0]["pessoa"]["contato"]["endereco"][2]["cidade"]}
		UF :{api["result"][0]["pessoa"]["contato"]["endereco"][2]["uf"]}
		CEP: {api["result"][0]["pessoa"]["contato"]["endereco"][2]["cep"]}
		'''
		msg = msg + mensagem
	except:
		pass
	try:
		mensagem = f'''
		Tipo de logradouro: {api["result"][0]["pessoa"]["contato"]["endereco"][3]["tipoLogradouro"]}
		Logradouro: {api["result"][0]["pessoa"]["contato"]["endereco"][3]["logradouro"]}
		Numero: {api["result"][0]["pessoa"]["contato"]["endereco"][3]["numero"]}
		Complemento: {api["result"][0]["pessoa"]["contato"]["endereco"][3]["complemento"]}
		Bairro: {api["result"][0]["pessoa"]["contato"]["endereco"][3]["bairro"]}
		Cidade: {api["result"][0]["pessoa"]["contato"]["endereco"][3]["cidade"]}
		UF :{api["result"][0]["pessoa"]["contato"]["endereco"][3]["uf"]}
		CEP: {api["result"][0]["pessoa"]["contato"]["endereco"][3]["cep"]}
		'''
		msg = msg + mensagem
	except:
		pass
	try:
		mensagem = f'''
		Tipo de logradouro: {api["result"][0]["pessoa"]["contato"]["endereco"][4]["tipoLogradouro"]}
		Logradouro: {api["result"][0]["pessoa"]["contato"]["endereco"][4]["logradouro"]}
		Numero: {api["result"][0]["pessoa"]["contato"]["endereco"][4]["numero"]}
		Complemento: {api["result"][0]["pessoa"]["contato"]["endereco"][4]["complemento"]}
		Bairro: {api["result"][0]["pessoa"]["contato"]["endereco"][4]["bairro"]}
		Cidade: {api["result"][0]["pessoa"]["contato"]["endereco"][4]["cidade"]}
		UF :{api["result"][0]["pessoa"]["contato"]["endereco"][4]["uf"]}
		CEP: {api["result"][0]["pessoa"]["contato"]["endereco"][4]["cep"]}
		'''
		msg = msg + mensagem
	except:
		pass
	try:
		mensagem = f'''
		Tipo de logradouro: {api["result"][0]["pessoa"]["contato"]["endereco"][5]["tipoLogradouro"]}
		Logradouro: {api["result"][0]["pessoa"]["contato"]["endereco"][5]["logradouro"]}
		Numero: {api["result"][0]["pessoa"]["contato"]["endereco"][5]["numero"]}
		Complemento: {api["result"][0]["pessoa"]["contato"]["endereco"][5]["complemento"]}
		Bairro: {api["result"][0]["pessoa"]["contato"]["endereco"][5]["bairro"]}
		Cidade: {api["result"][0]["pessoa"]["contato"]["endereco"][5]["cidade"]}
		UF :{api["result"][0]["pessoa"]["contato"]["endereco"][5]["uf"]}
		CEP: {api["result"][0]["pessoa"]["contato"]["endereco"][5]["cep"]}
		'''
		msg = msg + mensagem
	except:
		pass
	try:
		mensagem = f'''
		Tipo de logradouro: {api["result"][0]["pessoa"]["contato"]["endereco"][6]["tipoLogradouro"]}
		Logradouro: {api["result"][0]["pessoa"]["contato"]["endereco"][6]["logradouro"]}
		Numero: {api["result"][0]["pessoa"]["contato"]["endereco"][6]["numero"]}
		Complemento: {api["result"][0]["pessoa"]["contato"]["endereco"][6]["complemento"]}
		Bairro: {api["result"][0]["pessoa"]["contato"]["endereco"][6]["bairro"]}
		Cidade: {api["result"][0]["pessoa"]["contato"]["endereco"][6]["cidade"]}
		UF :{api["result"][0]["pessoa"]["contato"]["endereco"][6]["uf"]}
		CEP: {api["result"][0]["pessoa"]["contato"]["endereco"][6]["cep"]}
		'''
		msg = msg + mensagem
	except:
		pass
	try:
		mensagem = f'''
		Tipo de logradouro: {api["result"][0]["pessoa"]["contato"]["endereco"][7]["tipoLogradouro"]}
		Logradouro: {api["result"][0]["pessoa"]["contato"]["endereco"][7]["logradouro"]}
		Numero: {api["result"][0]["pessoa"]["contato"]["endereco"][7]["numero"]}
		Complemento: {api["result"][0]["pessoa"]["contato"]["endereco"][7]["complemento"]}
		Bairro: {api["result"][0]["pessoa"]["contato"]["endereco"][7]["bairro"]}
		Cidade: {api["result"][0]["pessoa"]["contato"]["endereco"][7]["cidade"]}
		UF :{api["result"][0]["pessoa"]["contato"]["endereco"][7]["uf"]}
		CEP: {api["result"][0]["pessoa"]["contato"]["endereco"][7]["cep"]}
		'''
		msg = msg + mensagem
	except:
		pass
	try:
		mensagem = f'''
		Tipo de logradouro: {api["result"][0]["pessoa"]["contato"]["endereco"][8]["tipoLogradouro"]}
		Logradouro: {api["result"][0]["pessoa"]["contato"]["endereco"][8]["logradouro"]}
		Numero: {api["result"][0]["pessoa"]["contato"]["endereco"][8]["numero"]}
		Complemento: {api["result"][0]["pessoa"]["contato"]["endereco"][8]["complemento"]}
		Bairro: {api["result"][0]["pessoa"]["contato"]["endereco"][8]["bairro"]}
		Cidade: {api["result"][0]["pessoa"]["contato"]["endereco"][8]["cidade"]}
		UF :{api["result"][0]["pessoa"]["contato"]["endereco"][8]["uf"]}
		CEP: {api["result"][0]["pessoa"]["contato"]["endereco"][8]["cep"]}
		'''
		msg = msg + mensagem
	except:
		pass
	try:
		mensagem = f'''
		Tipo de logradouro: {api["result"][0]["pessoa"]["contato"]["endereco"][9]["tipoLogradouro"]}
		Logradouro: {api["result"][0]["pessoa"]["contato"]["endereco"][9]["logradouro"]}
		Numero: {api["result"][0]["pessoa"]["contato"]["endereco"][9]["numero"]}
		Complemento: {api["result"][0]["pessoa"]["contato"]["endereco"][9]["complemento"]}
		Bairro: {api["result"][0]["pessoa"]["contato"]["endereco"][9]["bairro"]}
		Cidade: {api["result"][0]["pessoa"]["contato"]["endereco"][9]["cidade"]}
		UF :{api["result"][0]["pessoa"]["contato"]["endereco"][9]["uf"]}
		CEP: {api["result"][0]["pessoa"]["contato"]["endereco"][9]["cep"]}
		'''
		msg = msg + mensagem
	except:
		pass
	if not_found == 0:
		msg = msg + '\nTELEFONES:\n'
	try:
		mensagem = f'''
			DDD: {api["result"][0]["pessoa"]["contato"]["telefone"][0]["ddd"]}
			Numero: {api["result"][0]["pessoa"]["contato"]["telefone"][0]["numero"]}
			Operadora: {api["result"][0]["pessoa"]["contato"]["telefone"][0]["operadora"]}
			Procon: {api["result"][0]["pessoa"]["contato"]["telefone"][0]["procon"]}
			Whatsapp: {api["result"][0]["pessoa"]["contato"]["telefone"][0]["whatsapp"]}
			Tipo: {api["result"][0]["pessoa"]["contato"]["telefone"][0]["tipoTelefone"]}
			'''
		msg = msg + mensagem
	except:
		pass
	try:
		mensagem = f'''
			DDD: {api["result"][0]["pessoa"]["contato"]["telefone"][1]["ddd"]}
			Numero: {api["result"][0]["pessoa"]["contato"]["telefone"][1]["numero"]}
			Operadora: {api["result"][0]["pessoa"]["contato"]["telefone"][1]["operadora"]}
			Procon: {api["result"][0]["pessoa"]["contato"]["telefone"][1]["procon"]}
			Whatsapp: {api["result"][0]["pessoa"]["contato"]["telefone"][1]["whatsapp"]}
			Tipo: {api["result"][0]["pessoa"]["contato"]["telefone"][1]["tipoTelefone"]}
			'''
		msg = msg + mensagem
	except:
		pass
	try:
		mensagem = f'''
			DDD: {api["result"][0]["pessoa"]["contato"]["telefone"][2]["ddd"]}
			Numero: {api["result"][0]["pessoa"]["contato"]["telefone"][2]["numero"]}
			Operadora: {api["result"][0]["pessoa"]["contato"]["telefone"][2]["operadora"]}
			Procon: {api["result"][0]["pessoa"]["contato"]["telefone"][2]["procon"]}
			Whatsapp: {api["result"][0]["pessoa"]["contato"]["telefone"][2]["whatsapp"]}
			Tipo: {api["result"][0]["pessoa"]["contato"]["telefone"][2]["tipoTelefone"]}
			'''
		msg = msg + mensagem
	except:
		pass
	try:
		mensagem = f'''
			DDD: {api["result"][0]["pessoa"]["contato"]["telefone"][3]["ddd"]}
			Numero: {api["result"][0]["pessoa"]["contato"]["telefone"][3]["numero"]}
			Operadora: {api["result"][0]["pessoa"]["contato"]["telefone"][3]["operadora"]}
			Procon: {api["result"][0]["pessoa"]["contato"]["telefone"][3]["procon"]}
			Whatsapp: {api["result"][0]["pessoa"]["contato"]["telefone"][3]["whatsapp"]}
			Tipo: {api["result"][0]["pessoa"]["contato"]["telefone"][3]["tipoTelefone"]}
			'''
		msg = msg + mensagem
	except:
		pass
	try:
		mensagem = f'''
			DDD: {api["result"][0]["pessoa"]["contato"]["telefone"][4]["ddd"]}
			Numero: {api["result"][0]["pessoa"]["contato"]["telefone"][4]["numero"]}
			Operadora: {api["result"][0]["pessoa"]["contato"]["telefone"][4]["operadora"]}
			Procon: {api["result"][0]["pessoa"]["contato"]["telefone"][4]["procon"]}
			Whatsapp: {api["result"][0]["pessoa"]["contato"]["telefone"][4]["whatsapp"]}
			Tipo: {api["result"][0]["pessoa"]["contato"]["telefone"][4]["tipoTelefone"]}
			'''
		msg = msg + mensagem
	except:
		pass
	try:
		mensagem = f'''
			DDD: {api["result"][0]["pessoa"]["contato"]["telefone"][5]["ddd"]}
			Numero: {api["result"][0]["pessoa"]["contato"]["telefone"][5]["numero"]}
			Operadora: {api["result"][0]["pessoa"]["contato"]["telefone"][5]["operadora"]}
			Procon: {api["result"][0]["pessoa"]["contato"]["telefone"][5]["procon"]}
			Whatsapp: {api["result"][0]["pessoa"]["contato"]["telefone"][5]["whatsapp"]}
			Tipo: {api["result"][0]["pessoa"]["contato"]["telefone"][5]["tipoTelefone"]}
			'''
		msg = msg + mensagem
	except:
		pass
	try:
		mensagem = f'''
			DDD: {api["result"][0]["pessoa"]["contato"]["telefone"][6]["ddd"]}
			Numero: {api["result"][0]["pessoa"]["contato"]["telefone"][6]["numero"]}
			Operadora: {api["result"][0]["pessoa"]["contato"]["telefone"][6]["operadora"]}
			Procon: {api["result"][0]["pessoa"]["contato"]["telefone"][6]["procon"]}
			Whatsapp: {api["result"][0]["pessoa"]["contato"]["telefone"][6]["whatsapp"]}
			Tipo: {api["result"][0]["pessoa"]["contato"]["telefone"][6]["tipoTelefone"]}
			'''
		msg = msg + mensagem
	except:
		pass
	try:
		mensagem = f'''
			DDD: {api["result"][0]["pessoa"]["contato"]["telefone"][7]["ddd"]}
			Numero: {api["result"][0]["pessoa"]["contato"]["telefone"][7]["numero"]}
			Operadora: {api["result"][0]["pessoa"]["contato"]["telefone"][7]["operadora"]}
			Procon: {api["result"][0]["pessoa"]["contato"]["telefone"][7]["procon"]}
			Whatsapp: {api["result"][0]["pessoa"]["contato"]["telefone"][7]["whatsapp"]}
			Tipo: {api["result"][0]["pessoa"]["contato"]["telefone"][7]["tipoTelefone"]}
			'''
		msg = msg + mensagem
	except:
		pass
	try:
		mensagem = f'''
			DDD: {api["result"][0]["pessoa"]["contato"]["telefone"][8]["ddd"]}
			Numero: {api["result"][0]["pessoa"]["contato"]["telefone"][8]["numero"]}
			Operadora: {api["result"][0]["pessoa"]["contato"]["telefone"][8]["operadora"]}
			Procon: {api["result"][0]["pessoa"]["contato"]["telefone"][8]["procon"]}
			Whatsapp: {api["result"][0]["pessoa"]["contato"]["telefone"][8]["whatsapp"]}
			Tipo: {api["result"][0]["pessoa"]["contato"]["telefone"][8]["tipoTelefone"]}
			'''
		msg = msg + mensagem
	except:
		pass
	try:
		mensagem = f'''
			DDD: {api["result"][0]["pessoa"]["contato"]["telefone"][9]["ddd"]}
			Numero: {api["result"][0]["pessoa"]["contato"]["telefone"][9]["numero"]}
			Operadora: {api["result"][0]["pessoa"]["contato"]["telefone"][9]["operadora"]}
			Procon: {api["result"][0]["pessoa"]["contato"]["telefone"][9]["procon"]}
			Whatsapp: {api["result"][0]["pessoa"]["contato"]["telefone"][9]["whatsapp"]}
			Tipo: {api["result"][0]["pessoa"]["contato"]["telefone"][9]["tipoTelefone"]}
			'''
		msg = msg + mensagem
	except:
		pass
	if not_found == 0:
		msg = msg + '\nVIZINHOS:\n'
	try:
		mensagem =f'''
		CPF: {api["result"][0]["pessoa"]["vinculo"]["vizinho"][0]["cpf"]}
		Nome: {api["result"][0]["pessoa"]["vinculo"]["vizinho"][0]["nomePrimeiro"]} {api["result"][0]["pessoa"]["vinculo"]["vizinho"][0]["nomeMeio"]} {api["result"][0]["pessoa"]["vinculo"]["vizinho"][0]["nomeUltimo"]}
		Parentesco: {api["result"][0]["pessoa"]["vinculo"]["vizinho"][0]["nomeParentesco"]}
		'''
		msg = msg + mensagem
	except:
		pass
	try:
		mensagem =f'''
		CPF: {api["result"][0]["pessoa"]["vinculo"]["vizinho"][1]["cpf"]}
		Nome: {api["result"][0]["pessoa"]["vinculo"]["vizinho"][1]["nomePrimeiro"]} {api["result"][0]["pessoa"]["vinculo"]["vizinho"][1]["nomeMeio"]} {api["result"][0]["pessoa"]["vinculo"]["vizinho"][1]["nomeUltimo"]}
		Parentesco: {api["result"][0]["pessoa"]["vinculo"]["vizinho"][1]["nomeParentesco"]}
		'''
		msg = msg + mensagem
	except:
		pass
	try:
		mensagem =f'''
		CPF: {api["result"][0]["pessoa"]["vinculo"]["vizinho"][2]["cpf"]}
		Nome: {api["result"][0]["pessoa"]["vinculo"]["vizinho"][2]["nomePrimeiro"]} {api["result"][0]["pessoa"]["vinculo"]["vizinho"][2]["nomeMeio"]} {api["result"][0]["pessoa"]["vinculo"]["vizinho"][2]["nomeUltimo"]}
		Parentesco: {api["result"][0]["pessoa"]["vinculo"]["vizinho"][2]["nomeParentesco"]}
		'''
		msg = msg + mensagem
	except:
		pass
	try:
		mensagem =f'''
		CPF: {api["result"][0]["pessoa"]["vinculo"]["vizinho"][3]["cpf"]}
		Nome: {api["result"][0]["pessoa"]["vinculo"]["vizinho"][3]["nomePrimeiro"]} {api["result"][0]["pessoa"]["vinculo"]["vizinho"][3]["nomeMeio"]} {api["result"][0]["pessoa"]["vinculo"]["vizinho"][3]["nomeUltimo"]}
		Parentesco: {api["result"][0]["pessoa"]["vinculo"]["vizinho"][3]["nomeParentesco"]}
		'''
		msg = msg + mensagem
	except:
		pass
	try:
		mensagem =f'''
		CPF: {api["result"][0]["pessoa"]["vinculo"]["vizinho"][4]["cpf"]}
		Nome: {api["result"][0]["pessoa"]["vinculo"]["vizinho"][4]["nomePrimeiro"]} {api["result"][0]["pessoa"]["vinculo"]["vizinho"][4]["nomeMeio"]} {api["result"][0]["pessoa"]["vinculo"]["vizinho"][4]["nomeUltimo"]}
		Parentesco: {api["result"][0]["pessoa"]["vinculo"]["vizinho"][4]["nomeParentesco"]}
		'''
		msg = msg + mensagem
	except:
		pass
	try:
		mensagem =f'''
		CPF: {api["result"][0]["pessoa"]["vinculo"]["vizinho"][5]["cpf"]}
		Nome: {api["result"][0]["pessoa"]["vinculo"]["vizinho"][5]["nomePrimeiro"]} {api["result"][0]["pessoa"]["vinculo"]["vizinho"][5]["nomeMeio"]} {api["result"][0]["pessoa"]["vinculo"]["vizinho"][5]["nomeUltimo"]}
		Parentesco: {api["result"][0]["pessoa"]["vinculo"]["vizinho"][5]["nomeParentesco"]}
		'''
		msg = msg + mensagem
	except:
		pass
	try:
		mensagem =f'''
		CPF: {api["result"][0]["pessoa"]["vinculo"]["vizinho"][6]["cpf"]}
		Nome: {api["result"][0]["pessoa"]["vinculo"]["vizinho"][6]["nomePrimeiro"]} {api["result"][0]["pessoa"]["vinculo"]["vizinho"][6]["nomeMeio"]} {api["result"][0]["pessoa"]["vinculo"]["vizinho"][6]["nomeUltimo"]}
		Parentesco: {api["result"][0]["pessoa"]["vinculo"]["vizinho"][6]["nomeParentesco"]}
		'''
		msg = msg + mensagem
	except:
		pass
	try:
		mensagem =f'''
		CPF: {api["result"][0]["pessoa"]["vinculo"]["vizinho"][7]["cpf"]}
		Nome: {api["result"][0]["pessoa"]["vinculo"]["vizinho"][7]["nomePrimeiro"]} {api["result"][0]["pessoa"]["vinculo"]["vizinho"][7]["nomeMeio"]} {api["result"][0]["pessoa"]["vinculo"]["vizinho"][7]["nomeUltimo"]}
		Parentesco: {api["result"][0]["pessoa"]["vinculo"]["vizinho"][7]["nomeParentesco"]}
		'''
		msg = msg + mensagem
	except:
		pass
	try:
		mensagem =f'''
		CPF: {api["result"][0]["pessoa"]["vinculo"]["vizinho"][8]["cpf"]}
		Nome: {api["result"][0]["pessoa"]["vinculo"]["vizinho"][8]["nomePrimeiro"]} {api["result"][0]["pessoa"]["vinculo"]["vizinho"][8]["nomeMeio"]} {api["result"][0]["pessoa"]["vinculo"]["vizinho"][8]["nomeUltimo"]}
		Parentesco: {api["result"][0]["pessoa"]["vinculo"]["vizinho"][8]["nomeParentesco"]}
		'''
		msg = msg + mensagem
	except:
		pass
	try:
		mensagem =f'''
		CPF: {api["result"][0]["pessoa"]["vinculo"]["vizinho"][9]["cpf"]}
		Nome: {api["result"][0]["pessoa"]["vinculo"]["vizinho"][9]["nomePrimeiro"]} {api["result"][0]["pessoa"]["vinculo"]["vizinho"][9]["nomeMeio"]} {api["result"][0]["pessoa"]["vinculo"]["vizinho"][9]["nomeUltimo"]}
		Parentesco: {api["result"][0]["pessoa"]["vinculo"]["vizinho"][9]["nomeParentesco"]}
		'''
		msg = msg + mensagem
	except:
		pass
	if not_found == 0:
		msg = msg + '\nMORADORES:\n'
	try:
		mensagem=f'''
		Parentesco: {api["result"][0]["pessoa"]["vinculo"]["houseHold"][0]["nomeParentesco"]}
		Nome: {api["result"][0]["pessoa"]["vinculo"]["houseHold"][0]["nomePrimeiro"]} {api["result"][0]["pessoa"]["vinculo"]["houseHold"][0]["nomeMeio"]} {api["result"][0]["pessoa"]["vinculo"]["houseHold"][0]["nomeUltimo"]}
		CPF: {api["result"][0]["pessoa"]["vinculo"]["houseHold"][0]["cpf"]}
		'''
		msg = msg + mensagem
	except:
		pass
	try:
		mensagem=f'''
		Parentesco: {api["result"][0]["pessoa"]["vinculo"]["houseHold"][1]["nomeParentesco"]}
		Nome: {api["result"][0]["pessoa"]["vinculo"]["houseHold"][1]["nomePrimeiro"]} {api["result"][0]["pessoa"]["vinculo"]["houseHold"][1]["nomeMeio"]} {api["result"][0]["pessoa"]["vinculo"]["houseHold"][1]["nomeUltimo"]}
		CPF: {api["result"][0]["pessoa"]["vinculo"]["houseHold"][1]["cpf"]}
		'''
		msg = msg + mensagem
	except:
		pass
	try:
		mensagem=f'''
		Parentesco: {api["result"][0]["pessoa"]["vinculo"]["houseHold"][2]["nomeParentesco"]}
		Nome: {api["result"][0]["pessoa"]["vinculo"]["houseHold"][2]["nomePrimeiro"]} {api["result"][0]["pessoa"]["vinculo"]["houseHold"][2]["nomeMeio"]} {api["result"][0]["pessoa"]["vinculo"]["houseHold"][2]["nomeUltimo"]}
		CPF: {api["result"][0]["pessoa"]["vinculo"]["houseHold"][2]["cpf"]}
		'''
		msg = msg + mensagem
	except:
		pass
	try:
		mensagem=f'''
		Parentesco: {api["result"][0]["pessoa"]["vinculo"]["houseHold"][3]["nomeParentesco"]}
		Nome: {api["result"][0]["pessoa"]["vinculo"]["houseHold"][3]["nomePrimeiro"]} {api["result"][0]["pessoa"]["vinculo"]["houseHold"][3]["nomeMeio"]} {api["result"][0]["pessoa"]["vinculo"]["houseHold"][3]["nomeUltimo"]}
		CPF: {api["result"][0]["pessoa"]["vinculo"]["houseHold"][3]["cpf"]}
		'''
		msg = msg + mensagem
	except:
		pass
	try:
		mensagem=f'''
		Parentesco: {api["result"][0]["pessoa"]["vinculo"]["houseHold"][4]["nomeParentesco"]}
		Nome: {api["result"][0]["pessoa"]["vinculo"]["houseHold"][4]["nomePrimeiro"]} {api["result"][0]["pessoa"]["vinculo"]["houseHold"][4]["nomeMeio"]} {api["result"][0]["pessoa"]["vinculo"]["houseHold"][4]["nomeUltimo"]}
		CPF: {api["result"][0]["pessoa"]["vinculo"]["houseHold"][4]["cpf"]}
		'''
		msg = msg + mensagem
	except:
		pass
	try:
		mensagem=f'''
		Parentesco: {api["result"][0]["pessoa"]["vinculo"]["houseHold"][5]["nomeParentesco"]}
		Nome: {api["result"][0]["pessoa"]["vinculo"]["houseHold"][5]["nomePrimeiro"]} {api["result"][0]["pessoa"]["vinculo"]["houseHold"][5]["nomeMeio"]} {api["result"][0]["pessoa"]["vinculo"]["houseHold"][5]["nomeUltimo"]}
		CPF: {api["result"][0]["pessoa"]["vinculo"]["houseHold"][5]["cpf"]}
		'''
		msg = msg + mensagem
	except:
		pass
	try:
		mensagem=f'''
		Parentesco: {api["result"][0]["pessoa"]["vinculo"]["houseHold"][6]["nomeParentesco"]}
		Nome: {api["result"][0]["pessoa"]["vinculo"]["houseHold"][6]["nomePrimeiro"]} {api["result"][0]["pessoa"]["vinculo"]["houseHold"][6]["nomeMeio"]} {api["result"][0]["pessoa"]["vinculo"]["houseHold"][6]["nomeUltimo"]}
		CPF: {api["result"][0]["pessoa"]["vinculo"]["houseHold"][6]["cpf"]}
		'''
		msg = msg + mensagem
	except:
		pass
	try:
		mensagem=f'''
		Parentesco: {api["result"][0]["pessoa"]["vinculo"]["houseHold"][7]["nomeParentesco"]}
		Nome: {api["result"][0]["pessoa"]["vinculo"]["houseHold"][7]["nomePrimeiro"]} {api["result"][0]["pessoa"]["vinculo"]["houseHold"][7]["nomeMeio"]} {api["result"][0]["pessoa"]["vinculo"]["houseHold"][7]["nomeUltimo"]}
		CPF: {api["result"][0]["pessoa"]["vinculo"]["houseHold"][7]["cpf"]}
		'''
		msg = msg + mensagem
	except:
		pass
	try:
		mensagem=f'''
		Parentesco: {api["result"][0]["pessoa"]["vinculo"]["houseHold"][8]["nomeParentesco"]}
		Nome: {api["result"][0]["pessoa"]["vinculo"]["houseHold"][8]["nomePrimeiro"]} {api["result"][0]["pessoa"]["vinculo"]["houseHold"][8]["nomeMeio"]} {api["result"][0]["pessoa"]["vinculo"]["houseHold"][8]["nomeUltimo"]}
		CPF: {api["result"][0]["pessoa"]["vinculo"]["houseHold"][8]["cpf"]}
		'''
		msg = msg + mensagem
	except:
		pass
	try:
		mensagem=f'''
		Parentesco: {api["result"][0]["pessoa"]["vinculo"]["houseHold"][9]["nomeParentesco"]}
		Nome: {api["result"][0]["pessoa"]["vinculo"]["houseHold"][9]["nomePrimeiro"]} {api["result"][0]["pessoa"]["vinculo"]["houseHold"][9]["nomeMeio"]} {api["result"][0]["pessoa"]["vinculo"]["houseHold"][9]["nomeUltimo"]}
		CPF: {api["result"][0]["pessoa"]["vinculo"]["houseHold"][9]["cpf"]}
		'''
		msg = msg + mensagem
	except:
		pass
	if 'Oops, something lost' in msg:
		msg = 'Fodeu'
	bot.reply_to(message,msg)