import requests
from bs4 import BeautifulSoup
import re
import keyword
# import video as v

COMPANIES = ["NordVPN", "SurfShark", ]
#link for all sponsorship companies: https://youtube.fandom.com/wiki/Sponsorships#cite_note-2

def comp_link(link):
    """
    -------------------------------------------------------
    checks to see if value is found in COMPANIES
    Use: boolean = comp_link(string)
    -------------------------------------------------------
    Parameters:
        link - string that contains URL
    Returns:
        True if the link contains a sponsorship company, false if otherwise
    -------------------------------------------------------
    """
    comp_true = False
    for i in COMPANIES:
        if i.lower() in link:
            comp_true = True

    return comp_true


URL = "https://www.youtube.com/watch?v=pjSMl3tfhYo"
page = requests.get(URL)


soup = BeautifulSoup(page.content, "html.parser")
meta_tags = soup.find_all('meta') #get metadata from page

#iterate through the meta tags and print out the name and content

for t in meta_tags:
    name = t.get('name')
    content = t.get('content')
    print(f'{name}: {content}')

# results = soup.find(id="bottom-row")
# link_elements = results.find_all("div", class_="style-scope ytd-watch-metadata")

# for i in link_elements:
#     print(i)"
# for link in soup.find_all('id=', limit=10):
#     print(link.get('id=secondary-info'))
#     print
# for link in soup.find_all('id=page-manager'):
#     print(link.get('class'))

#     # print(soup.get("a", string="redir_token"))
# # print(results.prettify())
# # print(page.text)

# pattern = re.compile('(?<=shortDescription":").*(?=","isCrawlable)')
# description = pattern.findall(str(soup))[0].replace('\\n','\n')
# # print(description)

# description_list = []

# for i in description.split():
#     # if "https" in i
#     #     # if
#     #     description_list.append(i)
#     print(i + " " + str(comp_link(i)))
# print(description_list)
