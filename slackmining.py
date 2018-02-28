import requests, json
from slackclient import SlackClient

from pymongo import MongoClient

from config import *

client = MongoClient()
db = getattr(client, DATABASE_NAME)

slack_client = SlackClient('xoxp-322027627588-321396540064-321397039120-8b0d2dc7e29b8e127b13e32a10d3f17d')


slack_messages = slack_client.api_call("channels.history", channel='C9FEMSVTK', pretty=1)


print("messages of the slack.")


for message in slack_messages['messages']:
	print(message)

