run = True
print("Välkomen till påsen🧳")

bag = []
while run:
    print("Visa inehållet i påsen[V]\n")
    print("Avsluta programet[Q]\n")
    print("Spara i påse[S]\n")
    
    choice = input("Välj")
    if choice.lower() == 'v':
        for thing in bag:
            print(thing)
    elif choice.lower() =='s':
        bag.append(input("Skriv vad du vil spara"))
    
   
   
   
    elif choice.lower() == 'q':
        run = False
    else:
        print("Felaktigt")
    
    
    
