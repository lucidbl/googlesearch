import requests,re
word = input("Word to search: ")
def UnistavacVixovogAnusa(raw_html):
    cleantext = re.sub(re.compile(r'<.*?>'), '', raw_html)
    return cleantext
resp=requests.get(f"http://en.wikipedia.org/w/api.php?action=query&list=search&srsearch={word}&format=json")
print(UnistavacVixovogAnusa(resp.json()["query"]["search"][0]["snippet"]))
