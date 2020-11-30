from tkinter import *
import tkinter.font as tkFont

class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.titlefont = tkFont.Font(family="Arial", size=20, slant="italic")
        self.buttonfont = tkFont.Font(family="Arial", size=18)
        
        self.theCanvas = Canvas(self, width=600,height=400, bg="#AAAAFF")
        self.theCanvas.grid(row=1, column=0)
        
        woodBackground = PhotoImage(file = "wood.png") # convert the pictures into PhotoIMages
        self.theCanvas.create_image(300,200,image=woodBackground)
        
        b1Image =  PhotoImage(file = "button1.png") 
        b2Image =  PhotoImage(file = "button2.png")
        b1ID = self.theCanvas.create_image(300,100,image=b1Image)  # Draw them on the canvas and remember their ID number
        b2ID = self.theCanvas.create_image(300,300,image=b2Image)
        
        self.theCanvas.tag_bind(b1ID, "<Button-1>", self.b1Clicked)
        self.theCanvas.tag_bind(b2ID, "<Button-1>", self.b2Clicked)
        
        self.mainloop() # this is needed to start checking for clicks
        
    def b1Clicked(self,e):
        print("Button 1 pressed")
        print(e)
        
    def b2Clicked(self,e):
        print("Button 2 pressed")
        print(e)

if __name__ == "__main__":
    app = App()