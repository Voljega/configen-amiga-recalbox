import recalboxFiles
from generators.Generator import Generator
import os.path
import glob
import sys
import shutil

biosPath="/recalbox/share/bios/"

def initMountpoint(mountPoint,uae4armPath) :
    # ----- cleaning mountpoint directory ----- 
    if os.path.exists(mountPoint) :
        shutil.rmtree(mountPoint)
    
    # ----- Create & copy emulator structure -----
    print("Copy uae4arm files to %s" % mountPoint)
    os.makedirs(mountPoint+"/uae4arm")
    # TODO REDO IN PYTHON (not easily done)
    os.popen("cp -R "+uae4armPath+"/* "+mountPoint+"/uae4arm")
    
    # ----- Generate adfdir.conf -----
    # ----- Needed for right handling of bios even in whdl case -----
    adfdir = os.path.join(mountPoint,"uae4arm","conf","adfdir.conf")
    
    if os.path.exists(adfdir) :
        os.remove(adfdir)
        
    fAdfdir = open(adfdir,"a+")
    try :
        generateAdfdirConf(fAdfdir,mountPoint)
    finally :
        fAdfdir.close()
        
def generateAdfdirConf(fAdfdir,mountPoint) :
    fAdfdir.write("path="+mountPoint+"/uae4arm/adf/\n")
    fAdfdir.write("config_path="+mountPoint+"/uae4arm/conf/\n")
    fAdfdir.write("rom_path="+biosPath+"\n")
    fAdfdir.write("ROMs=4\n")
    fAdfdir.write("ROMName=KS ROM v1.3 (A500,A1000,A2000) rev 34.5 (256k) [315093-02]\n")    
    fAdfdir.write("ROMPath="+os.path.join(biosPath,"kick13.rom")+"\n")
    fAdfdir.write("ROMType=1\n")
    fAdfdir.write("ROMName=KS ROM v2.04 (A500+) rev 37.175 (512k) [390979-01]\n")
    fAdfdir.write("ROMPath="+os.path.join(biosPath,"kick20.rom")+"\n")
    fAdfdir.write("ROMType=1\n")
    fAdfdir.write("ROMName=KS ROM v3.1 (A1200) rev 40.68 (512k) [391773-01/391774-01]\n")    
    fAdfdir.write("ROMPath="+os.path.join(biosPath,"kick31.rom")+"\n")
    fAdfdir.write("ROMType=1\n")
    fAdfdir.write("ROMName= AROS KS ROM (built-in) (1024k)\n")
    fAdfdir.write("ROMPath=:AROS\n")
    fAdfdir.write("ROMType=1\n")
    # apparently not needed
    # MRUDiskList=0
    # MRUCDList=0

def generateConfType(fUaeConfig) :
    fUaeConfig.save("config_hardware","true")
    fUaeConfig.save("config_host","true")

def generateGUIConf(fUaeConfig,leds='true') :
    fUaeConfig.save("use_gui","no")
    fUaeConfig.save("use_debugger","false")
    # Show status leds (Status Line)
    fUaeConfig.save("show_leds",leds)

def generateKickstartPath(fUaeConfig, amigaHardware) :
    if  amigaHardware == "amiga1200" :
        fUaeConfig.save("kickstart_rom_file",os.path.join(biosPath,"kick31.rom"))
    else :
        fUaeConfig.save("kickstart_rom_file",os.path.join(biosPath,"kick13.rom"))
        
def generateKickstartPathWHDL(fUaeConfig, amigaHardware) :
    fUaeConfig.save("rom_path",biosPath)
    if  amigaHardware == "amiga1200" :
        fUaeConfig.save("kickstart_rom_file",os.path.join(biosPath,"kick31.rom"))
    else :
        fUaeConfig.save("kickstart_rom_file",os.path.join(biosPath,"kick20.rom"))
        
    
def generateHardwareConf (fUaeConfig,amigaHardware) :
    # ----- Hardware configuration -----
    if  amigaHardware == "amiga1200" :
        print ("Amiga Hardware 1200 AGA")
        # On configure en AGA
        fUaeConfig.save("chipset","aga")
        fUaeConfig.save("chipmem_size","4")
        fUaeConfig.save("cpu_speed","max")
        fUaeConfig.save("cpu_type","68040")
        fUaeConfig.save("cpu_model","68040")
        fUaeConfig.save("fpu_model","68040")
        fUaeConfig.save("fastmem_size","8")
    else :
        print("Amiga Hardware 600 ECS")
        # Nothing much needed for a600 uae4arm does what needed just with the right kickstart
        fUaeConfig.save("fastmem_size","8")
        
    # unused stuff 
    # cpu_compatible=false
    # cpu_24bit_addressing=false

def generateZ3Mem(fUaeConfig) :
    fUaeConfig.save("z3mem_size","64")
    fUaeConfig.save("z3mem_start","0x1000000")
        
def generateGraphicConf(fUaeConfig) :
    # ----- GFX configuration -----
    fUaeConfig.save("gfx_width","640")
    fUaeConfig.save("gfx_height","256")
    fUaeConfig.save("gfx_correct_aspect","true")
    fUaeConfig.save("gfx_center_horizontal","simple")
    fUaeConfig.save("gfx_center_vertical","simple")
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
    fUaeConfig.save("sound_output","exact")
    fUaeConfig.save("sound_bits","16")
    fUaeConfig.save("sound_channels","stereo")
    fUaeConfig.save("sound_stereo_separation","7")
    fUaeConfig.save("sound_stereo_mixing_delay","0")
    fUaeConfig.save("sound_frequency","44100")
    fUaeConfig.save("sound_interpol","none")
    fUaeConfig.save("sound_filter","off")
    fUaeConfig.save("sound_filter_type","standard")
    fUaeConfig.save("sound_volume","0")
    fUaeConfig.save("sound_auto","yes")
    fUaeConfig.save("cachesize","0")
    fUaeConfig.save("synchronize_clock","yes")

    