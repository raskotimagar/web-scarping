# from urllib.request import urlopen

# url = "https://www.linkedin.com/feed/"
# page = urlopen(url)
# html_bytes = page.read()
# html = html_bytes.decode("utf-8")
# # print(html)
# title_index = html.find("<title>")
# start_index = title_index + len("<title>")
# end_index = html.find("</title>")
# title = html[start_index:end_index]
# print(title)




import re
from urllib.request import urlopen
url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode('utf-8')

pattern = "<title.*?>.*?</title.*?>"
match_results = re.search(pattern, html, re.IGNORECASE)
title = match_results.group()
title = re.sub("<.*?>", "", title) # remove html tags
print(title)