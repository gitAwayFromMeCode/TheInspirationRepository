import requests

def quote_of_the_day():
    r = requests.get('https://quotes.rest/qod?language=en')
    #print(requests.get('https://quotes.rest/qod?language=en').json()["contents"]["quotes"][0])
    data = r.json()
    quote_content = data["contents"]["quotes"][0]["quote"]
    quote_author = data["contents"]["quotes"][0]["author"]
    print("{} ~ {}".format(quote_content, quote_author))
    return quote_content, quote_author

if '__name__' == '__main__':
    quote_of_the_day()

