#!/usr/bin/env python3

# The below Python script shows one possible method to return the cookie from a site that supports cookies.

import requests
from webbrowser import open
# targetsite = input("Enter target site:") # Uncomment this to accept user input target site
targetsite = "http://www.whatarecookies.com/cookietest.asp" # Comment this out if you're using the line above
response = requests.get(targetsite)
cookie = response.cookies

def bringforthcookiemonster(): # Because why not!
    print('''

              .---. .---.
             :     : o   :    me want cookie!
         _..-:   o :     :-.._    /
     .-''  '  `---' `---' "   ``-.
   .'   "   '  "  .    "  . '  "  `.
  :   '.---.,,.,...,.,.,.,..---.  ' ;
  `. " `.                     .' " .'
   `.  '`.                   .' ' .'
    `.    `-._           _.-' "  .'  .----.
      `. "    '"--...--"'  . ' .'  .'  o   `.

        ''')

bringforthcookiemonster()
print("Target site is " + targetsite)
print(cookie)

def generate_html(title, content):
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>{title}</title>
    </head>
    <body>
        {content}
    </body>
    </html>
    """
    # Correct indentation for the "with" statement
    with open("index.html", "w") as file:
        file.write(html_content)

def open_html():
    open("index.html")

title = "My Dynamic HTML Page"
content = "<h1>This is a page generated by Python!</h1>"

generate_html(title, content)
open_html()
# Add here some code to make this script perform the following:
# - Send the cookie back to the site and receive a HTTP response
# - Generate a .html file to capture the contents of the HTTP response
# - Open it with Firefox
#
# Stretch Goal
# - Give Cookie Monster hands