import requests
import hvac
import os
from random import randint
# The token is store at:
# secret/applications/scrapeops/tokens

vault_addr = os.getenv("VAULT_ADDR")
vault_token = os.getenv("VAULT_TOKEN")

client = hvac.Client(url=vault_addr, token=vault_token)
token = client.secrets.kv.v2.read_secret_version("applications/scrapeops/tokens", raise_on_deleted_version=False)['data']['data']["fake_headers_api_token"]
endpoint = "http://headers.scrapeops.io/v1/browser-headers"
params = {
    'api_key':token,
    'num_results': 2
}
browser_headers = requests.get(url=endpoint, params=params).json()
for agent in browser_headers['result']:
    print(agent)
headers =  browser_headers['result'][randint(0, len(browser_headers)-1)]
response = requests.get(url='https://books.toscrape.com', headers=headers)
