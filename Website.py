from tkinter import PhotoImage
class Website:
    def __init__(self, website, search, picture, separator, priority=-1):
        self.website = website
        self.search = search
        self.picture = picture
        self.separator = separator
        self.priority = priority