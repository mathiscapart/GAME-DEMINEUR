import tkinter as tk
from constant import background as b

premier_passage = True
root = tk.Tk()
root.attributes('-fullscreen', True)
root.resizable(False, False)
root.title('Démineur')
root.config(bg=b)

img_demineure = tk.PhotoImage(file="image/logo_demineur.png")
img_jouer = tk.PhotoImage(file="image/button_jouer.png")
img_option = tk.PhotoImage(file="image/button_option.png")
img_option_logo = tk.PhotoImage(file="image/logo_option.png")
img_sauvegarder = tk.PhotoImage(file='image/button_sauvegarder.png')
img_retour = tk.PhotoImage(file='image/button_retour.png')
img_escape = tk.PhotoImage(file='image/button_escape.png')

option_var = 1
select_option = tk.StringVar()


def jouer():
    import game
    if option_var == 2:
        game.partie(2)
    if option_var == 3:
        game.partie(1)
    else:
        game.partie(1)

def menu_game():
    global frame_principale, premier_passage

    if not premier_passage:
        frame_principale.destroy()
    else:
        premier_passage = False

    frame_principale = tk.Frame(root)
    frame_principale.config(bg=b)
    label_demineur = tk.Label(frame_principale, image=img_demineure, bg=b)
    btn_jouer = tk.Button(frame_principale, image=img_jouer, bg=b, borderwidth=0, command=jouer)
    btn_option = tk.Button(frame_principale, image=img_option, command=option, bg=b, borderwidth=0)
    btn_escape = tk.Button(frame_principale, image=img_retour, command=lambda: root.destroy(), bg=b, borderwidth=0)

    label_demineur.pack()
    btn_jouer.pack(pady=80)
    btn_option.pack()
    btn_escape.pack(anchor='se', pady=60)

    frame_principale.pack(fill=tk.BOTH, expand=True)

def select():
    global option_var

    option_var = select_option.get()

    return option_var

def option():
    global frame_principale, premier_passage
    if not premier_passage:
        frame_principale.destroy()
    else:
        premier_passage = False

    frame_principale = tk.Frame(root, bg=b)

    title_option = tk.Label(frame_principale, image=img_option_logo, bg=b)
    dur = tk.Radiobutton(frame_principale, text='Dur', bg=b, fg='blue', font='Arial 24', value=3, variable=select_option)
    moyen = tk.Radiobutton(frame_principale, text='Moyen', bg=b, fg='blue', font='Arial 24', value=2, variable=select_option)
    facile = tk.Radiobutton(frame_principale, text='Facile', bg=b, fg='blue', font='Arial 24', value=1, variable=select_option)
    btn_escape = tk.Button(frame_principale, image=img_escape, command=menu_game, bg=b, borderwidth=0)
    btn_sauvegarder = tk.Button(frame_principale, image=img_sauvegarder, command=select,bg=b, borderwidth=0)
    btn_retour = tk.Button(frame_principale, image=img_retour, command=menu_game, bg=b, borderwidth=0)

    dur.grid(row=1, column=0)
    moyen.grid(row=1, column=1)
    facile.grid(row=1, column=2)
    btn_escape.grid(row=0, column=0)
    title_option.grid(row=0, column=1)
    btn_sauvegarder.grid(row=2, column=0, ipady=10)
    btn_retour.grid(row=2, column=1, ipady=10)
    frame_principale.pack(fill='both', expand=True)

menu_game()

root.mainloop()
