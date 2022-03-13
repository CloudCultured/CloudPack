""" MullinsWarrenFinalProject.py - intended to be a base level communtiy app where members can see merch,
        leave suggestions, check the stream schedule, and find the url's to social media pages.
    Waren Mullins 03/13/2022
    CloudPack: (superclass) main application window
"""
from breezypythongui import EasyFrame
from tkinter import *
from tkinter import ttk
from tkinter.font import Font
class CloudPack(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title = 'The Cloud Pack') # Sets up initial window
        self.setResizable(True);
        imageLabel=self.addLabel(text ="",row=0,column=0,
                      sticky="NSEW")
        textLabel=self.addLabel(text ="Welcome To The Cloud Pack!!!\nBe Kind!\nBe Better!\nBe YOU!!",row=1,column=0,
                      sticky="NSEW")
        # Load the image file and associate it with the image label
        self.image=PhotoImage(file = r"C:\Users\warre\OneDrive\Pictures\TwitchBanner.png") 
        imageLabel["image"]=self.image
        # Set the font and color of the caption
        font = Font(family="Verdana",size=26,slant="italic")
        textLabel["font"] = font
        textLabel["foreground"]="blue"
        # Adds button panel and puts buttons on it in position
        buttonPanel=self.addPanel(row=3, column = 0, columnspan=3,
                       background="blue")
        buttonPanel.addButton(text = "Schedule", row = 4, column = 0,
                    command = self.getSchedule)
        buttonPanel.addButton(text = "Merch", row = 4, column = 1,
                    command = self.getMerch)
        buttonPanel.addButton(text = "Socials", row = 4, column = 2,
                    command = self.getSocials)
        buttonPanel.addButton(text = "Suggestions", row = 4, column = 3,
                    command = self.getSuggestions)
    def getSchedule(self): # Command to pull up schedule
        self.messageBox(title = "Schedule",
                        message = "Mon-Fri: 7PM-12PM \nSat: 7PM-2AM",
                        width=20,
                        height=1)
    def getMerch(self): # Command to pull up picture of merch(only a t-shirt right now)
        merch=Toplevel()
        merch.minsize(width=200, height=250)
        merch.title("Merch!!")
        canvas = Canvas(merch, width=400, height=600)
        canvas.pack()
        
        self.img=PhotoImage(file=r"C:\Users\warre\OneDrive\Pictures\Happy_cloud.png")
        canvas.create_image(200,400,image=self.img)
        
                
    def getSocials(self): # Command to pull up social media links
        self.messageBox(title = "Social Media links",
                        message = "Twitter: https://twitter.com/CloudCultured\n\nInstgram: https://www.instagram.com/cloudcultured/\n\nTikTok: https://www.tiktok.com/@cloudcultured?lang=en  ",
                        width=55,
                        height=8)
    def getSuggestions(self): # Command to pull up promterbox to accept user input suggestions
        ws = Tk()
        ws.title("Suggestions")
        ws.geometry('400x300')
        ws['bg'] = '#ffbf00'
        Label(ws, text='Help me be better!', pady=20, bg='#ffbf00').pack()
        

        def printSuggestion(): # Command to print user input under button
            u_suggestion = suggestion.get()
            Label(ws, text=f'{u_suggestion}', pady=20, bg='#ffbf00').pack()

        suggestion = Entry(ws)
        suggestion.pack(pady=30)
        # Button to enter suggestion
        Button(
            ws,
            text="Enter Suggestion", 
            padx=10, 
            pady=5,
            command=printSuggestion
            ).pack()

        ws.mainloop()

                


CloudPack().mainloop()
