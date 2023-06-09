import requests
from bs4 import BeautifulSoup

user_input = input("Enter the year you want to travel to, YYYY-MM-DD: ")
billboard_url = f"https://www.billboard.com/charts/hot-100/{user_input}"

respons = requests.get(url = billboard_url)
respons.raise_for_status()
billboard_html = respons.text

soup = BeautifulSoup(billboard_html, "html.parser")
songs_extract = soup.select("li ul li h3")
for  song in songs_extract:
    print(song.getText())
# all_song = [song.getText().strip() for song in songs_extract]
# print(all_song)


# all_songs_title = [songs.getText().strip(" ") for songs in all_top_songs]
# print(all_top_songs)
