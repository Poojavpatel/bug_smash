from bs4 import BeautifulSoup
import requests,csv
response = requests.get("https://www.buddy4study.com/article/scholarships-in-india")
soup = BeautifulSoup(response.content, 'html.parser')
# print(soup)

# Writing to csv file
f = open('data.csv', 'w', newline = '')
writer = csv.writer(f)
writer.writerow(['name','based_on','applicable_for','period'])

# main scraping
# there are 7 tables tbody
tables = soup.findAll('tbody')
mydict = {0:"merit",1:"annual income",2:"merit,annual income",3:"talent",4:"sports",5:"Women",6:"overseas"}

for t in tables:
    cols=t.findAll('tr')
    for c in cols:
        # s1=c.find('td', attrs={'width':'242'}).contents[0]
        s1= c.findChildren()[1].text
        s3= c.findChildren()[2].text
        s4= c.findChildren()[3].text
        s2= mydict[tables.index(t)]
        writer.writerow([s1,s2,s3,s4])
