from tkinter import *

root=Tk()
root.title("Simulation cooperative sonatel")
root.geometry("1092x680")
scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill = Y )

#first part CALCUL DU COUT GLOBAL
# Remove text from label


titre_un=Label(root, text="CONSTRUCTION ou TERRAIN + CONSTRUCTION ou ACQUISITION BIEN IMMOBILIER", font="arial 15 bold").place(x=100,y=25)

cout_terrain = Label(root, text="Cout du terrain", font="arial 15")
cout_construction = Label(root, text="Cout de la construction", font="arial 15")
cout_acquis = Label(root, text="Cout d'acquisition du bien immo.", font="arial 15")

cout_terrain.place(x=100,y=50)
cout_construction.place(x=100,y=100)
cout_acquis.place(x=100,y=150)

principalValue = StringVar(root, value = 0)
rateValue = StringVar(root, value = 0)
timeValue = StringVar(root, value = 0)

ct_entry=Entry(root,textvariable=principalValue, font="arial 20", width=10)
cc_entry=Entry(root,textvariable=rateValue, font="arial 20", width=10)
ca_entry=Entry(root,textvariable=timeValue, font="arial 20", width=10)

ct_entry.place(x=400,y=50)
cc_entry.place(x=400,y=100)
ca_entry.place(x=400,y=160)




#Apport de l'agent 



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
	apport_sonatel = cg/2
	verif = (((apport_agent+apport_sonatel+pb)*100)/cg)
	perc = ((ca*100)/cg)
	raj= ((40-perc)*cg)/100
	rajout= ((90-verif)*cg)/100
	#if((((apport_agent+apport_sonatel+pb)*100)/cg)>=90):
			#Label(text=f"apport sonatel : {apport_sonatel}", font='arial 20 bold',  bg='orange').place(x=600,y=450)
			#Label(text=f"apport agent(FINANCEMENT projet) : {apport_agent}", font='arial 20 bold',  bg='grey').place(x=600,y=500)
	if(((ca*100)/cg)>=40):
		if((((apport_agent+apport_sonatel+pb)*100)/cg)>=90):
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
	global text
	text = Label(root,text=f"Avis favorable de financement.", font='arial 20 bold',  bg='green')
	text.place(x=100,y=500)

def bis_scd():
	global text
	text = Label(root,text=f"financement refusé,total<90%. ", font='arial 20 bold',  bg='red')
	text.place(x=100,y=500)
def fourth_case():
	global text
	text = Label(root, text=f"financement refusé, apport agent<15% du cout projet.", font='arial 20 bold',  bg='red')
	text.place(x=100,y=500)
def fifth_case():
	global text
	text = Label(root, text=f"financement refusé, apport global<40% cout projet.", font='arial 20 bold',  bg='red')
	text.place(x=100,y=500)

def remove_text():
    text.destroy()

titre_DEUX=Label(root, text="Apport agent", font="arial 15 bold").place(x=100,y=200)

apport_terrain = Label(root, text="Apport terrain", font="arial 15")
apport_felson = Label(root, text="Apport Felson", font="arial 15")
pret_banquaire = Label(root, text="Pret banque", font="arial 15")
app_num = Label(root, text="Apport numeraire", font="arial 15")
app_tr = Label(root, text="Apport travaux realises", font="arial 15")

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

at_entry=Entry(root,textvariable=atValue, font="arial 20", width=10)
af_entry=Entry(root,textvariable=afValue, font="arial 20", width=10)
pb_entry=Entry(root,textvariable=pbValue, font="arial 20", width=10)
an_entry=Entry(root,textvariable=anValue, font="arial 20", width=10)
atr_entry=Entry(root,textvariable=atrValue, font="arial 20", width=10)

at_entry.place(x=400,y=250)
af_entry.place(x=400,y=300)
pb_entry.place(x=400,y=350)
an_entry.place(x=400,y=400)
atr_entry.place(x=400,y=450)

#financement du projet






#bouttons

Button(text='OUTPUT', font='arial 15', command=coutApport).place(x=600,y=200)
reset = Button(root,text='reset' ,font='arial 15' ,command=remove_text)
reset.place(x= 700,y=200)

Button(root,text='exit',command=lambda:exit(),font="arial 15",width=0).place(x=400,y=600)



root.mainloop()