from tkinter import *
class SearchWindow:
    def __init__(self):
        self.screen_size = None
        self.root = self.create_root()
        self.root.overrideredirect(1)
        self.input_field = self.create_input()
        self.input_field.pack()



        self.input_field.focus_set()
        self.root.bind("<FocusOut>", self.exit_window)

    def create_root(self):
        root = Tk()
        self.screen_size = {"x":root.winfo_screenwidth(), "y":root.winfo_screenheight()}
        frame = {"w":250,"h":100,"x":0,"y":0}
        frame["y"]=self.screen_size["y"] - frame["h"]
        root.title("SwiftSearch - by NateRiz")
        root.geometry("{}x{}+{}+{}".format(frame["w"], frame["h"],frame["x"],frame["y"]))
        return root

    def create_input(self):
        """
        Creates input field for the root
        :return: input field
        """
        input_field = Entry(self.root)
        input_field.bind("<Return>", self.exit_window)
        input_field.bind("<Escape>", self.exit_window)
        return input_field

    def exit_window(self, event):
        """
        leaves the window when unfocus or completes search.
        :param event: calling event of function
        :return:  None
        """
        self.root.destroy()

    def update(self):
        """
        Updates the mainloop of root
        :return: None
        """
        self.root.mainloop()


#TODO
#window in bottom right
#Animate in
#Animate out only on <Escape>
#picture bg
#default settings ini