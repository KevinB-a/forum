from view.messageview import MessageView

if __name__ == "__main__":    
    messageview = MessageView()
    messageview.show_message()
    answer = ""
    while answer != "q":
        while answer not in ["e","v","q"] :
            answer = input("veuillez choisir l'action a executer e pour ecrire un message, v pour consulter et q pour quitter  ")
            if answer == "e":
                messageview.new_message()
                answer = input("veuillez choisir l'action a executer e pour ecrire un message, v pour consulter et q pour quitter  ")
            if answer =="v": 
                messageview.show_message()
                answer = input("veuillez choisir l'action a executer e pour ecrire un message, v pour consulter et q pour quitter  ")
            if answer == "q":
                exit()