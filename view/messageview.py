from model.messagemodel import MessageModel

class MessageView ():
    """ """
    def __init__(self):
        self.model = MessageModel()
        
    
    def new_message(self):
        content = input("Entrez le contenu de votre message :")
        author = input("Entrez votre nom :")
        self.model.write_message(content,author)
    
    def show_message(self):
        """ """
        # get the messages from the model
        messages = self.model.display_message()
        print('Bonjour et bienvenue sur le forum, voici les derniers messages : ')
        if messages:
            for message in messages:
                print("\nmessage {} : {}".format(message['id'], message['content']))
                print("Posté par {} le {} à {}".format(
                message['author'],
                message['publishing_date'].strftime("%d/%m/%Y"),
                message['publishing_date'].strftime("%H:%M")
                ))
                print("\n------------------------------")
        else:
            print("Aucun message pour le moment")