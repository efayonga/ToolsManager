from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import MenuPrincipal




 
class Moyenne:
    """
        Instancier un objet de type "Moyenne" lancera la fenêtre de calcul de Moyenne
    """
    def __init__(self):
        #######Fenêtre#######
        root=Tk()
        root.focus_force()
        root.title("Calcul de moyenne")
        root.geometry("1080x720+400+200")
        root.resizable(False, False)
        #####################

        #########Frames######
        mainframe=ttk.Frame(root)
        mainframe.pack(expand=True, fill=Y, side=RIGHT, padx= 10, pady=15)

        f_inp= Frame(root)
        f_inp.pack(side= LEFT, fill=Y)
        #####################
        
        #####Variables###
        global nb_row, tab_ent
        tab_ent=[] #Contient les tuples d'enrtées
        nb_row= 0 #Contient le nombre de de tuples d'entrées
        #################
        
        ###############Fonctions#################

        
        def launch_MP(event=0):
            """
                Lance la fenêtre MenuPrincipal.
            """
            
            root.destroy()
            MenuPrincipal.MP()
            return

        
        def ajout_mat(nb=-1):
            """
                Ajoute une ligne d'entrée de moyenne.
            """
            global nb_row, tab_ent

            #Lors d'un appel avec un bind, nous voulons que le programme traite l'"event" comme une selection avec un bouton. On affecte donc -1 a nb.
            if(type(nb)!=int):
                nb=-1

            #Si on utilise le bouton ajout custom
            if(nb!=-1):
                #Si le nombre est valide, on crée les entrées. 
                if (0<nb<18):
                    tempo.destroy()

                    #On efface puis recrée le nombre 'nb' d'entrées. 
                    for i in range(nb_row):
                        delete_mat()
                    for i in range(nb-1):
                        ajout_mat()

                #Si le nombre est invalide, on affiche une alerte
                else:
                    mb.showwarning("Attention !","Vous devez entrer un nombre positif et plus petit que 18")

                return


            #Si on utilise pas le bouton ajout_custom et qu'il y a moins de 18 entrées (Sinon les entrées sortent de la fenêtre)
            if(nb_row < 18):
                #Ajout dans la liste 'tab_ent' des entrées
                tab_ent.append( (ttk.Checkbutton(f_inp),ttk.Checkbutton(f_inp),  Entry(f_inp), Entry(f_inp)) )
                tab_ent[-1][0].state(['!alternate'])
                tab_ent[-1][1].state(['!alternate'])


                c=0
                for e in tab_ent[-1]:
                    e.grid(row= nb_row+2, column= c, pady= 5)
                    c+=1

                nb_row+=1



        
        def custom_ajout_mat(self=0):
            """
               Trigger quand l'utilisateur utilise la fenêtre d'ajout précis de colonnes. 
            """
            global tempo
            tempo = Tk()
            tempo.title("Ajout customisé de matières")
            tempo.geometry("250x100")
            tempo.resizable(False, False)

            Label(tempo, text="Veuillez entrer un nombre valide de matières\n à insérer plus petit que 18, puis appuyez sur\n entrée.").pack(expand=True)

            ent=Entry(tempo)
            ent.pack(expand=True)
            ent.insert(0, "Tapez ici")
            
            ent.bind("<Return>", lambda x :ajout_mat(int(ent.get())))
            
            
                
        
        def delete_mat(event=0):
            """
                Enlève une ligne d'entrée
            """
            global nb_row, tab_ent
            if(nb_row>1):
                for ent in tab_ent[-1]:
                    ent.destroy()

                tab_ent.remove(tab_ent[-1])
                nb_row-=1


        def calcul_moy(self=0):
            """
                Calcule les differentes moyennes et les affiche
            """

            #########Calcul moyenne générale####
            #Liste par comprénsion, prend des tuples (note, coefficient)
            moy_g= [ (float(ent[2].get()), float(ent[3].get()))
                     for ent in tab_ent if (len(ent[2].get())!=0 and len(ent[3].get()) != 0)]
            if(len(moy_g)!=0):
                total_g=0
                total_g_coeff=0
                for valeur in moy_g:
                    total_g+=valeur[0]*valeur[1]
                    total_g_coeff+=valeur[1]

                total_g= total_g/total_g_coeff
                l_show_gene.config(text="{}".format(round(total_g, 2)))
            ###################################

            #########Calcul moyenne scientifique (coché)
            #Liste par comprénsion, prend des tuples (note, coefficient)
            moy_s= [ (float(ent[2].get()), float(ent[3].get()))
                     for ent in tab_ent if (len(ent[2].get())!=0 and len(ent[3].get()) != 0 and ent[0].state())]


            #Si il n'y a pas de moy_s de coché, on marque 0
            if (len(moy_s)==0):
                l_show_scie.config(text="{}".format(0))

            else:
                total_s=0
                total_s_coeff=0
                for valeur in moy_s:
                    total_s+=valeur[0]*valeur[1]
                    total_s_coeff+=valeur[1]

                total_s= total_s/total_s_coeff
                l_show_scie.config(text="{}".format(round(total_s, 2)))

            #############################################


            #########Calcul moyenne info/elec (coché)
            #Liste par comprénsion, prend des tuples (note, coefficient)
            moy_ie= [ (float(ent[2].get()), float(ent[3].get()))
                     for ent in tab_ent if (len(ent[2].get())!=0 and len(ent[3].get()) != 0 and ent[1].state())]


            #Si il n'y a pas de moy_ie, on affiche 0
            if (len(moy_ie)==0):
                l_show_ie.config(text="{}".format(0))
                

            #Calcul de moyenne info/elec
            else:
                total_ie=0
                total_ie_coeff=0
                for valeur in moy_ie:
                    total_ie+=valeur[0]*valeur[1]
                    total_ie_coeff+=valeur[1]

                total_ie= total_ie/total_ie_coeff
                
                l_show_ie.config(text="{}".format(round(total_ie, 2)))

            #############################################

                commentaire(total_g, total_s, total_ie)


 
        def commentaire(total_g, total_s, total_ie):
            """
                Affiche des commentaires en fonction des notes de l'élève.
            """
            
            if total_g>=8 and total_s<8 and total_ie>total_s :
                l_text.config(text="Je vois que la physique a frappé ...")
                return

            if 17>total_g>=15 and 17>total_s>=15 and 17>total_ie>=15 :
                l_text.config(text="Ne serait-ce pas là un major de promo ?")
                return

            if total_g<10 and total_s<8 and total_ie<8 :
                l_text.config(text="Bah écoute: Bouge-toi le Callypige qu'est-ce que tu veux que je te dise !!!")
                return

            if total_g<8 and total_s<6 and total_ie<6 :
                l_text.config(text="Bon écoute. Je pense qu'il est un peu trop tard mais t'inquiètes pas on t'aime bien ...")
                return

            if total_g<6 and total_s<total_g and total_ie<total_g:
                l_text.config(text="A partir de là, même la reconversion professionnelle me semble compliqué pour toi ... ")
                return

            if total_g<total_s and total_g<total_ie :
                l_text.config(text="Les langues, la P5 et la MSH semblent être une vaste contrée négative pour toi ...")
                return
            
            if total_g>=8 and total_ie<7 and total_s>total_ie :
                l_text.config(text="J'imagine que le tri fusion et la recherche dichotomique ne sont pas tes points forts ?")
                return

            if total_g>=10 and 8.5<=total_s<10 and 10>total_ie>=8.5 :
                l_text.config(text="Allez encore un effort, tu y es presque !!!")
                return
            
            if 11>total_g>=10 and 11>total_s>=10 and 11>total_ie>=10 :
                l_text.config(text="C'est juste mais ca passe !!!")
                return

            if 12>total_g>=11 and total_s>10 and total_ie>10 :
                l_text.config(text="Peut mieux faire")
                return

            if total_g>=12 and total_s>=11 and total_ie>=11 :
                l_text.config(text="Réclame la switch à tes parents si tu l'as pas encore")
                return

            if total_g>=17 and total_s>17 and total_ie>17:
                l_text.config(text="Vous avez trouvé le remède contre le Coronavirus et l'ONU vous convoque régler les récents conflits du monde actuel")
                return


        
        
        ########F_INP####
        ##
        l_coeff=Label(f_inp, text="Entrez vos notes et coefficients dans les entrées ci dessous ! \n Cochez les box devant votre entrée pour la compter dans la moyenne.\nRaccourcis : 'a' pour ajouter une ligne, 'r' pour en retirer, 'Entrée' pour calculer.")
        l_coeff.grid(row=0, column=0, columnspan=4, sticky= NSEW, pady= 15)

        l_sc= Label(f_inp, text="Scientifique")
        l_sc.grid(row=1, column=0, sticky= NSEW)

        l_ie= Label(f_inp, text="Info/Elec")
        l_ie.grid(row=1, column=1, sticky= NSEW)

        l_note= Label(f_inp, text="Note")
        l_note.grid(row=1, column=2, sticky= NSEW)

        l_coeff= Label(f_inp, text="Coefficient")
        l_coeff.grid(row=1, column=3, sticky=NSEW)
        ##################


        ########Mainframe###
        l_moy=Label(mainframe, text="MOYENNES :")
        l_moy.grid(row=3, column=0, sticky=NSEW)

        l_show_gene=Label(mainframe)
        l_show_gene.grid(row=3, column=1, sticky=NSEW)

        l_show_scie=Label(mainframe)
        l_show_scie.grid(row=3, column=2, sticky=NSEW)

        l_show_ie=Label(mainframe)
        l_show_ie.grid(row=3, column=3, sticky=NSEW)

        l_moygen=Label(mainframe, text="Moyenne générale")
        l_moygen.grid(row=2, column=1, sticky='nsew', padx=5)

        l_sci=Label(mainframe, text="Moyenne scientifique:")
        l_sci.grid(row=2, column=2, sticky='nsew', padx=5)

        l_inf_elec=Label(mainframe, text="Moyenne dans le bloc info/élec:")
        l_inf_elec.grid(row=2, column=3,sticky='nsew')

        l_commentaires=Label(mainframe, text="Commentaires :")
        l_commentaires.grid(row=4, column=0, sticky='nsew', pady=10)

        l_text= Label(mainframe, text="")
        l_text.grid(row=4, column=1, columnspan=2 ,sticky='nsew', pady=10)

        l_ps=Label(mainframe, text="PS: Ce commentaire n'est pas à prendre au sérieux")
        l_ps.grid(row=5, column=1, columnspan=3, sticky='nsew', pady= 20)
        ##################

        ####Boutons######
        b_ajout=ttk.Button(mainframe, text="Ajout d'une matière", command=ajout_mat)
        b_ajout.grid(row=1, column=0, padx=10)

        b_del=ttk.Button(mainframe, text="Retrait d'une matière", command=delete_mat)
        b_del.grid(row=1, column=1, padx=10)

        b_calcul=ttk.Button(mainframe, text="Calculer", command=calcul_moy)
        b_calcul.grid(row=1, column=2, padx=10)

        b_custajout=ttk.Button(mainframe, text="Ajouter un nombre précis de matières", command=custom_ajout_mat)
        b_custajout.grid(row=1, column=3, padx=10)


        ttk.Button(mainframe, text= "Revenir au menu", command= launch_MP).grid(row=0, column=3)
        #################


        #Pour ajouter une colonne dès le début
        ajout_mat()


        ####Binds####
        root.bind("<a>", ajout_mat)
        root.bind("<r>", delete_mat)
        root.bind("<Return>", calcul_moy)
        root.bind("<Escape>", launch_MP)
        #############
        

        
        root.mainloop()


