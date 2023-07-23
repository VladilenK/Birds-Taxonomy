from bs4 import BeautifulSoup
import requests


# HTML From Website
url = "https://www.newegg.ca/gigabyte-geforce-rtx-3080-ti-gv-n308tgaming-oc-12gd/p/N82E16814932436?Description=3080&cm_re=3080-_-14-932-436-_-Product"
url = "https://www.newegg.com/p/14F-00HG-00003?Description=PC%208%20Double-Sided%20Over-the-Head%20USB%20Headset&cm_re=PC_8%20Double-Sided%20Over-the-Head%20USB%20Headset-_-9SIBBN9JU34825-_-Product"
url = "https://species.wikimedia.org/wiki/Chroicocephalus_ridibundus"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

occurences = doc.find_all(string="Chroicocephalus ridibundus")
occurences = doc.find_all(["span"], lang="en" )
occurences = doc.find_all(class_="mw-page-title-main")
occurences = doc.find_all(["span"], limit=3 )
for occ in occurences:
    print(occ)

# print(doc.prettify())


# parent = prices[0].parent
# strong = parent.find("strong")
# print(strong.string)
# print(parent)

#  <h1 id="firstHeading" class="firstHeading mw-first-heading"><span class="mw-page-title-main">Chroicocephalus ridibundus</span></h1>