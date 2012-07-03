import pygame, threading , time

class PyGameObject:
    def __init__(self,pos,parentsurface):
        self.x = pos[0]
        self.y = pos[1]
        self.parent=parentsurface
        self.Surface= pygame.Surface((50,50))
        self.Surface.fill((0,0,0))
        
    def draw(self):
        self.parent.blit(self.Surface, (self.x,self.y))
    
    def move(self,x,y):
        self.x +=x
        self.y +=y
        

class Screen:
    def __init__(self,size,name):
        pygame.init()
        self.Surface = pygame.display.set_mode(size)
        pygame.mouse.set_visible(0)
        self.Surface.fill((255,255,255))
        pygame.display.set_caption(name)
        self.resolution=size
    
    def clear(self):
        self.Surface.fill((255,255,255))
        
class Main(threading.Thread):
    
    def __init__(self):
        self.objects = []
        threading.Thread.__init__(self)
        self.stopthread = threading.Event()
        self.Screen = Screen((800,600),"game1")
        self.objects.append(PyGameObject((50,50),self.Screen.Surface))
    
    def run(self):
        while not self.stopthread.isSet():
            pygame.display.update()
            self.redrawAll()
            
    def stop(self):
        self.stopthread.set()
        
    def redrawAll(self):
        self.Screen.clear()
        for object in self.objects:
            object.draw()
        

if __name__ == "__main__":
    gui = Main()
    gui.start()
    time.sleep(2)
    gui.stop()