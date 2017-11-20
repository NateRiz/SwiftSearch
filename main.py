from SearchWindow import SearchWindow
from Website import Website
from json import load
def main():
    websites = get_websites()
    if not websites:
        return
    search = SearchWindow(websites)
    search.update()

def get_websites() -> list():
    websites = list()
    try:
        with open("Settings.txt","r") as settings:
            web_json = load(settings)
            for w in web_json:
                site = Website(w["site"], w["search"], w["img"], w["separator"], w["priority"])
                websites.append(site)

    except FileNotFoundError as E:
        print("Settings.txt could not be opened:\n", E)

    return websites

if __name__ == "__main__":
    main()