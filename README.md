# SwiftSearch
Python 3.x minimal GUI for searching any website quickly without having to navigate through multiple URLs. 

This project was made in Python 3.6 and uses Tkinter and Pillow. The purpose of SwiftSearch is to speed up the process of searching your favorite websites without having to open your browser, go to a site, and then enter a query. This can be easily customized to add more websites to your search using the settings.txt. Priorities are also assigned to sites that are searched more frequently in order. This speeds up the searching process even further by suggesting sites you are likely to be searching.

![Preview](https://thumbs.gfycat.com/KaleidoscopicThickBassethound-size_restricted.gif)



### Adding a site:
In settings.txt, add a dictionary with the following format:  
  
{  
        "site" : "google.com", #shorthand for website you will search for  
        "img" : "twitter.png", #Background image for website : Optimized for 500x200  
        "search" : "https://twitter.com/search?q={}&src=typd", #site's search address. the {} will be replaced by your query  
        "separator" : "%20", #site's specific separator for spaces. (Usually %20, +, -, ...)  
        "priority" : 0 # Incremented each time you visit the site to suggest it faster during the next search.   
}  
