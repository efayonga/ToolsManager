from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import MenuPrincipal




class conversion:
    def __init__(self):
        root=Tk()
        root.focus_force()
        root.geometry("1080x720+400+200")
        root.resizable(False, False)

        ####################################################################### FONCTION ########### 
        def launch_MP(event=0):
            root.destroy()
            MenuPrincipal.MP()
            return

        def convertir(event=0):

            #Pour mettre une unité on a la forme :  'ton_unité': {'deuxième_unité' : equivalent, 'x ème unité' : 'equivalent de ton_unité en x .......}  } 
            convertir= {
                        'inches': {'foot': 1/12, 'cm': 2.54, 'm': 0.0254},
                        'foot': {'inches': 12, 'cm': 30.48, 'm': 0.3048, 'km': 0.3048*(1/1000)},
                        'cm': {'inches': 1/(2.54), 'foot': 1/(30.48), 'm': 1/100},
                        'm': {'inch': 39.37, 'foot': 3.281, 'cm': 100, 'km': 1/1000},
                        'km': {'foot':3281, 'cm': 100000, 'm': 1000},
                        'grams': {'kg':1/1000, 'lbs': 2.20462*(1/1000), 'ounces':3.5274*(1/100)},
                        'kg': {'grams':1000, 'lbs': 2.20462, 'ounces':35.274},
                        'lbs': {'kg': 1/2.20462, 'ounces':16},
                        'ounces': {'grams':1/(3.5274*(1/100)), 'lbs': 1/16},
                        'L': {'US Gallons': 0.264172},
                        'US Gallons': {'L': 1/0.264172},
                                      
                        'euros': {'US dollars': 1.10 , 'pounds': 0.85, 'bitcoins':1.2*(1/10000), 'yen':120.12, 'yuan':7.64,
                                  'pesos': 20.67, 'rupees': 78.42, 'dong': 25522.08, 'CA dollars': 1.45, 'AU dollars': 1.63,
                                  'dirhams': 4.05},
                        
                        'US dollars': {'euros': 0.91, 'pounds': 0.77, 'bitcoins':1.1*(1/10000), 'yen':109.14, 'yuan':6.94,
                                  'pesos': 18.756, 'rupees': 71.287, 'dong': 23166.9, 'CA dollars': 1.318, 'AU dollars': 1.48,
                                  'dirhams': 3.67 },

                        'pounds': {'euros': 1.18, 'US dollars': 1.30, 'bitcoins':1.4*(1/10000), 'yen':141.8, 'yuan': 9.03,
                                  'pesos': 24.36, 'rupees': 92.64, 'dong': 30108.75, 'CA dollars': 1.714, 'AU dollars': 1.925,
                                  'dirhams': 4.77},

                        'bitcoins': {'US dollars': 9281.56 , 'pounds': 7148, 'euros':8467.15, 'yen':1013313.52, 'yuan':64916.24,
                                  'pesos': 174850.29, 'rupees': 667500.8, 'dong': 215610843.50, 'CA dollars': 12275.09,
                                  'AU dollars': 13800.64,'dirhams': 34389.7},

                        'yen': {'US dollars': 9.17*(1/1000), 'pounds': 7.053*(1/1000), 'bitcoins':1/(1013313.52), 'euros':8.33*(1/1000),
                                'yuan':6.3621*(1/100), 'pesos': 0.171766, 'rupees': 0.654019, 'dong': 212.45,
                                'CA dollars': 1.2101*(1/100), 'AU dollars': 1.4*(1/10000), 'dirhams': 0.033664},

                        'yuan': {'US dollars': 0.1441 , 'pounds': 0.111, 'bitcoins':1.5*(1/100000), 'yen':15.72, 'euros':0.131,
                                  'pesos': 2.693, 'rupees': 10.281, 'dong': 3340.52, 'CA dollars': 0.19, 'AU dollars': 0.213,
                                  'dirhams': 0.529},

                        'pesos': {'US dollars': 0.0535 , 'pounds': 0.041, 'bitcoins':5.7*(1/1000000), 'yen':5.837, 'yuan':0.371,
                                  'euros': 0.0486, 'rupees': 3.818, 'dong':1240.11 , 'CA dollars': 0.0706, 'AU dollars': 0.0793,
                                  'dirhams': 0.197},

                        'rupees': {'US dollars':0.014 , 'pounds': 0.0107, 'bitcoins':1.5*(1/1000000), 'yen':1.529, 'yuan':0.0972,
                                  'pesos': 0.262, 'euros': 0.0127, 'dong':324.9 , 'CA dollars': 0.019, 'AU dollars': 0.021,
                                  'dirhams': 0.0515},

                        'dong': {'US dollars': 4.3*(1/100000) , 'pounds': 3.3*(1/100000), 'bitcoins':1/100000000, 'yen':4.7*(1/1000),
                                 'yuan':3*(1/10000), 'pesos': 8.1*(1/10000), 'rupees': 3.1*(1/1000), 'euros': 3.9*(1/100000),
                                 'CA dollars': 5.7*(1/100000), 'AU dollars': 6.4*(1/100000), 'dirhams': 1.6*(1/10000)},

                        'CA dollars': {'US dollars': 0.757, 'pounds': 0.582, 'bitcoins':8.1*(1/100000), 'yen':82.59, 'yuan':5.254,
                                  'pesos': 14.16, 'rupees': 53.994, 'dong': 17548.53, 'euros': 0.688, 'AU dollars':1.122,
                                  'dirhams': 2.781},

                        'AU dollars': {'US dollars': 0.675 , 'pounds': 0.519, 'bitcoins':7.2*(1/100000), 'yen':73.63, 'yuan':4.68,
                                  'pesos': 12.629, 'rupees': 48.13, 'dong': 15640.97, 'CA dollars': 0.891, 'euros': 0.613,
                                  'dirhams': 2.479},

                        'dirhams': {'US dollars': 0.272 , 'pounds': 0.209, 'bitcoins':2.9*(1/100000), 'yen':29.7, 'yuan':1.889,
                                  'pesos': 5.093, 'rupees': 19.42, 'dong': 6308.88, 'CA dollars': 0.359, 'AU dollars': 0.403,
                                  'euros': 0.247},
                        '°C': { '°F': 9/5, 'Kelvin': 1},
                        '°F': { '°C': 0, 'Kelvin': 0},
                        'Kelvin': { '°C': 1, '°F': 9/5}
                        }

            c1= unit1.get() #Ca c'est la combo box de la première unité
            c2= unit2.get() #Ca c'est la combo box de la deuxième unité

            #vérifie si l'entrée est bien une variable flottante

            try:
                nombre= float(entr_value.get())
            

            except:
                mb.showwarning("Attention !", "Veuillez entrer un nombre valide")
                entr_value.delete(0,END)
                return
            
            #conversion spéciale pour les températures

            const=0
            if c1=='°C' and c2=='°F':
                const= 32
                #value=(nombre*(9/5))+32
                #conversion=str((round(value,2)))

            if c1=='°C' and c2=='Kelvin':
                const=273.15

            if c1=='°F' and c2=='°C':
                const=(nombre-32)*(5/9)

            if c1=='°F' and c2=='Kelvin':
                const=(nombre+459.67)*(5/9)

            if c1=='Kelvin' and c2=='°C':
                const=-273.15

            if c1=='Kelvin' and c2=='°F':
                const= -459.67

            if(c1==''):
                mb.showwarning("Attention !", "Vous n'avez pas selectionné l'unité de la valeur")
                return
            if(c2==''):
                mb.showwarning("Attention !", "L'unité à convertir n'a pas été choisie !")
                return
            if(c1==c2): #Si on fait par exemple de pound en pound
                label.config(text= entr_value.get())
                mb.showwarning("Attention !", "Même unité !")
                return
                    
            try:
                equivalent= convertir[c1][c2]  #Equivalent de la premiere unité en la deuxième

            except:
                mb.showwarning("Attention", "Vous devez choisir des unités compatibles")
                return


            conversion= str (round(float(nombre) * float(equivalent) + const ,2))
            label.config(text= ("{} {} est équivalent à {} {}".format(entr_value.get(), c1, conversion, c2)))
            label.grid(#row=4, column=2, columnspan=2,  sticky="nsew", pady=15
                column=1, row=4, columnspan=3, pady=10)
            entr_value.delete(0,END)
            unit1.set('')
            unit2.set('')

           
            
            
        #######################################################################





        root.title("Convertisseur")

        mainframe=ttk.Frame(root, padding="3 3 12 12")

        mainframe.pack(expand=True)

        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        root.bind("<Return>", convertir)
        root.bind("<Escape>", launch_MP)

        unitA=StringVar()
        unitB=StringVar()

        #res=DoubleVar()
        entr_value= ttk.Entry(mainframe, width=7
                             #, textvariable=res
                             )
            
        entr_value.grid(column=0, row=0, columnspan=2, sticky=(E,W), pady=10)


        unit1=ttk.Combobox(mainframe, textvariable= unitA,
                        values=('inches', 'foot', 'cm', 'm', 'km', 'grams', 'kg', 'ounces','lbs',
                                'L', 'US Gallons', '°C', '°F', 'Kelvin','euros', 'US dollars', 'pounds',
                                'bitcoins', 'yen', 'yuan', 'pesos', 'rupees', 'dong', 'CA dollars',
                                'AU dollars','dirhams'),
                        stat='readonly')
        unit1.grid(row=0, column=3, pady=10, sticky=(W, E))

        #ttk.Label(mainframe, text="est équivalent à").grid(column=1, row=3, sticky=(W, E))

        label=ttk.Label(mainframe, text="" )
        label.grid(column=2, row=3, sticky='nsew')

        label2=ttk.Label(mainframe, text=" UNITE DE CONVERSION : ")
        label2.grid(column=1, row=3, sticky='nsew')

        unit2=ttk.Combobox(mainframe, textvariable= unitB,
                        values=('inches', 'foot', 'cm', 'm', 'km', 'grams', 'kg', 'ounces','lbs',
                                'L', 'US Gallons', '°C', '°F', 'Kelvin','euros', 'US dollars', 'pounds',
                                'bitcoins', 'yen', 'yuan', 'pesos', 'rupees', 'dong', 'CA dollars',
                                'AU dollars','dirhams'),
                        stat='readonly')
        unit2.grid(row=3, column=3, sticky=(W, E))

        conversion=ttk.Button(mainframe, text='Convertir', command=convertir
                   ).grid(column=1, row=6, columnspan=3, pady=10)

        ttk.Button(mainframe, text= "Revenir au menu", command= launch_MP).grid(row=0, column=4)
        



        root.mainloop()

