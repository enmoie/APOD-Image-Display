from io import BytesIO
import datetime
from PIL import ImageTk, Image
import requests
import tkinter as tk

NASA_API_KEY = "LxZqA4Fu9dtT6stNEXeoUbU8adXRf4mtXhBuMOKC"


class ApodViewer(tk.Frame):
    """
    A GUI application that displays the Astronomy Picture of the Day (APOD) from NASA.

    Attributes:
        master (tk.Tk): The root Tkinter window.
        image_labels (list): A list of three Tkinter Labels that display the APOD images.
        quit_button (tk.Button): A Tkinter Button that closes the window.
    """

    def __init__(self, master=None):
        """
        Initializes the ApodViewer object.

        Args:
            master (tk.Tk): The root Tkinter window (default is None).
        """
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        """
        Creates the widgets for the GUI.
        """
        self.image_labels = []
        for i in range(3):
            label = tk.Label(self)
            label.pack(side="left")
            self.image_labels.append(label)

    def load_images(self):
        """
        Loads the APOD images from the NASA API and displays them in the GUI.
        """
        image_url = []
        for days in range(3):
            date = datetime.datetime.now() - datetime.timedelta(days=days+1)
            date_string = date.strftime("%Y-%m-%d")
            NASA_APOD_URL = f"https://api.nasa.gov/planetary/apod?api_key={NASA_API_KEY}&date={date_string}"
            response = requests.get(NASA_APOD_URL)
            if response.status_code == 200:
                apod_data = response.json()
                image_url.append(apod_data["url"])
        for i, url in enumerate(image_url):
            response = requests.get(url)
            if response.status_code == 200:
                img = Image.open(BytesIO(response.content))
                img = img.resize((300, 300), Image.ANTIALIAS)
                photo = ImageTk.PhotoImage(img)
                self.image_labels[i].configure(image=photo)
                self.image_labels[i].image = photo

    def run(self):
        """
        Runs the GUI application.
        """
        self.load_images()
        self.master.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = ApodViewer(master=root)
    app.run()
