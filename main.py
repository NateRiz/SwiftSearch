from SearchWindow import SearchWindow
from Website import Website
from json import load
from json import dump
import os
def main():
    websites = list()
    try:
        with open(os.path.abspath("Settings.txt"),"r") as settings:
            web_json = load(settings)
            for w in web_json:
                site = Website(w["site"], w["search"], w["img"], w["separator"], w["priority"])
                websites.append(site)

    except FileNotFoundError as E:
        print("Settings.txt could not be opened:\n", E)
        return


    search = SearchWindow(websites)
    chosen_site = search.update() #call main loop
    for i in web_json:
        if i["site"] == chosen_site:
            i["priority"]+=1

    try:
        with open(os.path.abspath("Settings.txt"), "w") as settings:
            dump(web_json, settings, indent=4,sort_keys=True )


    except FileNotFoundError:
        print("settings.txt not found")
        return







if __name__ == "__main__":
    main()