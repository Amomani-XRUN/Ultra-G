import cx_Oracle



class DatabaseSQL :
    
    
    #def __init__(self):
       # self.Ultracode = []
       # self.Ultrapass= []

    def add_user_db(self):
        connstr='system/7556@localhost'
        conn = cx_Oracle.connect(connstr)
        curs = conn.cursor()
        #s1 =self.Ultracode
        #s2 =self.Ultrapass               
        curs.execute("INSERT INTO usersp(Ultracode, Ultrapass) VALUES ('Ahmadmomani',1112)")
        conn.commit()
        curs.execute("SELECT * FROM usersp") 
        print(curs.fetchall())

        add_user_db()