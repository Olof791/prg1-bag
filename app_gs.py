import tkinter
main = tkinter.Tk()
#main.geometry("800x800")

inventory = []

label = tkinter.Label(main, text="Välkomen till påsen🧳")
label.pack(pady= 20)
text_box = tkinter.Text(main, height = 15)
text_box.pack()

input_text = tkinter.Entry(main)
input_text.pack()

def add_to_bag(event = None):
    item = input_text.get().strip()
    if not item:
        return
    inventory.append(item)
    text_box.insert(tkinter.END, item + "\n")
    input_text.delete(0, tkinter.END)
input_text.bind('<Return>', add_to_bag)


def remove_from_bag():
    item = input_text.get().strip()
    if item in inventory:
        inventory.remove(item)
        text_box.delete("1.0", tkinter.END)
        for i in inventory:
            text_box.insert(tkinter.END, i + "\n")
    else: 
        print(f"{item} fanns ej i påsen")

remove_button = tkinter.Button(main, text="Radera något från påsen", command= remove_from_bag)
remove_button.pack(pady=10)


add_button = tkinter.Button(main, text="Spara i påsen", command= add_to_bag)
add_button.pack(pady= 10)

quitButton = tkinter.Button(main, text="Avsluta programet", command=main.quit)
quitButton.pack(pady= 20)

main.mainloop()