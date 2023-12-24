import requests
from bs4 import BeautifulSoup
import csv
def scrap(url, url2, track):
    # Send a GET request to the URL
    response = requests.get(url)

    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")
    title = soup.find_all("h2", {"class": "TextLabel-sc-8kw9oj-0 LyricsHeader__Title-ejidji-0 dddWnX"})
    lyrics = soup.find_all("div", {"class": "Lyrics__Container-sc-1ynbvzw-1 kUgSbL"})
    for br in soup.find_all("br"):
        br.replace_with("\n")
    album = soup.find("a", {"class": "PrimaryAlbum__Title-cuci8p-4 NcWGs"})
    #album = soup.find("a", {"class": "PrimaryAlbum__Title-cuci8p-4 MKFFi"})
    year = album.text[album.text.find("(")+1:album.text.find(")")]
    album = album.text[:album.text.find(" (")]
    response2 = requests.get(url2)

    # Create a BeautifulSoup object to parse the HTML content
    soup2 = BeautifulSoup(response2.content, "html.parser")
    view = soup2.find_all("div", {"class": "chart_row-metadata_element chart_row-metadata_element--large"})
    with open('lyrics.csv', 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Write the title and lyrics to the CSV file
        #writer.writerow([album, title[0].text.replace(" Lyrics", ""), lyrics[0].text.replace("[Verse 1]", "[Verse]").replace("[Verse 2]", "[Verse]"), year, view[track].text.replace(" ", "").replace("\n", "")])
        writer.writerow([album, title[0].text.replace(" Lyrics", ""), lyrics[0].text.replace("[Verse 1]", "[Verse]").replace("[Verse 2]", "[Verse]")  + "\n" + lyrics[1].text.replace("[Verse 1]", "[Verse]").replace("[Verse 2]", "[Verse]"), year, view[track].text.replace(" ", "").replace("\n", "")])

# scrap("https://genius.com/Lany-you-lyrics", "https://genius.com/albums/Lany/Mamas-boy", 0)
# scrap("https://genius.com/Lany-cowboy-in-la-lyrics", "https://genius.com/albums/Lany/Mamas-boy", 1)
scrap("https://genius.com/Lany-heart-wont-let-me-lyrics", "https://genius.com/albums/Lany/Mamas-boy", 2)
scrap("https://genius.com/Lany-i-still-talk-to-jesus-lyrics", "https://genius.com/albums/Lany/Mamas-boy", 4)
scrap("https://genius.com/Lany-if-this-is-the-last-time-lyrics", "https://genius.com/albums/Lany/Mamas-boy", 3)
scrap("https://genius.com/Lany-paper-lyrics", "https://genius.com/albums/Lany/Mamas-boy", 5)
scrap("https://genius.com/Lany-good-guys-lyrics", "https://genius.com/albums/Lany/Mamas-boy", 6)
scrap("https://genius.com/Lany-sharing-you-lyrics", "https://genius.com/albums/Lany/Mamas-boy", 7)
scrap("https://genius.com/Lany-bad-news-lyrics", "https://genius.com/albums/Lany/Mamas-boy", 8)
scrap("https://genius.com/Lany-when-youre-drunk-lyrics", "https://genius.com/albums/Lany/Mamas-boy", 9)
scrap("https://genius.com/Lany-anything-4-u-lyrics", "https://genius.com/albums/Lany/Mamas-boy", 10)
scrap("https://genius.com/Lany-sad-lyrics", "https://genius.com/albums/Lany/Mamas-boy", 11)
scrap("https://genius.com/Lany-what-i-wish-just-one-person-would-say-to-me-lyrics", "https://genius.com/albums/Lany/Mamas-boy", 12)
scrap("https://genius.com/Lany-nobody-else-lyrics", "https://genius.com/albums/Lany/Mamas-boy", 13)

#scrap("", "", 0)
#scrap("", "", 1)
#scrap("", "", 2)
#scrap("", "", 3)
#scrap("", "", 4)
#scrap("", "", 5)
#scrap("", "", 6)
#scrap("", "", 7)
#scrap("", "", 8)
#scrap("", "", 9)
#scrap("", "", 10)
#scrap("", "", 11)
#scrap("", "", 12)
#scrap("", "", 13)
#scrap("", "", 14)