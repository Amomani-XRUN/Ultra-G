import datetime
from DatabaseSQL import *


class DataBase:
    def __init__(self,filename):
        self.filename = filename
        self.usersp = None
        self.file=None
        self.load()

    def load(self):
        self.file = open(self.filename, "r")
        self.usersp = {}

        for line in self.file:
            Ultracode, Ultrapass, created = line.strip().split(";")
            self.usersp[Ultracode] = (Ultrapass, created)

        self.file.close()

    def get_user(self, Ultracode):
        if Ultracode in self.usersp:
            return self.usersp[Ultracode]
        else:
            return -1

    def add_user(self, Ultracode,Ultrapass):
        if Ultracode.strip() not in self.usersp:
            self.usersp[Ultracode.strip()] = (Ultrapass.strip(), DataBase.get_date())
            self.save()
            return 1
        else:
            print("Email exists already")
            return -1

    def validate(self, Ultracode, Ultrapass):
        if self.get_user(Ultracode) != -1:
            return self.usersp[Ultracode][0] == Ultrapass
        else:
            return False

    

    @staticmethod
    def get_date():
        return str(datetime.datetime.now()).split(" ")[0]