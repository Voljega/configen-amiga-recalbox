import recalboxFiles
from generators.Generator import Generator
import os.path
import glob
import sys
import shutil
import amigaController
import sys

import binascii

whdFilespath="/recalbox/share/emulateurs/GAME"
uae4armPath="/recalbox/share/emulateurs/amiga/uae4arm"
mountPoint="/tmp/amiga"

def generateWHDL(fullName,romFolder,gameName,amigaHardware) :
    print("execute WHDLoad : <%s>" % os.path.join(romFolder,gameName))

    # ----- cleaning mountpoint directory ----- 
    if os.path.exists(mountPoint) :
        shutil.rmtree(mountPoint)
        
    os.makedirs(mountPoint)    

    # ------------ copy WHDL structure Files ------------
    print("Copy Amiga OS files from %s to %s" %(whdFilespath,mountPoint))
    # TODO REDO IN PYTHON (not easily done)
    os.popen('cp -R '+whdFilespath+'/* '+mountPoint)

    # ------------ copy game folder & uae ------------
    print("Copy game folder and uae %s" % os.path.join(romFolder,gameName))
    # TODO REDO IN PYTHON (not easily done)
    os.popen('cp -R "'+os.path.join(romFolder,gameName)+'/"* '+mountPoint)
    shutil.copy2(os.path.join(romFolder,gameName+".uae"),mountPoint)

    # ------------ Create StartupSequence with right slave files ------------
    fStartupSeq = open(os.path.join(mountPoint,"S","Startup-Sequence"),"a+")
    try :
        slaveFiles = [filename for filename in os.listdir(mountPoint) if filename.endswith(".Slave") or filename.endswith(".slave")]
        print(slaveFiles)
        if len(slaveFiles)==0 :
            sys.exit("This is not a valid WHD game")
        
        for slaveFile in slaveFiles :
            print("Using slave file %s" %slaveFile)
            fStartupSeq.write("WHDload "+slaveFile+" Preload\n")
            
        fStartupSeq.write("exitemu\n")
    finally :
        fStartupSeq.close()
        
    # TODO Tweak uae file

def handleBackup(fullName,romFolder,gameName,amigaHardware) :
    # ------------ WHDL structure Files before backup of backups ------------
    shutil.rmtree(os.path.join(mountPoint,'S'))
    shutil.rmtree(os.path.join(mountPoint,'C'))
    shutil.rmtree(os.path.join(mountPoint,'Devs'))
    os.remove(os.path.join(mountPoint,gameName+".uae"))
    
    # ------------ detect changes in remaining games files for backuping saves ------------
    print("Backup changed files from %s to %s" %(mountPoint,os.path.join(romFolder,gameName)))
    backupDir(mountPoint,os.path.join(romFolder,gameName))

def backupDir(source,target) :
    # print("backup dir <%s> <%s>" %(source, target))
    for f in os.listdir(source) :
        filePath = os.path.join(source,f)
        # print ("f : %s %s" %(source,f))
        if os.path.isdir(filePath) :
            backupDir(filePath,os.path.join(target,f))
        else :
            if not os.path.exists(os.path.join(target,f)) :
                print ("new file : %s backup %s -> %s" %(f,source,target))
                # TODO REDO IN PYTHON (not easily done)
                if os.path.isdir(os.path.join(source,f)) :
                    os.popen('cp -R "'+os.path.join(source,f)+'/"* "'+target+'"')
                else :
                    shutil.copy2(os.path.join(source,f),target)
			
            else :
                sourceCRC32 = CRC32_from_file(os.path.join(source,f))
                targetCRC32 = CRC32_from_file(os.path.join(target,f))
                if not sourceCRC32 == targetCRC32 :
                    print ("changed file : %s backup %s -> %s" %(f,source,target))
                    # TODO REDO IN PYTHON (not easily done)
                    shutil.copy2(os.path.join(source,f),target)

def CRC32_from_file(filename):
    buf = open(filename,'rb').read()
    buf = (binascii.crc32(buf) & 0xFFFFFFFF)
    return "%08X" % buf
   