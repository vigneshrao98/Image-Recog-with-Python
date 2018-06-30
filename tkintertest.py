#importing required packages
from tkinter import *
from PIL import Image
from PIL import ImageTk
from tkinter import filedialog
#from getinfo import get_pred
from clarifai.rest import ClarifaiApp
import json
app=ClarifaiApp()
model=app.models.get('general-v1.3')
def get_pred(img_path):
    response = model.predict_by_filename(filename=img_path)
    #data=json.load(response)
    result=response['outputs'][0]['data']['concepts'][0]['name']
    return result
   
   
#set environment varible[clarifai_api_key] in clarifai to your clarifai key
#func slect image for locating and selecting image
def select_image():
    # grab a reference to 1 image panel, panel2 to be decided
    global panelA, panelB

   
    # open a file chooser dialog and allow the user to select an input image
    path = filedialog.askopenfilename()
    if len(path)>0:
        img = ImageTk.PhotoImage(Image.open(path))
        pred=get_pred(path)
        
        if panelA is None or panelB is None:
            panelA = Label(image=img)
            panelA.image = img
            panelA.pack(side="left", padx=10, pady=10)
            panelB = Text(root, height=2, width=30)
            panelB.pack(side="right", padx=10, pady=10)
            panelB.insert(END,pred)
        else:
            panelA.configure(image=img)
            panelA.image = img


root = Tk()
panelA = None
panelB = None

btn = Button(root, text="Select an image", command=select_image)
btn.pack(side="bottom", fill="both", expand="yes", padx="10", pady="10")


root.mainloop()