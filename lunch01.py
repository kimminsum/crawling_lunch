from bs4 import BeautifulSoup
import urllib.request, datetime

now = datetime.datetime.now()
webpage = urllib.request.urlopen("https://choji.hs.kr/lunch.lunch_list?ym=2021%d&mcode=&cate=" % int(now.month-1))
soup = BeautifulSoup(webpage, 'html.parser')
bob = soup.find(id = "foodListArea")
with open("lunch.txt", "w", encoding="utf-8") as f:
    f.write(str(bob.get_text()))