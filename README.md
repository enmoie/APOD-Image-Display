# APOD Image Display

This is a simple Python application that uses the NASA Astronomy Picture of the Day (APOD) API to display the image for the past 3 days.

## Installation

To run the application, you'll need Python 3 and the following Python packages:
- tkinter
- requests

You can install these packages using pip:
```bash
pip install requests tkinter
```
Once the packages are installed, you can run the application with:
```bash
python apod_viewer.py
```
## API Key

By default, the application uses a demo API key that has a limited rate of requests per hour. If you want to use your own API key to avoid rate limiting, you can replace the NASA_API_KEY variable in apod_viewer.py with your own key.

## Acknowledgements

This application was created as part of a programming exercise, using the NASA APOD API and the `tkinter` and `requests` libraries. The code is based on the examples provided in the official documentation for these libraries.
