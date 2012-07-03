# Create your views here.
import cocos 
from cocos.actions import *

class HelloWorld(cocos.layer.Layer):
    def __init__(self):
        super (HelloWorld, self).__init__()
            
        label = cocos.text.Label('Hello World',
            font_name ='Times New Roman',
            font_size=32,
            anchor_x='center',anchor_y='center')
           
        label.position = 320,240
        self.add(label)
        
if __name__ == "__main__":
    cocos.director.director.init()
    
    hello_layer = HelloWorld ()
    
    main_scene = cocos.scene.Scene (hello_layer)
    
    hello_layer.do( Ripple3D(center=(320,240), radius=240, waves=15, amplitude=60, duration=20, grid=(32,24) ))
    
    cocos.director.director.run(main_scene)
    
            