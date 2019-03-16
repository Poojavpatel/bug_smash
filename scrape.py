from bs4 import BeautifulSoup
import requests,csv
response = requests.get("https://scholarships.gov.in/NSP1718/public/homePage")
soup = BeautifulSoup(response.content, 'html.parser')

soup1 = soup.find('body')

# Writing to csv file
f = open('data.csv', 'w', newline = '')
writer = csv.writer(f)
writer.writerow(['name','expires_in','for_degree','country'])

# main scraping
# soup1 = soup.findAll('div', attrs={'id':'scholarship-content'})
posts =[]
posts = soup.findAll('div', attrs={'class':'post'})
print(posts)

# div = soup.find(id="scholarship-content")








# writer.writerow([s1,s2,s3,s4])