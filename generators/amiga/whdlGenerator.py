import recalboxFiles
from generators.Generator import Generator
import os.path
import glob
import sys
import shutil
import amigaController

uae4armPath="/recalbox/share/emulateurs/amiga/uae4arm"
mountPoint="/tmp/amiga"

def generateWHDL(fullName,romPath,uaeName,amigaHardware) :
    print("execute WHDLoad : <%s>" % os.path.join(romPath,uaeName))

    # ----- cleaning mountpoint directory ----- 
    if os.path.exists(mountPoint) :
        shutil.rmtree(mountPoint)
        
    os.makedirs(mountPoint)
            # echo "execute WHDLoad on $romFolder/$uaeName"
            # # mounting 24M ram on $mountpoint  
            # echo "Mounting 24M ram on $mountPoint"
            # mount -t tmpfs -o size=24M tmpfs $mountPoint

            # # ------------ copy Amiga OS Files ------------
            # echo "Copy Amiga OS files from $osFilespath to $mountPoint"
            # cp -R $osFilespath/* $mountPoint

            # # ------------ copy game files & folder ------------
            # cd "$romFolder/$gameName"
            # for fichier in `ls`
            # do
                # echo "Copy Game File $fichier from $romFolder to $mountPoint"
                # cp -R "$fichier" $mountPoint
            # done
            # cd "$romFolder"
            # echo "Copy $uaeName from $romFolder to $mountPoint"
            # cp "$uaeName" $mountPoint

        
            # # ------------ Modify StartupSequence with right slave files ------------
            # cd $mountPoint
            # touch Startup-Sequence
            # slaveFiles=`ls *.slave`
            # if [ -z "$slaveFiles" ]; then
                # echo "slaveFiles .slave does not exist, trying .Slave"
                # slaveFiles=`ls *.Slave`
                # if [ -z "$slaveFiles" ]; then
                    # echo "This is not a valid WHD game"
                # else
                    # for slave in `ls *.Slave`
                    # do
                        # echo "use slaveFile $slave"
                        # echo "WHDload $slave Preload" >> Startup-Sequence
                    # done
                # fi	
            # else	
                # for slave in `ls *.slave`
                # do
                    # echo "use slaveFile $slave"
                    # echo "WHDload $slave Preload" >> Startup-Sequence
                # done
            # fi

            # echo "exitemu" >> Startup-Sequence
            # mv Startup-Sequence $mountPoint/S

            # # ------------ execute uae4arm ------------
            # cd $uae4armPath
            # echo "execute $uae4armPath/uae4arm on $mountPoint/$uaeName"
            # ./uae4arm -f "$mountPoint/$uaeName"

            # cd $mountPoint
            # # ------------ clean Amiga OS Files before backup of backups ------------
            # rm -rf S
            # rm -rf C
            # rm -rf Devs
            # rm "$uaeName"

            # # ------------ remaining games files used to detect saves to backup ------------
            # $scriptPath/backupAmigaSaves.sh $mountPoint "$romFolder/$gameName"

            # # ------------ unmount with -l to avoid resource busy ------------
            # umount -l $mountPoint
    