import webbrowser
url=input('Query:')
use=url.replace(' ','+')
print(use)
webbrowser.open_new('www.google.com/search?&q='+use)