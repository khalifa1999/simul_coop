from tkinter import *
from tkinter import filedialog
import pyautogui
from PIL import ImageTk, Image
import sys
import keyboard
from time import sleep

import re


root=Tk()
root.title("Simulation cooperative sonatel")

root.geometry("1920x1080")
#root.configure(background='orange')


img = ImageTk.PhotoImage(Image.open("nati.jpg"))
panel = Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")

#Affichage automatique



def get_out():
	sys.exit()

def takeScreenshot():
    myScreenshot = pyautogui.screenshot()
    file_path = filedialog.asksaveasfilename(defaultextension='.png')
    myScreenshot.save(file_path)

myButton = Button(root, text="capture d\'ecran",command=takeScreenshot,bg='green',fg='white',font=10)
myButton.place(x=750,y=550)
first = ""
scd =""
third = ""
cumul = 0
cumulNode = Label(root, text=f"cout total : {cumul} ", bg='orange',fg='white',font=10)
def  click(key):
	global first, cumul, temp 
	first += key.char

	displayCumul()
	# print(cumul)
	# node = Label(root, text=f"cumul : {cumul} ", bg='orange',fg='white',font=10)
	# node.place(x=700,y=400)
def click_one(key):
	global scd, cumul
	scd += key.char
	displayCumul()

def click_two(key):
	global third, cumul
	third += key.char
	displayCumul()

def displayCumul():
	global cumulNode, scd, first, third
	global cumul
	cumul = 0
	cumul = int(first)+int(scd)+int(third)

	cumulNode = Label(root, text=f"cout total : {cumul} ", bg='orange',fg='white',font=10)
	cumulNode.place(x=800,y=100)



titre_un=Label(root, text="CONSTRUCTION ou TERRAIN + CONSTRUCTION ou ACQUISITION BIEN IMMOBILIER", bg='orange',fg='white',font=10).place(x=400,y=25)

cout_terrain = Label(root, text="Cout du terrain", bg='orange',fg='white',font=10)
cout_construction = Label(root, text="Cout de la construction",bg='orange',fg='white',font=10)
cout_acquis = Label(root, text="Cout d'acquisition du bien immo.", bg='orange',fg='white',font=10)

cout_terrain.place(x=100,y=50)
cout_construction.place(x=100,y=100)
cout_acquis.place(x=100,y=150)

principalValue = StringVar(root, value = 0)
rateValue = StringVar(root, value = 0)
timeValue = StringVar(root, value = 0)

ct_entry=Entry(root,textvariable=principalValue, bg='orange',fg='white',font=10)
cc_entry=Entry(root,textvariable=rateValue, bg='orange',fg='white',font=10)
ca_entry=Entry(root,textvariable=timeValue,bg='orange',fg='white',font=10)
#Apport de l'agent et cout global live update



ct_entry.bind('<Key>',click)
cc_entry.bind('<Key>',click_one)
ca_entry.bind('<Key>',click_two)
#ca_entry.bind('<Key>',click_two)

ct_entry.place(x=400,y=50)
cc_entry.place(x=400,y=100)
ca_entry.place(x=400,y=160)






def coutApport():
	ct = int(ct_entry.get())
	cc= int(cc_entry.get())
	ca = int(ca_entry.get())
	global raj, rajout, perc, apport_agent, cg
	cg = ct+cc+ca

	at = int(atValue.get())
	af= int(afValue.get())
	pb = int(pbValue.get())
	an = int(an_entry.get())
	atr = int(atr_entry.get())
	ca = at+af+pb+an+atr
	apport_agent = ca-pb
	if(cg/2>=30000000):
		apport_sonatel = 30000000
	else:	
		apport_sonatel = cg/2
	verif = (((ca+apport_sonatel)*100)/cg)
	perc = ((ca*100)/cg)
	global quizaine, reste_quizaine, reste_quarante, reste_nonante
	quizaine=((apport_agent*100)/cg)
	reste_quizaine=((15-quizaine)*cg)/100
	reste_quarante=((40-perc)*cg)/100
	reste_nonante=((90-verif)*cg)/100
	#if((((apport_agent+apport_sonatel+pb)*100)/cg)>=90):
			#Label(text=f"apport sonatel : {apport_sonatel}", font='arial 20 bold',  bg='orange').place(x=600,y=450)
			#Label(text=f"apport agent(FINANCEMENT projet) : {apport_agent}", font='arial 20 bold',  bg='grey').place(x=600,y=500)
	if(((ca*100)/cg)>=40):
		if(verif>=90):
			if(((apport_agent*100)/cg)>=15):
				first_case()
			else:
				fourth_case()
		else:
				bis_scd()

	else:
		fifth_case()

def first_case():
	#Label(text=f"l'apport agent {ca}", font='arial 20 bold',  bg='blue').place(x=600,y=350)
	global one
	one = Label(root,text=f"Avis favorable de financement.", font='arial 20 bold',  bg='green')
	one.place(x=100,y=500)



def bis_scd():
	global two
	two = Label(root,text=f"financement refusé,total<90%. Il manque {reste_nonante}.", font='arial 20 bold',  bg='red')
	two.place(x=100,y=500)
def fourth_case():
	global three
	three = Label(root, text=f"financement refusé, apport agent<15% du cout projet. Il manque {reste_quizaine}.", font='arial 20 bold',  bg='red')
	three.place(x=100,y=500)
def fifth_case():
	global four
	four = Label(root, text=f"financement refusé, apport global<40% cout projet. Il manque {reste_quarante}.", font='arial 20 bold',  bg='red')
	four.place(x=100,y=500)



def remove_text():
    try:	
    	four.destroy()
    except:
    	pass
    try:	
    	one.destroy()
    except:
    	pass
    try:	
    	two.destroy()
    except:
    	pass
    try:	
    	three.destroy()
    except:
    	pass
  

titre_DEUX=Label(root, text="Apport agent", bg='orange',fg='white',font=10).place(x=650,y=200)

apport_terrain = Label(root, text="Apport terrain",bg='orange',fg='white',font=10)
apport_felson = Label(root, text="Apport Felson", bg='orange',fg='white',font=10)
pret_banquaire = Label(root, text="Pret banque", bg='orange',fg='white',font=10)
app_num = Label(root, text="Apport numeraire", bg='orange',fg='white',font=10)
app_tr = Label(root, text="Apport travaux realises",bg='orange',fg='white',font=10)

apport_terrain.place(x=100,y=250)
apport_felson.place(x=100,y=300)
pret_banquaire.place(x=100,y=350)
app_num.place(x=100,y=400)
app_tr.place(x=100,y=450)

atValue = StringVar(root, value = 0)
afValue = StringVar(root, value = 0)
pbValue = StringVar(root, value = 0)
anValue = StringVar(root, value = 0)
atrValue = StringVar(root, value = 0)

at_entry=Entry(root,textvariable=atValue,bg='orange',fg='white',font=10)
af_entry=Entry(root,textvariable=afValue, bg='orange',fg='white',font=10)
pb_entry=Entry(root,textvariable=pbValue, bg='orange',fg='white',font=10)
an_entry=Entry(root,textvariable=anValue, bg='orange',fg='white',font=10)
atr_entry=Entry(root,textvariable=atrValue, bg='orange',fg='white',font=10)

at_entry.place(x=400,y=250)
af_entry.place(x=400,y=300)
pb_entry.place(x=400,y=350)
an_entry.place(x=400,y=400)
atr_entry.place(x=400,y=450)



#financement du projet





#bouttons



Button(text='sortie',bg='green',fg='white',font=10, width=10, command=coutApport).place(x=550,y=550)
reset = Button(root,text='actualiser' ,bg='green',fg='white',font=10 , width=10,command=remove_text)
reset.place(x= 650,y=550)

Button(root,text='quitter',command=get_out,bg='green', fg='white',font=10,width=10).place(x=650,y=600)



root.mainloop()