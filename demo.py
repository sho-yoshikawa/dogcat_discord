import requests
import json

DOG_API = "https://api.thecatapi.com/v1/images/search"

def get_dog_image():
	res = requests.get(DOG_API)
	data = json.loads(res.text)
	image_url = data
	print(data)
	return image_url

get_dog_image()
