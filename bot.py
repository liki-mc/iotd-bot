import requests
import pickle

from discord_webhook import DiscordWebhook

webhook_url = ""
with open("secrets/webhook_url.txt", "r") as f:
    webhook_url = f.read().strip()

webhook = DiscordWebhook(url = webhook_url)

already_visited = set()
try:
    with open("visited.pkl", "rb") as f:
        already_visited = pickle.load(f)
except:
    pass

found_url = False
option = ""

while not found_url:
    resp : requests.Response = requests.post("https://integralsforyou.com/Search/getRandomIntegral")
    if resp.status_code != 200:
        continue

    option = resp.text
    if option not in already_visited:
        found_url = True

webhook.add_file(file = requests.get(f"https://i.ytimg.com/vi/{option}/hqdefault.jpg").content, filename = "integral.jpg")
webhook.execute()

already_visited.add(option)
with open("visited.pkl", "wb") as f:
    pickle.dump(already_visited, f)
