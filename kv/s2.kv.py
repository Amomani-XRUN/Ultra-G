

#KV file


class ConnectPage(GridLayout):
   
    def __init__(self, **kwargs):
     
        super().__init__(**kwargs)

        self.cols = 2 
        
        self.add_widget(Label(text='IP:'))  
        self.ip = TextInput(multiline=False)  
        self.add_widget(self.ip)

        self.add_widget(Label(text='Port:'))
        self.port = TextInput(multiline=False)
        self.add_widget(self.port)

        self.add_widget(Label(text='Username:'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)


class EpicApp(App):
    def build(self):
        return ConnectPage()


if __name__ == "__main__":
    EpicApp().run()