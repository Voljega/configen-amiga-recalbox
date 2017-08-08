import recalboxFiles
from generators.Generator import Generator
import os.path
import glob
import sys
import shutil


def generateControllerConf(fUaeConfig) :
    # ----- Controllers configuration ----- 
    fUaeConfig.write("config_version=2.8.1\n")
    #fUaeConfig.write("pandora.joy_conf=0\n")
    #fUaeConfig.write("pandora.joy_port=0\n")
    #fUaeConfig.write("pandora.custom_dpad=1\n")
    #fUaeConfig.write("pandora.button1=2\n")
    #fUaeConfig.write("pandora.button2=1\n")
    fUaeConfig.write("joyport0=mouse\n")
    fUaeConfig.write("joyport0autofire=none\n")
    fUaeConfig.write("joyport0mode=mouse\n")
    fUaeConfig.write("joyportname0=MOUSE0\n")
    fUaeConfig.write("joyport1=joy0\n")
    fUaeConfig.write("joyport1autofire=normal\n")
    fUaeConfig.write("joyport1mode=djoy\n")
    fUaeConfig.write("joyportname1=JOY1\n")
    fUaeConfig.write("input.autofire_speed=0\n")
    fUaeConfig.write("input.mouse_speed=100\n")
    fUaeConfig.write("button_for_menu=2\n")
    fUaeConfig.write("button_for_quit=3\n")