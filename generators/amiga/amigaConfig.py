import recalboxFiles
from generators.Generator import Generator
import os.path
import glob
import sys
import shutil
import amigaController

uae4armPath="/recalbox/share/emulateurs/amiga/uae4arm"
mountPoint="/tmp/amiga"

def generateConfType(fUaeConfig) :
    fUaeConfig.write("config_hardware=true\n")
    fUaeConfig.write("config_host=true\n")

def generateGUIConf(fUaeConfig,leds='true') :
    fUaeConfig.write("use_gui=no\n")
    fUaeConfig.write("use_debugger=false\n")
    # Show status leds (Status Line)
    fUaeConfig.write("show_leds="+leds+"\n")

def generateKickstartPath(fUaeConfig, amigaHardware) :
    if  amigaHardware == "amiga1200" :
        fUaeConfig.write("kickstart_rom_file="+mountPoint+"/uae4arm/kickstarts/kick31.rom\n")
    else :
        fUaeConfig.write("kickstart_rom_file="+mountPoint+"/uae4arm/kickstarts/kick13.rom\n")
        
def generateKickstartPathWHDL(fUaeConfig, amigaHardware) :
    if  amigaHardware == "amiga1200" :
        fUaeConfig.write("kickstart_rom_file="+uae4armPath+"/kickstarts/kick31.rom\n")
    else :
        fUaeConfig.write("kickstart_rom_file="+uae4armPath+"/kickstarts/kick20.rom\n")
        
    
def generateHardwareConf (fUaeConfig,amigaHardware) :
    # ----- Hardware configuration -----
    if  amigaHardware == "amiga1200" :
        print ("Amiga Hardware 1200 AGA")
        # On configure en AGA
        fUaeConfig.write("chipset=aga\n")
        fUaeConfig.write("chipmem_size=4\n")
        fUaeConfig.write("cpu_speed=max\n")
        fUaeConfig.write("cpu_type=68040\n")
        fUaeConfig.write("cpu_model=68040\n")
        fUaeConfig.write("fpu_model=68040\n")
        fUaeConfig.write("fastmem_size=8\n")
    else :
        print("Amiga Hardware 600 ECS")
        # Nothing much needed for a600 uae4arm does what needed just with the right kickstart
        fUaeConfig.write("fastmem_size=8\n")

def generateZ3Mem(fUaeConfig) :
    fUaeConfig.write("z3mem_size=64\n")
    fUaeConfig.write("z3mem_start=0x1000000\n")
        
def generateGraphicConf(fUaeConfig) :
    # ----- GFX configuration -----
    fUaeConfig.write("gfx_width=640\n")
    fUaeConfig.write("gfx_height=256\n")
    fUaeConfig.write("gfx_correct_aspect=true\n")
    fUaeConfig.write("gfx_center_horizontal=simple\n")
    fUaeConfig.write("gfx_center_vertical=simple\n")
    # extra ? doesn't seem needed
    # gfx_refreshrate=0
    # gfx_vsync=true
    # gfx_lores=false
    # gfx_resolution=hires
    # gfx_framerate=0
    # immediate_blits=false
    # fast_copper=true
    # ntsc=false
    # collision_level=playfields
    
    # Old Pandora Stuff for WHDL seems totally useless
    # pandora.floppy_path=/recalbox/share/emulateurs/amiga/uae4arm/disks/
    # pandora.hardfile_path=/recalbox/share/roms/amiga/
    # ; host-specific
    # pandora.blitter_in_partial_mode=0
    # pandora.cpu_speed=600
        
def generateSoundConf(fUaeConfig) :
    # ----- Sound configuration -----
    fUaeConfig.write("sound_output=exact\n")
    fUaeConfig.write("sound_bits=16\n")
    fUaeConfig.write("sound_channels=stereo\n")
    fUaeConfig.write("sound_stereo_separation=7\n")
    fUaeConfig.write("sound_stereo_mixing_delay=0\n")
    fUaeConfig.write("sound_frequency=44100\n")
    fUaeConfig.write("sound_interpol=none\n")
    fUaeConfig.write("sound_filter=off\n")
    fUaeConfig.write("sound_filter_type=standard\n")
    fUaeConfig.write("sound_volume=0\n")
    fUaeConfig.write("sound_auto=yes\n")
    fUaeConfig.write("cachesize=0\n")
    fUaeConfig.write("synchronize_clock=yes\n")
    
    