import requests
from bs4 import BeautifulSoup

URL = input("Enter webpage address you want to scrap it : ")

def extract_texts(url):
    res = requests.get(url)
    html_page = res.content
    soup = BeautifulSoup(html_page, 'html.parser')
    text = soup.find_all(text=True)

    output = ''
    blacklist = [
        '[document]',
        'noscript',
        'header',
        'html',
        'meta',
        'head', 
        'input',
        'script',
        # there may be more elements you don't want, such as "style", etc.
    ]

    for t in text:
        if t.parent.name not in blacklist:
            output += '{} '.format(t)


def find_emails(text):
    text = str(text)
    splited_text = text.split(" ")
    output = ''
    for word in splited_text:
        if "@" in word:
            splited_by_at = word.split("@")
            if "." in splited_by_at[1]:
                output += f"{word}\n"
    if output != '': return output
    return None

texts = extract_texts(URL)
emails = find_emails(texts)
print(emails)