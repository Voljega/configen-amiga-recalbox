import recalboxFiles
from generators.Generator import Generator
import os.path
import glob
import sys
import shutil
import amigaController

uae4armPath="/recalbox/share/emulateurs/amiga/uae4arm"
mountPoint="/tmp/amiga"

def generateAdf(fullName,romPath,uaeName,amigaHardware) :
    print("execute ADF : <%s> on <%s>" %(uae4armPath+"/uae4arm",romPath + "/" + uaeName))
    
    # ----- cleaning mountpoint directory ----- 
    if os.path.exists(mountPoint) :
        shutil.rmtree(mountPoint)
    
    # ----- Create & copy emulator structure -----
    print("Copy uae4arm files to %s" % mountPoint)
    os.makedirs(mountPoint+"/uae4arm")
    # TODO REDO IN PYTHON (not easily done)
    os.popen("cp -R "+uae4armPath+"/* "+mountPoint+"/uae4arm")
    
    # ----- Create uae configuration file -----
    uaeconfig = os.path.join(mountPoint,"uae4arm","conf","uaeconfig.uae")
    
    if os.path.exists(uaeconfig) :
        os.remove(uaeconfig)
        
    fUaeConfig = open(uaeconfig,"a+")
    try :
        amigaController.generateControllerConf(fUaeConfig)
        generateGUIConf(fUaeConfig)
        generateHardwareConf(fUaeConfig,amigaHardware)
        floppiesManagement(fUaeConfig,romPath,uaeName)
        generateGraphicConf(fUaeConfig)
    finally :
        fUaeConfig.close()
    
    # ----- Generate adfdir.conf -----
    adfdir = os.path.join(mountPoint,"uae4arm","conf","adfdir.conf")
    
    if os.path.exists(adfdir) :
        os.remove(adfdir)
        
    fAdfdir = open(adfdir,"a+")
    try :
        generateAdfdirConf(fAdfdir)
    finally :
        fAdfdir.close()

def floppiesManagement(fUaeConfig,romPath,uaeName) :
    # ----- Floppies management -----
    indexDisk = uaeName.rfind("Disk 1")
    
    if indexDisk == -1 :
        # Mono disk
        fUaeConfig.write("floppy0="+os.path.join(romPath,uaeName)+"\n")
        print("Added %s as floppy0" % os.path.join(romPath,uaeName))
        fUaeConfig.write("floppy0type=0\n")
        fUaeConfig.write("nr_floppies=1\n")
        print("Number of floppies : 1")
    
    else :
        # Several disks
        prefix = uaeName[0:indexDisk+4]
        prefixed = [filename for filename in os.listdir(romPath) if filename.startswith(prefix)]
        for i in range(0,min(4,len(prefixed))) :
            fUaeConfig.write("floppy"+`i`+"="+os.path.join(romPath,prefixed[i])+"\n")
            print("Added %s as floppy%i" % (os.path.join(romPath,prefixed[i]),i))
            fUaeConfig.write("floppy"+`i`+"type=0\n")
        
        nbFloppies=min(4,len(prefixed))
        fUaeConfig.write("nr_floppies="+`nbFloppies`+"\n")
        print("Number of floppies : "+`nbFloppies`)
    
def generateGUIConf(fUaeConfig) :
    fUaeConfig.write("use_gui=no\n")
    fUaeConfig.write("use_debugger=false\n")
    # Show status leds (Status Line)
    fUaeConfig.write("show_leds=true\n")
    
def generateHardwareConf (fUaeConfig,amigaHardware) :
    # ----- Hardware configuration -----
    if  amigaHardware == "amiga1200" :
        print ("Amiga Hardware 1200 AGA")
        fUaeConfig.write("kickstart_rom_file="+mountPoint+"/uae4arm/kickstarts/kick31.rom\n")
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
        fUaeConfig.write("kickstart_rom_file="+mountPoint+"/uae4arm/kickstarts/kick13.rom\n")
        fUaeConfig.write("fastmem_size=8\n")
        
def generateGraphicConf(fUaeConfig) :
    # ----- GFX configuration -----
    fUaeConfig.write("gfx_width=640\n")
    fUaeConfig.write("gfx_height=256\n")
    fUaeConfig.write("gfx_correct_aspect=true\n")
    fUaeConfig.write("gfx_center_horizontal=simple\n")
    fUaeConfig.write("gfx_center_vertical=simple\n")

def generateAdfdirConf(fAdfdir) :
    fAdfdir.write("path="+mountPoint+"/uae4arm/adf/\n")
    fAdfdir.write("config_path="+mountPoint+"/uae4arm/conf/\n")
    fAdfdir.write("rom_path="+mountPoint+"/uae4arm/kickstarts/\n")
    fAdfdir.write("ROMs=2\n")
    fAdfdir.write("ROMName=KS ROM v1.3 (A500,A1000,A2000)\n")
    fAdfdir.write("ROMPath="+mountPoint+"/uae4arm/kickstarts/kick13.rom\n")
    fAdfdir.write("ROMType=1\n")
    fAdfdir.write("ROMName=KS ROM v3.1 (A1200)\n")
    fAdfdir.write("ROMPath="+mountPoint+"/uae4arm/kickstarts/kick31.rom\n")
    fAdfdir.write("ROMType=1\n")