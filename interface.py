from tkinter import Tk, Button, Entry, Label, messagebox, Radiobutton, StringVar, Scrollbar, Text
from functools import partial
from threading import Thread
import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import index

choix = ['p', 'h1', 'h2', 'nav', 'div', 'section', 'article']
if not os.path.isdir('web'):
    os.mkdir('web')
    index.base_html()
else :
    if os.stat("web/index.html").st_size == 0:
        index.base_html()
def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()
        Web.driver.close()
def test():
    if Web.isAlive():
        print('Il existe')
    else:
        print('Non')

class ViewHtml(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.oui = True
    def run(self):
        chrome_options = Options()
        html_file = os.getcwd() + "//" + "web/index.html"
        chrome_options.add_argument("--app=file:///" + html_file)
        chrome_options.add_argument("--window-size=600,539")
        chrome_options.add_argument("--window-position=601,100")
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        assert "No results found." not in self.driver.page_source
        while self.oui:
            time.sleep(2)
            self.driver.refresh()
    def enter_click(self):
        index.ajout_element(varGr.get(),comment.get())
        self.driver.refresh()
    def fini(self):
        self.oui = False
        on_closing()


Web = ViewHtml()
root = Tk()
Web.start()
root.protocol("WM_DELETE_WINDOW", on_closing)
root.geometry("500x500+100+100")
root.propagate(0)
root.title('Simple exemple')

qb = Button(root, text='Quitter', command=partial(Web.fini))
qb.grid(column=0,row=0)
text = Label(root, text="Choisisser l'élément à ajouter sur votre site : ")
text.grid(column=0,row=1, columnspan=4)

varGr = StringVar()
for i in range(len(choix)):
    b = Radiobutton(root, variable=varGr,text=choix[i], value=choix[i])
    b.grid(column=i,row=2)

text1 = Label(root, text="Entrer le texte que possèdera l'élément : ")
text1.grid(column=0,row=3, columnspan=4)
comment = Text(root, height=2, width=30)
comment.grid(column=4,row=3,columnspan=4)
valide = Button(root, text='Valider', command=partial(Web.enter_click))
valide.grid(column=3,row=4, pady=20)

test = Button(root, text='TEST THREAD', command=partial(test))
test.grid(column=0,row=5)


root.mainloop()


