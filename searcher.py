import requests,re
word = input("Word to search: ")
def ilovevany(raw_html):
    cleantext = re.sub(re.compile(r'<.*?>'), '', raw_html)
    return cleantext
resp=requests.get(f"http://en.wikipedia.org/w/api.php?action=query&list=search&srsearch={word}&format=json")
print(ilovevany(resp.json()["query"]["search"][0]["snippet"]))
