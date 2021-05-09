from kivy.app import App
#kivy.require("1.9.1")
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.network.urlrequest import UrlRequest
import json
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
class MyWidget(BoxLayout):
    
    def __init__(self,**kwargs):
        super(MyWidget,self).__init__(**kwargs)
        origin = "University of Toronto"
        destination = "9 Dietz Ave S"
        origin = origin.replace(" ", "+")
        destination = destination.replace(" ", "+")
        key = "AIzaSyCtdQu1BjOcEJsUVPIBWiyK2HTs1FtEymw"
        url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=metric&origins=" + origin + "&destinations=" + destination + "&mode=walking&key=" + key
        
        print(url)
        self.request = UrlRequest(url, self.res)
        print(self.request)
        print("Result: before success", self.request.result,"\n")


    def res(self,*args):
        x = self.request.result

        # json_data = json.loads(str(self.request.result))
        print(x['rows'][0]['elements'][0]['distance']['value'])

class MyApp(App):
    def build(self):
        screen = Screen()
        text = TextInput(text="input place of origin", pos_hint={'center_x':0.5,'center_y':0.5})
        screen.add_widget(text)
        return MyWidget()


if __name__ == '__main__':
    MyApp().run()