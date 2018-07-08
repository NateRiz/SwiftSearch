from tkinter import *
from PIL import ImageTk
from PIL import Image
import time
import os
import webbrowser

class SearchWindow:
    def __init__(self, websites):
        self.screen_size = None
        self.all_websites = websites
        self.filtered_websites = list(websites)
        self.root = self.create_root()
        self.img = None
        self.background = Label(self.root, image=self.img, bg = "black")
        self.background.place(x=0, y=0, relwidth=1, relheight=1)
        self.hidden_search=""
        self.suggestion = StringVar()
        self.suggested_website = None
        self.input_field = self.create_web_input()


        self.search_query = StringVar()
        self.search_field= None

        self.root.bind("<FocusOut>",self.exit_window)

    def create_root(self):
        """
        Creates root window
        :return: root of the window
        """
        root = Tk()
        self.screen_size = {"x":root.winfo_screenwidth(), "y":root.winfo_screenheight()}
        frame = {"w":500,"h":200,"x":0,"y":0}
        frame["y"]=int(self.screen_size["y"] - frame["h"])
        root.title("SwiftSearch - by NateRiz")
        root.geometry("{}x{}+{}+{}".format(frame["w"], frame["h"],frame["x"],frame["y"]))
        root.overrideredirect(1)
        return root

    def create_web_input(self):
        """
        Creates input field for the root
        :return: input field
        """
        input_field =Entry(self.root, width = 32, textvariable = self.suggestion, state = "readonly")
        self.suggestion.set("Search...")
        input_field.bind("<Return>", lambda redirect:
                                self.transition_input_fields() if self.suggested_website else None)
        input_field.bind("<Tab>", lambda redirect:
                                self.transition_input_fields() if self.suggested_website else None)

        input_field.bind("<Escape>",lambda event: self.animate_out(time.time(), time.time()+.3))
        input_field.bind("<Key>",  self.key_press)
        input_field.place(relx = .50, rely = .80, anchor=CENTER)
        input_field.focus_set()

        return input_field

    def create_search_input(self):
        """
        Creates input field for search query
        :return: input field
        """
        input_field =Entry(self.root, width = 32, textvariable = self.search_query)
        input_field.bind("<Return>", lambda redirect:
                                self.search_site() if self.search_query else None)
        input_field.bind("<Tab>", lambda redirect:
                                self.search_site() if self.search_query else None)

        input_field.bind("<Escape>",lambda event: self.animate_out(time.time(), time.time()+.3))
        input_field.place(relx = 1.5, rely = .80, anchor=CENTER)
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

        self.update_filter()
        if self.suggested_website:
            self.suggestion.set(self.suggested_website.website)
        else:
            self.suggestion.set(self.hidden_search)


        self.input_field.select_range(len(self.hidden_search),END)

    def update_filter(self):
        """
        updates current filter of matching websites.
        Updates image of background if search found.
        :return: None
        """
        new_filter = list()
        max_priority = -1
        self.suggested_website = None
        for w in self.filtered_websites:
            if w.website.startswith(self.hidden_search):
                new_filter.append(w)
                if w.priority > max_priority:
                    max_priority = w.priority
                    self.suggested_website = w
        if self.suggested_website:
            path = os.path.join(os.getcwd(), "assets",self.suggested_website.picture)
            img = Image.open(path)
            img = img.resize((self.root.winfo_width(),self.root.winfo_height()), Image.ANTIALIAS)
            img.putalpha(180)
            self.img = ImageTk.PhotoImage(img)
            self.background.configure(image = self.img)
        else:
            self.background.configure(image = "")

    def search_site(self):
        """
        opens browser with whatever is in the suggestion
        :param event: None
        :return:None
        """
        if self.suggested_website and self.search_query.get():
            site = self.suggested_website.search.format(self.search_query.get()
                                                        .replace(" ", self.suggested_website.separator))
            webbrowser.open(site)
            self.exit_window(None)

    def exit_window(self, event):
        """
        leaves the window when unfocus or completes search.
        :param event: calling event of function
        :return:  None
        """
        self.root.destroy()

    ###############################
    #Animations
    def animate_in(self, begin, end):
        """

        :param begin: time when first called
        :param end: time when first called + total time of animation
        :return: None
        """
        final_alpha = .8
        alpha = (final_alpha/.3) * (time.time() - begin)
        self.root.attributes("-alpha",alpha)
        if time.time() <= end:
            self.root.after(25, self.animate_in, begin, end)
        else:
            self.root.attributes("-alpha", final_alpha)

    def animate_out(self, begin, end):
        """
        animates window out on escape
        :param event: calling event. Escape only
        :return: None
        """
        begin_alpha = .8
        alpha = begin_alpha - (begin_alpha/.3) * (time.time() - begin)
        self.root.attributes("-alpha",alpha)
        if time.time() <= end:
            self.root.after(25, self.animate_out, begin, end)
        else:
            self.root.attributes("-alpha", alpha)
            self.exit_window(None)

    def transition_input_fields(self, begin=None, end=None):
        """
        pushes input out of screen for search input.
        :return:None
        """
        TRANSITION_TIME = .2
        if self.search_field == None:
            self.search_field = self.create_search_input()

        if not begin or not end:
            begin = time.time()
            end = time.time() + TRANSITION_TIME

        multiplier = (time.time()-begin) / TRANSITION_TIME #0 -> 1.0

        if time.time() <= end:
            self.root.after(25, self.transition_input_fields, begin, end)
            self.input_field.place_configure(relx = .5 - multiplier)
            self.search_field.place_configure(relx = 1.5 - multiplier)

        else:
            self.input_field.destroy()
            self.search_field.focus()
            self.search_field.place_configure(relx=.5)
    #End Animaitons
    ###############################

    def update(self):
        """
        Updates the mainloop of root
        :return: None
        """
        self.animate_in(time.time(), time.time()+.3)
        self.root.mainloop()
        if self.suggested_website:
            return self.suggested_website.website




#TODO
#Animate out only on <Escape>
