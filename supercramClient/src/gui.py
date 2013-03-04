'''

'''

import pygame


class GUIManager(): #GUI Manager - stores all overlays, primary, focus
    def __init__(self):
        self.primaryGUI = None
        self.overlays = []
        self.activeGUI = 0
        self.focusElement = None
    def openOverlay(self, overlay):
        self.overlays.append(overlay)
        self.activeGUI = len(self.overlays)-1
    def closeOverlay(self):
        self.overlays.remove(self.overlays[self.activeGUI])
        self.activeGUI -= 1
    def openPrimaryGUI(self, primary):
        self.primaryGUI = primary
        self.overlays = []
        self.activeGUI = 0
        self.focusElement = None
    def focusOnElement(self):
        pass

class GUIFrame():
    def __init__(self):
        self.elements = []
        self.displayMouse = False
        self.image = None
        self.focusElementIndex = 0
    def draw(self, screen):
        for e in self.elements:
            screen.blit(e.image, e.rect)
    def onMouseDown(self,x,y,button):
        pass
    def onMouseUp(self,x,y,button):
        pass
    def onKeyDown(self,key):
        pass
    

class GUIElement():
    def __init__(self, x,y,w,h):
        self.rect = pygame.Rect((x,y), (w,h))
        self.image = None
        self.mustHaveFocus = True
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    def onFocus(self):
        pass
    def onBlur(self):
        pass
    def onMouseDown(self,x,y,button):
        pass
    def onMouseUp(self,x,y,button):
        pass
    def onKeyDown(self,key):
        pass
    def onKeyUp(self,key):
        pass
    