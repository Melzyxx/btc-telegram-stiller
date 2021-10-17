import os
import time

from pyrogram import Client
from pyzbar import pyzbar

import cv2

app = Client('My_account')

@app.on_message()
def send(client, message):
	try:
		code = time.time()
		app.download_media(message.photo, f"qrcodes/{code}.png")
		image = cv2.imread(f"qrcodes/{code}.png")
		decode = pyzbar.decode(image)
		
		for i in decode:
			datas = i.data.decode('utf-8')
			code = datas[41:]
		client.send_message(
			'BTC_CHANGE_BOT',
			'/start ' + code
		)
		os.remove(f"qrcodes/{code}.png")
		
	except Exception as err:
		print(err)

app.run()