import tkinter, random

#dopracować!!!!!!
class Converter():

    def __init__(self, output_bot):
        self.output_bot = output_bot

    def bot_converter(output_bot):
        if output_bot == 1:
            pick = "papier"
            return pick
        elif output_bot == 2:
            pick = "kamień"
            return pick
        elif output_bot == 3:
            pick = "nożyce"
            return pick

def user_converter(user_input):
    pass
    # if user_input ==

def bot_converter(output_bot):
    if output_bot == 1:
        pick = "papier"
        return pick
    elif output_bot == 2:
        pick = "kamień"
        return pick
    elif output_bot == 3:
        pick = "nożyce"
        return pick

def paper_rock_scissors():
    user_input = int(okno_wpisu.get())
    output_bot = random.randrange(1,4)

#comparision of bot output to the user input
    if user_input == 1 and output_bot == 1:
        okno_bota.configure(text=f"Bot wybrał {bot_converter(output_bot)} i zremisował.")
    elif user_input == 1 and output_bot == 2:
        okno_bota.configure(text=f"Bot wybrał {bot_converter(output_bot)} i przegrał.")
    elif user_input == 1 and output_bot == 3:
        okno_bota.configure(text=f"Bot wybrał {bot_converter(output_bot)} i wygrał.")

    elif user_input == 2 and output_bot == 1:
        okno_bota.configure(text=f"Bot wybrał {bot_converter(output_bot)} i przegrał.")
    elif user_input == 2 and output_bot == 2:
        okno_bota.configure(text=f"Bot wybrał {bot_converter(output_bot)} i zremisował.")
    elif user_input == 2 and output_bot == 3:
        okno_bota.configure(text=f"Bot wybrał {bot_converter(output_bot)} i przegrał.")

    elif user_input == 3 and output_bot == 1:
        okno_bota.configure(text=f"Bot wybrał {bot_converter(output_bot)} i przegrał.")
    elif user_input == 3 and output_bot == 2:
        okno_bota.configure(text=f"Bot wybrał {bot_converter(output_bot)} i wygrał.")
    elif user_input == 3 and output_bot == 3:
        okno_bota.configure(text=f"Bot wybrał {bot_converter(output_bot)} i zremisował.")

root = tkinter.Tk()
polecenie = tkinter.Label(master=root, text="Wpisz papier, kamień lub nożyce (1-papier, 2-kamień, 3-nożyce)",width=50)
polecenie.pack()

okno_wpisu = tkinter.Entry(master=root)
okno_wpisu.pack()
root.title("papier, kamień, nożyce")

przycisk_zatwierdzenia = tkinter.Button(master=root, text="zatwierdź", command=paper_rock_scissors)
przycisk_zatwierdzenia.pack()

okno_bota = tkinter.Label(master=root, text="Wynik bota")
okno_bota.pack()
root.mainloop()
