import tkinter as tk
from tkinter import SUNKEN
from PIL import Image, ImageTk
from random import *

root1 = tk.Toplevel()
root1.title('Game')
root1.attributes('-fullscreen', True)
root1.resizable(False, False)

count_drapeau = 0
nbr_bombe = 0
chiffres = 0
counter_win = 0

cases = []
discovery_cases = []
t_visible_no_visible = []
t_discovery = []

img_retour = tk.PhotoImage(file='image/button_retour.png')
img_rejouer= tk.PhotoImage(file='image/button_rejouer.png')
img_resize = Image.open("image/drapeau.png")
img_resize_bomb = Image.open("image/bombe_menu.png")
img_resize_smiley = Image.open("image/pngfind.com-smile-emoji-png-215707.png")
img_resize_game_over = Image.open("image/GAME-OVER.png")
resized_image = img_resize.resize((20, 20))
resized_image_bomb = img_resize_bomb.resize((20, 20))
resized_image_smiley = img_resize_smiley.resize((40, 40))
resized_image_smiley_regle = img_resize_smiley.resize((20, 20))
img_drapeau = ImageTk.PhotoImage(resized_image)
img_bomb = ImageTk.PhotoImage(resized_image_bomb)
img_smiley = ImageTk.PhotoImage(resized_image_smiley)
img_smiley_regle = ImageTk.PhotoImage(resized_image_smiley_regle)
img_game_over = ImageTk.PhotoImage(img_resize_game_over)

frame_principale = tk.Frame(root1, height=800, width=550, bg='white', relief=tk.RAISED, border=10, padx=5, pady=5)
frame_regle = tk.Frame(root1)
frame_grid = tk.Frame(frame_principale)

def desactive(a):#focntion qui désactive une case qui découvre ce que se cache derrière la case
    cases[a].grid_remove()
    if t_discovery[a] == 2:
        for s in range(64):
            cases[s].unbind("<Button-1>")
            cases[s].unbind("<Button-3>")
            if t_discovery[s] == 2:
                cases[s].grid_remove()

def drapeau(a):#place un drapeau sur la case et si drapeau enlève le drapeau
    global drap, count_drapeau

    if count_drapeau < 15 and t_visible_no_visible[a] == 0:
        cases[a].config(width=20,image=img_drapeau)
        t_visible_no_visible[a] = 2
        count_drapeau += 1

    elif t_visible_no_visible[a] == 2:
        cases[a].config(image="", width=2)
        t_visible_no_visible[a] = 0
        count_drapeau -= 1

    for i in range (64):
        if t_visible_no_visible[i] == t_discovery[i] == 2:
            counter_win =+ 1
            if counter_win == 15:
                tk.Label(frame_principale, text='Vous avez gagné').grid(row=3, column=0)
                for s in range(64):
                    cases[s].unbind("<Button-1>")
                    cases[s].unbind("<Button-3>")



def partie(option):#fonction qui contient la frame grid qui elle contient toutes les cases et les bombes la génération de nombre
    global nbr_bombe, option_use

    option_use = option

    if option == 1:
        indice = 0
        nbr_bombe = 15

        #discovery demineur
        for y in range(64):
            t_discovery.append(0)
            t_visible_no_visible.append(0)

        #config grid visual demineur
        for i in range(8):
            for j in range(8):
                discovery_cases.append((tk.Label(frame_grid, width=2, border=4, relief=tk.SOLID, fg='blue', font='Arial 13')))
                cases.append(tk.Button(frame_grid, width=2, relief=tk.RAISED, border=3.5))
                cases[indice].grid(row=i, column=j)
                discovery_cases[indice].grid(row=i, column=j)
                cases[indice].bind("<Button-1>", lambda event, index=indice: desactive(index))
                cases[indice].bind("<Button-3>", lambda event, index=indice: drapeau(index))
                indice += 1

        #config bomb
        for z in range(16):
            random_bomb = randint(0, 63)
            discovery_cases[random_bomb].config(image=img_bomb, width=20)
            t_discovery[random_bomb] = 2

        for q in range(64):
            if t_discovery[q] == 2:
                if t_discovery.index(t_discovery[q]) in [-2, -3, -4, -5, -6, -7]:
                    discovery_cases[q - 1].config(text=+ 1)
                    discovery_cases[q + 1].config(text=+ 1)
                    discovery_cases[q - 6].config(text=+ 1)
                    discovery_cases[q - 7].config(text=+ 1)
                    discovery_cases[q - 8].config(text=+ 1)

                if t_discovery.index(t_discovery[q]) in [1, 2, 3, 4, 5, 6]:
                    discovery_cases[q - 1].config(text=+ 1)
                    discovery_cases[q + 1].config(text=+ 1)
                    discovery_cases[q + 7].config(text=+ 1)
                    discovery_cases[q + 8].config(text=+ 1)
                    discovery_cases[q + 9].config(text=+ 1)

                if t_discovery.index(t_discovery[q]) == 0:
                    print(t_discovery.index(discovery_cases[q + 8]))
                    discovery_cases[q + 1].config(text=+ 1)
                    discovery_cases[q + 8].config(text=+ 1)
                    discovery_cases[q + 9].config(text=+ 1)

                if t_discovery.index(t_discovery[q]) == 7:
                    discovery_cases[q - 1].config(text=+ 1)
                    discovery_cases[q + 7].config(text=+ 1)
                    discovery_cases[q + 8].config(text=+ 1)

                if t_discovery.index(t_discovery[q]) == -8:
                    discovery_cases[q + 1].config(text=+ 1)
                    discovery_cases[q - 7].config(text=+ 1)
                    discovery_cases[q - 8].config(text=+ 1)

                if t_discovery.index(t_discovery[q]) == -1:
                    discovery_cases[q - 1].config(text=+ 1)
                    discovery_cases[q - 9].config(text=+ 1)
                    discovery_cases[q - 8].config(text=+ 1)

                else:
                    discovery_cases[q - 1].config(text=+ 1)
                    discovery_cases[q - 7].config(text=+ 1)
                    discovery_cases[q - 8].config(text=+ 1)
                    discovery_cases[q - 9].config(text=+ 1)
                    discovery_cases[q + 1].config(text=+ 1)
                    discovery_cases[q + 7].config(text=+ 1)
                    discovery_cases[q + 8].config(text=+ 1)
                    discovery_cases[q + 9].config(text=+ 1)
    if option == 2:
        indice = 0
        nbr_bombe = 30

        #discovery demineur
        for y in range(144):
            t_discovery.append(0)
            t_visible_no_visible.append(0)

        #config grid visual demineur
        for i in range(12):
            for j in range(12):
                discovery_cases.append((tk.Label(frame_grid, width=2, border=4, relief=tk.SOLID, fg='blue', font='Arial 13')))
                cases.append(tk.Button(frame_grid, width=2, relief=tk.RAISED, border=3.5))
                cases[indice].grid(row=i, column=j)
                discovery_cases[indice].grid(row=i, column=j)
                cases[indice].bind("<Button-1>", lambda event, index=indice: desactive(index))
                cases[indice].bind("<Button-3>", lambda event, index=indice: drapeau(index))
                indice += 1

        #config bomb
        for z in range(31):
            random_bomb = randint(0, 143)
            discovery_cases[random_bomb].config(image=img_bomb, width=20)
            t_discovery[random_bomb] = 2

        for q in range(144):
            if t_discovery[q] == 2:
                if t_discovery.index(t_discovery[q]) in [-2, -3, -4, -5, -6, -7]:
                    discovery_cases[q - 1].config(text=+ 1)
                    discovery_cases[q + 1].config(text=+ 1)
                    discovery_cases[q - 6].config(text=+ 1)
                    discovery_cases[q - 7].config(text=+ 1)
                    discovery_cases[q - 8].config(text=+ 1)

                if t_discovery.index(t_discovery[q]) in [1, 2, 3, 4, 5, 6]:
                    discovery_cases[q - 1].config(text=+ 1)
                    discovery_cases[q + 1].config(text=+ 1)
                    discovery_cases[q + 7].config(text=+ 1)
                    discovery_cases[q + 8].config(text=+ 1)
                    discovery_cases[q + 9].config(text=+ 1)

                if t_discovery.index(t_discovery[q]) == 0:
                    print(t_discovery.index(discovery_cases[q + 8]))
                    discovery_cases[q + 1].config(text=+ 1)
                    discovery_cases[q + 8].config(text=+ 1)
                    discovery_cases[q + 9].config(text=+ 1)

                if t_discovery.index(t_discovery[q]) == 7:
                    discovery_cases[q - 1].config(text=+ 1)
                    discovery_cases[q + 7].config(text=+ 1)
                    discovery_cases[q + 8].config(text=+ 1)

                if t_discovery.index(t_discovery[q]) == -8:
                    discovery_cases[q + 1].config(text=+ 1)
                    discovery_cases[q - 7].config(text=+ 1)
                    discovery_cases[q - 8].config(text=+ 1)

                if t_discovery.index(t_discovery[q]) == -1:
                    discovery_cases[q - 1].config(text=+ 1)
                    discovery_cases[q - 9].config(text=+ 1)
                    discovery_cases[q - 8].config(text=+ 1)

                else:
                    discovery_cases[q - 1].config(text=+ 1)
                    discovery_cases[q - 7].config(text=+ 1)
                    discovery_cases[q - 8].config(text=+ 1)
                    discovery_cases[q - 9].config(text=+ 1)
                    discovery_cases[q + 1].config(text=+ 1)
                    discovery_cases[q + 7].config(text=+ 1)
                    discovery_cases[q + 8].config(text=+ 1)
                    discovery_cases[q + 9].config(text=+ 1)

    if option == 3:
        indice = 0
        nbr_bombe = 50

        #discovery demineur
        for y in range(225):
            t_discovery.append(0)
            t_visible_no_visible.append(0)

        #config grid visual demineur
        for i in range(15):
            for j in range(15):
                discovery_cases.append((tk.Label(frame_grid, width=2, border=4, relief=tk.SOLID, fg='blue', font='Arial 13')))
                cases.append(tk.Button(frame_grid, width=2, relief=tk.RAISED, border=3.5))
                cases[indice].grid(row=i, column=j)
                discovery_cases[indice].grid(row=i, column=j)
                cases[indice].bind("<Button-1>", lambda event, index=indice: desactive(index))
                cases[indice].bind("<Button-3>", lambda event, index=indice: drapeau(index))
                indice += 1

        #config bomb
        for z in range(225):
            random_bomb = randint(0, 224)
            discovery_cases[random_bomb].config(image=img_bomb, width=20)
            t_discovery[random_bomb] = 2

        for q in range(225):
            if t_discovery[q] == 2:
                if t_discovery.index(t_discovery[q]) in [-2, -3, -4, -5, -6, -7]:
                    discovery_cases[q - 1].config(text=+ 1)
                    discovery_cases[q + 1].config(text=+ 1)
                    discovery_cases[q - 6].config(text=+ 1)
                    discovery_cases[q - 7].config(text=+ 1)
                    discovery_cases[q - 8].config(text=+ 1)

                if t_discovery.index(t_discovery[q]) in [1, 2, 3, 4, 5, 6]:
                    discovery_cases[q - 1].config(text=+ 1)
                    discovery_cases[q + 1].config(text=+ 1)
                    discovery_cases[q + 7].config(text=+ 1)
                    discovery_cases[q + 8].config(text=+ 1)
                    discovery_cases[q + 9].config(text=+ 1)

                if t_discovery.index(t_discovery[q]) == 0:
                    print(t_discovery.index(discovery_cases[q + 8]))
                    discovery_cases[q + 1].config(text=+ 1)
                    discovery_cases[q + 8].config(text=+ 1)
                    discovery_cases[q + 9].config(text=+ 1)

                if t_discovery.index(t_discovery[q]) == 7:
                    discovery_cases[q - 1].config(text=+ 1)
                    discovery_cases[q + 7].config(text=+ 1)
                    discovery_cases[q + 8].config(text=+ 1)

                if t_discovery.index(t_discovery[q]) == -8:
                    discovery_cases[q + 1].config(text=+ 1)
                    discovery_cases[q - 7].config(text=+ 1)
                    discovery_cases[q - 8].config(text=+ 1)

                if t_discovery.index(t_discovery[q]) == -1:
                    discovery_cases[q - 1].config(text=+ 1)
                    discovery_cases[q - 9].config(text=+ 1)
                    discovery_cases[q - 8].config(text=+ 1)

                else:
                    discovery_cases[q - 1].config(text=+ 1)
                    discovery_cases[q - 7].config(text=+ 1)
                    discovery_cases[q - 8].config(text=+ 1)
                    discovery_cases[q - 9].config(text=+ 1)
                    discovery_cases[q + 1].config(text=+ 1)
                    discovery_cases[q + 7].config(text=+ 1)
                    discovery_cases[q + 8].config(text=+ 1)
                    discovery_cases[q + 9].config(text=+ 1)

#données partie
frame_donnee = tk.Frame(frame_principale, bg='white', relief=SUNKEN, border=4)
#nombre de drapeau
drap = tk.Label(frame_donnee, text=count_drapeau, fg='red', bg='black', font="Helvetica 26", width=2, height=1, borderwidth=3,relief="solid")
drap.pack(side="left", padx=5, pady=5)
tk.Button(frame_donnee, image=img_smiley, fg='white', bg='white', command=lambda: partie(option_use)).pack(side="left", padx=25)
tk.Label(frame_donnee, text=nbr_bombe, fg='red', bg='black', font="Helvetica 26", width=2, height=1, borderwidth=3,relief="solid").pack(side="left", padx=5, pady=5)
#assenblement de toutes les frames
frame_principale.pack()
frame_donnee.grid(row=0, column=0)
tk.Label(frame_principale, text="", bg="white").grid(row=1, column=0)
frame_grid.grid(row=2, column=0)
#Les règles
tk.Label(frame_regle, text='Comment jouer au démineur ?', bg='white', font='Arial 22').grid(row=0, column=0, columnspan=2)
tk.Button(frame_regle, width=2, relief=tk.RAISED, border=3.5).grid(row=1, column=0)
tk.Label(frame_regle, text="Clic gauche = libérer une cellule ou une case.", bg="white").grid(row=1, column=1)
tk.Button(frame_regle, relief=tk.RAISED, border=3.5, width=20, image=img_drapeau).grid(row=2, column=0)
tk.Label(frame_regle, text="Clic droit = placer un drapeau sur une cellule.", bg="white").grid(row=2, column=1)
tk.Button(frame_regle, relief=tk.RAISED, border=3.5, width=20, image=img_smiley_regle).grid(row=3, column=0)
tk.Label(frame_regle, text="Augmente les nombres de bombes dans la grille.", bg="white").grid(row=3, column=1)
tk.Label(frame_regle, text="Le but est qu'il faut découvrir toutes les cases libres en plaçant des drapeaux (avec le clic de la souris).", bg="white").grid(row=4, column=0, columnspan=2)
tk.Label(frame_regle, text="Sans faire exploser les mines présentes sur la grille représentant un champ.", bg="white").grid(row=5, column=0, columnspan=2)
frame_regle.pack()

#bouton pour rejouer ou retour
tk.Button(root1, image=img_retour, command=lambda: root1.destroy(), borderwidth=0).pack(anchor='se')
tk.Button(root1, image=img_rejouer, command=lambda: partie(option_use), borderwidth=0).pack(anchor='sw')
