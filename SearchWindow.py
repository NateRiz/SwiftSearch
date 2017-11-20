from tkinter import *
import time
class SearchWindow:
    def __init__(self, websites):
        self.screen_size = None
        self.all_websites = websites
        self.filtered_websites = list(websites)
        self.root = self.create_root()
        self.hidden_search=""
        self.suggestion = StringVar()
        self.input_field = self.create_input()

        self.input_field.focus_set()
        self.root.bind("<FocusOut>",self.exit_window)
        self.animate_in()


    def animate_in(self, begin = time.time(), end = time.time()+.3):
        """

        :param begin: time when first called
        :param end: time when first called + total time of aniamtion
        :return: None
        """
        final_alpha = .8
        alpha = (final_alpha/.3) * (time.time() - begin)
        self.root.attributes("-alpha",alpha)
        if time.time() <= end:
            self.root.after(25, self.animate_in, begin, end)
        else:
            self.root.attributes("-alpha", final_alpha)

    def create_root(self):
        root = Tk()
        self.screen_size = {"x":root.winfo_screenwidth(), "y":root.winfo_screenheight()}
        frame = {"w":500,"h":200,"x":0,"y":0}
        frame["y"]=self.screen_size["y"] - frame["h"]
        root.title("SwiftSearch - by NateRiz")
        root.geometry("{}x{}+{}+{}".format(frame["w"], frame["h"],frame["x"],frame["y"]))
        root.overrideredirect(1)
        return root

    def create_input(self):
        """
        Creates input field for the root
        :return: input field
        """
        input_field =Entry(self.root, width = 32, textvariable = self.suggestion, state = "readonly")
        self.suggestion.set("Type a website: eg: facebook.com")
        input_field.bind("<Return>", self.exit_window)
        input_field.bind("<Escape>", self.exit_window)
        input_field.bind("<Key>",  self.key_press)
        input_field.place(relx=0.5, rely=0.5, anchor=CENTER)
        return input_field

    def key_press(self, event):
        """
        User has entered a key
        backspace will check if empty  -> return to default
        letters will update text.
        :param event: calling event
        :return: None
        """
        if event.keysym == "BackSpace":
            self.hidden_search=self.hidden_search[0:-1]
        else:
            self.hidden_search=self.hidden_search+event.char

        self.update_search()
        self.input_field.select_range(len(self.hidden_search),END)
    def update_search(self):
        """
        :param letter: letter being typed in.
        :return: None
        """
        new_filter = list()
        max_priority = -1
        suggested = ""

        for w in self.filtered_websites:
            if w.website.startswith(self.hidden_search):
                new_filter.append(w)
                if w.priority > max_priority:
                    max_priority = w.priority
                    suggested = w.website

        self.suggestion.set(suggested)


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
#Search
