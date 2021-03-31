# RobinHood Bot
![RobinHood Bot](https://raw.githubusercontent.com/oporadokrl/robinhood_bot/master/robinhood.png)

Um bot que entrega aos pobres o que os ricos obtém facilmente

## Instalação
1. Clonar o repositório

$ git clone https://github.com/oporadokrl/robinhood_bot.git

2. Clonar o repositório de dependência

$ git clone https://github.com/eternnoir/pyTelegramBotAPI

3. Mover os arquivos de um repositório para outro

$ mv ./pyTelegramBotAPI/* ./robinhood_bot

4. Inserir o token

Troque a seguinte linha do arquivo "token" :
```
{COLOQUE O SEU TOKEN AQUI}
```
Pelo seu token do telegram

5. Executar

$ python3 main.py

6. Adaptar ao seu uso :)

## Obtendo o token do telegram

Se você não tem um token para o seu bot,siga os passos abaixo:
1. Entre no seu telegram
2. Procure por @BotFather
3. Clique em start/iniciar
4. Mande um /newbot
5. Defina o nome do seu bot
6. Mande um /token
7. Pronto,só copiar o código que ele te der e seguir as instruções acima.

## Instalando as dependências
### Arch Linux
```
# pacman -Syyu python git
```
### Debian/Ubuntu
```
# apt update && apt upgrade
# apt install python git
```
### SUSE
```
# zypper install python git
```
