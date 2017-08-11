#!/usr/bin/env python
import Command
import recalboxFiles
from generators.Generator import Generator
import os.path
import glob
import sys
import adfGenerator
import whdlGenerator

uae4armPath="/recalbox/share/emulateurs/amiga/uae4arm"
mountPoint="/tmp/amiga"

class AmigaGenerator(Generator):
    # Main entry of the module
    # Return command
    def generate(self, system, rom, playersControllers):
        print("Amiga Emulation")
        print("Params : <%s>, <%s>" % (system.name, rom))
        
        #------------ CHECK entry params ------------
        if not os.path.exists(rom) or os.path.isdir(rom):
            sys.exit("Please execute this script on full path to an uae or adf like /recalbox/share/roms/amiga/gamename.uae\nFor uae file, the game folder should be named exactly alike and be in the same folder : /recalbox/share/roms/amiga/gamename")
        
        #command params
        uaeName = os.path.basename(rom)
        romFolder = os.path.dirname(rom)
        romType= uaeName[-3:]
        gameName= uaeName[0:len(uaeName)-4]
        
        #detect bad parameters
        if not uaeName or not romFolder or not gameName or not len(romType)==3 or romType.lower() not in ['adf','uae'] :
            sys.exit("Please execute this script on an uae or adf file only")
        
        print("Launching game <%s> of type <%s> from <%s>" % (gameName,romType,romFolder))
        
        #------------ Launch ADF ------------
        if	romType == "adf" :
            if not os.path.exists(os.path.join(romFolder,uaeName)) :
                sys.exit("ADF file "+romFolder + "/" + uaeName +"doesn't exist")
            
            adfGenerator.generateAdf(rom,romFolder,uaeName,system.name)
            
            # mandatory change of current working dir to uae4arm's one
            os.chdir(os.path.join(mountPoint,"uae4arm"))
            print("Executing %s in %s" % ("uae4arm",os.getcwd()))
            os.popen("./uae4arm")
            
        #------------ Launch WHD ------------
        elif romType == "uae" :
            whdlDir = os.path.join(romFolder,gameName)
            if not os.path.exists(whdlDir) or not os.path.isdir(whdlDir):
                sys.exit("No WHDLoad folder <"+whdlDir+"> corresponding to your uae file "+  romFolder+"/"+uaeName)
            
            whdlGenerator.generateWHDL(rom,romFolder,gameName,system.name)
            
            # mandatory change of current working dir to uae4arm's one
            os.chdir(os.path.join(mountPoint,"uae4arm"))
            print("Executing uae4arm -f %s in %s" %(os.path.join(mountPoint,"WHDL",uaeName),os.getcwd()))
            os.popen('./uae4arm -f "'+os.path.join(mountPoint,"WHDL",uaeName)+'"')
            
            whdlGenerator.handleBackup(rom,romFolder,gameName,system.name)
            
        sys.exit()
        # Find rom path
#        gameDir = rom
#        batFile = gameDir + "/dosbox.bat"
#        gameConfFile = gameDir + "/dosbox.cfg"
#           
#        commandArray = ["dosbox", 
#			"-userconf", 
#			"-exit", 
#			"""{}""".format(batFile),
#			"-c", """set ROOT=""{}""".format(gameDir)]
#        if os.path.isfile(gameConfFile):
#            commandArray.append("-conf")
#            commandArray.append("""{}""".format(gameConfFile))
#			
#        return Command.Command(videomode='default', array=commandArray)
        return None
    
