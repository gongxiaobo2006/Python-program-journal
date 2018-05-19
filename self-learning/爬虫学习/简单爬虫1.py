

import urllib.request  
url='http://www.google.com/'  
def getHtml(url):  
    page=urllib.request.urlopen(url)  
    html=page.read().decode(encoding='utf-8',errors='strict')  
    return html  
print(getHtml(url)) 

