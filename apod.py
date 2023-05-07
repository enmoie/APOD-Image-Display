import requests
import datetime
from PIL import Image
from io import BytesIO


def display_apod_images(api_key: str) -> None:
    for days in range(3):
        date = datetime.datetime.now() - datetime.timedelta(days=days+1)
        date_string = date.strftime("%Y-%m-%d")
        url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}&date={date_string}"
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Failed to get APOD data for {date_string}.")
        else:
            data = response.json()
            image_url = data["url"]
            title = data["title"]
            response = requests.get(image_url)
            image_data = response.content
            image = Image.open(BytesIO(image_data))
            print(f"\n{date_string}: {title}")
            image.show()


if __name__ == "__main__":
    api_key = "LxZqA4Fu9dtT6stNEXeoUbU8adXRf4mtXhBuMOKC"
    display_apod_images(api_key)
