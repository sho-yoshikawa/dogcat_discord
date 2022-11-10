import discord
import requests
import json
from passwd import TOKEN_ID, CHANNEL_ID

DOG_API = "https://dog.ceo/api/breeds/image/random"
CAT_API = "https://api.thecatapi.com/v1/images/search"

client = discord.Client(intents=discord.Intents.all())

def save_image(url):
	response = requests.get(url)
	image = response.content
	with open("image.png", "wb") as img:
		img.write(image)

def get_dog_image():
	res = requests.get(DOG_API)
	data = json.loads(res.text)
	image_url = data["message"]
	return image_url

def get_cat_image():
	res = requests.get(CAT_API)
	data = json.loads(res.text)
	image_url = data[0]["url"]
	return image_url


@client.event
async def on_ready():
		print("start up... ")

@client.event
async def on_message(message):
	if message.author.bot:
		return
	channel = client.get_channel(CHANNEL_ID)
	if message.content == "にゃん":
		image_url = get_cat_image()
		save_image(image_url)
		file = discord.File("image.png", filename="cat.png")
		await message.channel.send(file=file)
	elif message.content == "わふ":
		image_url = get_dog_image()
		save_image(image_url)
		file = discord.File("image.png", filename="dog.png")
		await message.channel.send(file=file)


client.run(TOKEN_ID)
