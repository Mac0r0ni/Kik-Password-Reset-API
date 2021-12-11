import requests

class bcolors:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    ENDC = '\033[0m'

url = 'https://KPR-API.stethosayshello.repl.co'
get_emailOrUsername = input(bcolors.GREEN + "Enter the username or email you would like to reset the password for: " + bcolors.ENDC)
print(bcolors.GREEN + "Please wait..." + bcolors.ENDC)
payload = { 'emailOrUsername' : str(get_emailOrUsername) }
res = requests.post(url, data=payload)
result = str(res.content)
result = result[18:-7]
'''
The API returns raw results from ws.kik.com, which tends to have some odd formatting. 
The below 4 lines is just to remove that formatting.
'''
result = result.replace("\n", " ")
result = result.replace("\\", "")
while "  " in result:
  result = result.replace("  ", " ")
print(bcolors.BLUE + result + bcolors.ENDC)
