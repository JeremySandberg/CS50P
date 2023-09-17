import sys
import requests

if len(sys.argv) == 1:
    sys.exit("Missing command-line argument")

try:
    amount = float(sys.argv[1])
except:
    sys.exit("Command-line argument is not a number")

try:
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    json = r.json()
except requests.RequestException:
    sys.exit("Request failed")

value = float(json["bpi"]["USD"]["rate"].replace(",",""))*amount
print(f"${value:,.4f}")