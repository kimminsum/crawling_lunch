from bs4 import BeautifulSoup
from tkinter import *
from tkinter import ttk
import urllib.request, datetime

now = datetime.datetime.now()
webpage = urllib.request.urlopen("https://choji.hs.kr/lunch.view?date=%d&mcode=&cate=" %int(now.strftime("%Y%m%d")))
soup = BeautifulSoup(webpage, 'html.parser')
bob = soup.find("div", "menuName")
root = Tk()
root.title("오늘의 급식")
root.resizable(False, False)
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text=str(bob.get_text())).grid(column=0, row=1)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=1)
root.mainloop()