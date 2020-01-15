from model.connection import Connection

class MessageModel():
    """ """
    
    def __init__(self):
        self.db = Connection()
    
    
    def display_message(self):
        """method to display messages """
        self.db.initialize_connection()
        self.db.cursor.execute("SELECT * FROM message;")
        view=self.db.cursor.fetchall()
        self.db.close_connection()
        return view    
    
    def write_message(self,content, author):
        """ """ 
        self.db.initialize_connection()
        self.db.cursor.execute("INSERT INTO message(content, publishing_date, author) VALUES (%s, now(), %s);",(content,author))
        self.db.connection.commit() 
        self.db.close_connection() 