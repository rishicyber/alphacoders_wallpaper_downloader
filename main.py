import requests

import os
import bs4


if __name__ == "__main__":
    link = "https://wall.alphacoders.com/tag/noelle-(genshin-impact)-wallpapers"

    link = input("Paste link :: ")
    total_pages = int(input("Enter no of pages (Each page contain 30 imaages): "))

    page = 1

    while page <= total_pages:
        print((link + f"&page={page}"))

        res = requests.get((link + f"?page={page}"))
        page += 1

        with open("index.txt", "w+") as fh:
            fh.write(res.text)

        images_number_list = []

        hand = open("index.txt", "r")
        for line in hand:
            for word in line.strip().split():
                if word.startswith("data-id"):
                    images_number_list.append(word[9:-1])

        print(images_number_list)

        for image_number in images_number_list:
            res_2 = requests.get(
                f"https://wall.alphacoders.com/big.php?i={image_number}"
            )
            soup = bs4.BeautifulSoup(res_2.text, "html.parser")
            elments = soup.select("#page_container > div.center.img-container-desktop")
            for s in str(elments[0]).split():
                for ss in s:
                    if s.startswith("href"):
                        # os.system(f"wget {s[6:-2]}")
                        link_of_photo = s[6:-2]
                        print(link_of_photo)
                    break
