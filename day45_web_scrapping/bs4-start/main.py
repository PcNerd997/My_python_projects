from bs4 import BeautifulSoup

with open("./bs4-start/website.html") as html_file:
    content = html_file


soup = BeautifulSoup(markup= content, parse_only="html.parser")
print(soup)