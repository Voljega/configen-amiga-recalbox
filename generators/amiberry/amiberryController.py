import recalboxFiles
from generators.Generator import Generator
import os.path
import glob
import sys
import shutil

def generateControllerConf(fUaeConfig) :
    
    # ----- Controllers configuration ----- 
    fUaeConfig.save("config_version","2.8.1")
    fUaeConfig.save("joyport0","mouse")
    fUaeConfig.save("joyport0autofire","none")
    fUaeConfig.save("joyport0mode","mouse")
    fUaeConfig.save("joyportname0","MOUSE0")
    fUaeConfig.save("joyport1","joy0")
    fUaeConfig.save("joyport1autofire","normal")
    fUaeConfig.save("joyport1mode","djoy")
    fUaeConfig.save("joyportname1","JOY1")
    fUaeConfig.save("input.autofire_speed","0")
    fUaeConfig.save("input.mouse_speed","100")
    
def generateSpecialKeys(fUaeConfig,controller) :
    hotkeyId = controller.inputs['hotkey'].id
    selectId = controller.inputs['start'].id
    fUaeConfig.save("button_for_menu",selectId)
    fUaeConfig.save("button_for_quit",hotkeyId)
    