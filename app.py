import tkinter
run = True
print("Välkomen till påsen🧳")
print()


bag = []
while run:
    print("Visa inehållet i påsen[V]\n")
    print("Avsluta programet[Q]\n")
    print("Spara i påse[S]\n")
    print("Sök efter inehåll[F]\n")
    print("Radera alt inehåll[R]\n")

    choice = input("Välj ")
    if choice.lower() == 'v':
        for thing in bag:
            print(thing)
    elif choice.lower() =='s':
        bag.append(input("Skriv vad du vil spara "))
        print()
        print(f"Sparade {bag[len(bag)-1]} i påsen")
        print()
    elif choice.lower() == 'r':
        print("Raderar allt inehåll i påsen")
        bag.clear()
    elif choice.lower() == 'q':
        run = False
    elif choice.lower() == "f":
        query = input("Vad vill du söka ")
        if query.lower() in bag:
            print(f"hittade: {query} i bag")
            if query.lower() in bag:
                tabort = input("Vill du ta bort det?[J/N] ")
                if tabort.lower() == "j":
                    bag.remove(query)
                    print("Klart!")
                    if tabort.lower() == "N":
                        print("ok") 
        else:
            print(f"hittade inte: {query} i bag")
    else:
        print("Felaktigt")
print()
print("Hejdå👋")   
   
 
   
   
   
