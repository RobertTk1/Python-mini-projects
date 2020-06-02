from tkinter import *
from PIL import ImageTk, Image
import requests
import json
root = Tk()
root.title('Weather App')
root.iconbitmap("iconx.ico")
root.geometry('200x70')


zipcode = Entry(root)
zipcode.pack()


def ziplook():
    try:
        api_request = requests.get(
            "http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode.get() + "&distance=20&API_KEY=4E6599BF-F962-42BD-9FDB-933B03C99D6D")
        api = json.loads(api_request.content)
        city = api[0]['ReportingArea']
        quality = api[0]['AQI']
        category =api[0]['Category']['Name']
        mylabel = Label(root, text='City ' + city + ' Air quality ' + str(quality) + ' ' + category, font=('Helvetica', 10), bg='Green')
        mylabel.pack()

    except Exception as e:
        api = "Error"

zip_btn = Button(root, text="Submit", command= ziplook)
zip_btn.pack()


root.mainloop()
