# SwiftSearch
Python 3.x GUI for searching multiple websites quickly without having to load browsers and secondary sites.

This project was made in Python 3.6 and uses Tkinter and Pillow. The purpose of SwiftSearch is to speed up the process of searching your favorite websites without having to open your browser, go to a site, and then enter a query. This can be easily customized to add more websites to your search using the settings.txt. Priorities are also assigned to sites that are searched more frequently in order. This speeds up the searching process even further by suggesting sites you are likely to be searching.


### Adding a site:
In settings.txt, add a dictionary with the following format:_
_
{_
        "site" : "google.com", #shorthand for website you will search for_
        "img" : "twitter.png", #Background image for website : Optimized for 500x200_
        "search" : "https://twitter.com/search?q={}&src=typd", #site's search address. the {} will be replaced by your query_
        "separator" : "%20", #site's specific separator for spaces. (Usually %20, +, -, ...)_
        "priority" : 0 # Incremented each time you visit the site to suggest it faster during the next search. _
}_
