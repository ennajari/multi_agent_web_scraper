from bs4 import BeautifulSoup

def parse_page(content):
    soup = BeautifulSoup(content, 'html.parser')
    data = []
    quotes = soup.find_all("div", class_="quote")
    for q in quotes:
        text = q.find("span", class_="text").text.strip()
        author = q.find("small", class_="author").text.strip()
        data.append({'quote': text, 'author': author})
    return data