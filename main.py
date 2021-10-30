import requests
from threading import Thread
import os
import bs4
from sys import platform

os_type = platform


def download_for_windows(image_link):  # For windows machine
    print(image_link)


def download_for_linux(image_link):  # For linux machine
    os.system(f"wget {s[6:-2]}")


if __name__ == "__main__":
    link = input("Paste link :: ")
    link = "https://wall.alphacoders.com/tag/noelle-(genshin-impact)-wallpapers"
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
                        link_of_photo = s[6:-2]
                        print(link_of_photo)
                        print(os_type == "win32")
                        if os_type == "win32":  # FOR WINDOWS MACHINE
                            new_thread = Thread(
                                target=download_for_windows, args=[link_of_photo]
                            )
                        else:  # FOR LINUX MACHINE
                            new_thread = Thread(
                                target=download_for_linux, args=[link_of_photo]
                            )
                    break
