import os

api_id = os.environ.get("API_ID", "23237831")
api_hash = os.environ.get("API_HASH", "017dc661ca1432ac2fe5ecb62499d88f")
bot_token = os.environ.get("BOT_TOKEN", "6216840269:AAFNzApyRlXuZ94T3UZgd-XqNun2mA40kJU")

auth_users_str = os.environ.get("AUTH_USERS", "")
auth_users = []
if auth_users_str:
    auth_users = [int(user_id) for user_id in auth_users_str.split(",")]
else:
    auth_users=[6103594386]
