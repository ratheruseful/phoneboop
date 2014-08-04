import requests
URL = 'http://IP_ADDRESS/phone_dumps/all.txt'

response  = requests.get(URL)
raw_data = response.text

def isonline(name, surname):
    for line in raw_data.splitlines():
        tokens = line.split()
        if tokens[1] == name and tokens[2] == surname and tokens[5] == "AVAIL":
            return True
    return False

    
print(isonline("Oliver", "Gross"))
print(isonline("Walter", "Lenuzza"))


