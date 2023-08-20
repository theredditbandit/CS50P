import sys
import requests
import json

try:
    n = float(sys.argv[1])
except IndexError:
    print("Missing command-line argument")
    sys.exit(1)
except ValueError:
    print("Command-line argument is not a number")
    sys.exit(1)

api_response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
o = api_response.json()
# print(json.dumps(o,indent=4))

value = float(o["bpi"]["USD"]["rate_float"])*n
print(f'${value:,.4f}')