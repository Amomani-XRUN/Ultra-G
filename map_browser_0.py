from kivy.base import runTouchApp
from kivy.uix.dropdown import DropDown 
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.lang import Builder

if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))


      

root = Builder.load_string("""
#:import MapSource mapview.MapSource

<Toolbar@BoxLayout>:
    size_hint_y: None
    height: '48dp'
    padding: '4dp'
    spacing: '4dp'

    canvas:
        Color:
            rgba: .2, .2, .2, .6
        Rectangle:
            pos: self.pos
            size: self.size

<ShadedLabel@Label>:
    size: self.texture_size
    canvas.before:
        Color:
            rgba: .2, .2, .2, .6
        Rectangle:
            pos: self.pos
            size: self.size


               

RelativeLayout:

    MapView:
        id: mapview
        lat: 3.140853
        lon: 101.693207
        zoom: 8
        #size_hint: .5, .5
        #pos_hint: {"x": .25, "y": .25}

        #on_map_relocated: mapview2.sync_to(self)
        #on_map_relocated: mapview3.sync_to(self)

        MapMarker:
            lat: 3.140853
            lon: 101.693207

        MapMarker
            lat: -33.867
            lon: 151.206

    Toolbar:
        top: root.top
    
        
        Button:
            text: "Kota Damansara "
            background_color: (0.1,0.5,0.6,1)
            on_release: mapview.center_on(3.1622,101.5869)
        Button:
            text: "kuala Lumpur "
            background_color: (0.1,0.5,0.6,1)
            on_release: mapview.center_on(3.1390, 101.6869)
        Button:
            text: "Putajaya "
            background_color: (0.1,0.5,0.6,1)
            on_release: mapview.center_on(2.9175, 101.6851) 
        Button:
            text: "Selayang "
            background_color: (0.1,0.5,0.6,1)
            on_release: mapview.center_on(3.2637, 101.6538)      

        
        Spinner:
            text: "Map view"
            values: MapSource.providers.keys()
            on_text: mapview.map_source = self.text

    Toolbar:
        Label:
            text: "Longitude: {}".format(mapview.lon)
        Label: 
            text: "Latitude: {}".format(mapview.lat)
    """)

runTouchApp(root)
