import requests
import random

apikey = ""

def askAPI(word):
    if word in ["are", "is", "was", "a", "or", "has", "his"] or word[0].isupper():
        return {'noun': {'syn': [word]}}

    res = requests.get("https://words.bighugelabs.com/api/2/" + apikey + "/" + word + "/json")
    if res.status_code != 200:
        return {'noun': {'syn': [word]}}
    #print(res.json())
    return res.json()


def ask():
    print("Enter a word or phrase")

    # create 2 phrases, 1 will always be first word only, 2 will be random word
    phrase1 = ""
    phrase2 = ""

    inputphrase = input()
    for r in inputphrase.split(" "):
        jsonResponse = askAPI(r.replace(" ", ""))
        #print(jsonResponse)
        phrase1 += list(jsonResponse.values())[0]['syn'][0] + " "
        phrase2 += list(jsonResponse.values())[0]['syn'][random.randrange(len(list(jsonResponse.values())[0]['syn']))] + " "
    print(phrase1)
    print(phrase2)
    print("\n")

if __name__ == "__main__":
    while(True):
        ask()
