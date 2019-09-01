import requests
from bs4 import BeautifulSoup

# Get HTML page
r = requests.get("http://surfclub-vieuxboucau.com/")
r = r.content

# BeautifulSoup 4 (bs4) pour parser le HTML
soup = BeautifulSoup(r)

imgs = soup.find_all("img")

urls = []
for img in imgs:
    i = img
    urls.append(i.get("src"))
    

# Save in excel
import xlsxwriter

workbook = xlsxwriter.Workbook('liens_surf.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write(0,0,"URL")
for i in range(len(urls)):
    worksheet.write(i+1,0,urls[i])
workbook.close()




###########################################
r = requests.get("https://en.wikipedia.org/wiki/World_Surf_League")
r = r.content

soup = BeautifulSoup(r)

mw = soup.find("div", {"class":"mw-parser-output"})
wsl = mw.find_all("table")[1]
trs = wsl.find_all("tr")


men = []
for tr in trs:
    if tr.find("th") == None or len(tr.find("th")) == 0:
        tds = tr.find_all("td")
        year = tds[0].find("a")
        if year is not None:
            man = tds[1].find_all("span")[1].getText()
            men.append([year.getText(),man.replace("(","").replace(")","")])
            
workbook = xlsxwriter.Workbook('gagnants_hommes.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write(0,0,"année")
worksheet.write(0,1,"pays")
for i in range(len(men)):
    worksheet.write(i+1,0,men[i][0])
    worksheet.write(i+1,1,men[i][1])
workbook.close()


import csv
with open('gagnants_hommes.csv', mode='w') as monfichier:
    fichier = csv.writer(monfichier, delimiter=';', quotechar='"')
    fichier.writerow(["année","pays"])
    for i in range(len(men)):
        fichier.writerow([men[i][0],men[i][1]])