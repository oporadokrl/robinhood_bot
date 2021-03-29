import moviepy.editor as mp
import os,re
from pytube import YouTube 
def download(message,bot):
	print('Download de video do Youtube requisitado por {} {}'.format(message.chat.first_name,message.chat.last_name))
	bot.reply_to(message,'Pedido recebido,realizando processo...')
	url=(message.text).replace('/yt ','').replace('/YT','')
	print(url)
	video = YouTube(url).streams.get_highest_resolution().download(skip_existing=False)
	file = open(video, 'rb')
	bot.send_video(message.chat.id, file, timeout=10000)
	file.close()
	os.remove(video)
def downloadmp3(message,bot):
	print('Download de musica do Youtube requisitado por {} {}'.format(message.chat.first_name,message.chat.last_name))
	bot.reply_to(message,'Pedido recebudo,realizando processo...')
	url=(message.text).replace('/ytmp3 ','')
	print(url)
	file = YouTube(url)
	final = file.streams.filter(only_audio=True)
	final[0].download(output_path="downloads")
	tgt_folder = "downloads"
	for file in [n for n in os.listdir(tgt_folder) if re.search('mp4',n)]:
		full_path = os.path.join(tgt_folder, file)
		output_path = os.path.join(tgt_folder, os.path.splitext(file)[0] + '.mp3')
		clip = mp.AudioFileClip(full_path).subclip(10,)
		clip.write_audiofile(output_path)
	file = open(output_path, 'rb')
	bot.send_audio(message.chat.id, file, timeout=10000)
	file.close()
	os.system('rm -rf downloads')