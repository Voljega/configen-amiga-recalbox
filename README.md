Alpha version of configenized amiga4recalbox based on recalbox configen 2017.11.10

Do not use :)

```
<system>
     <fullname>amiga600</fullname>
     <name>amiga600</name>
     <path>/recalbox/share/roms/amiga600</path>
     <extension>.adf .Adf .ADF .uae</extension>
 	<!-- <command>/recalbox/scripts/amigalauncher.sh %ROM% 600</command> -->
    <command>python /usr/lib/python2.7/site-packages/configgen/emulatorlauncher.pyc %CONTROLLERSCONFIG% -system %SYSTEM% -rom %ROM% -emulator %EMULATOR% -core %CORE% -ratio %RATIO%</command>	
 	<platform>amiga600</platform>
     <theme>amiga600</theme>
 </system>
 <system>
     <fullname>amiga1200</fullname>
     <name>amiga1200</name>
     <path>/recalbox/share/roms/amiga1200</path>
     <extension>.adf .Adf .ADF .uae</extension>
 	<!-- <command>/recalbox/scripts/amigalauncher.sh %ROM% 1200</command>	 -->
    <command>python /usr/lib/python2.7/site-packages/configgen/emulatorlauncher.pyc %CONTROLLERSCONFIG% -system %SYSTEM% -rom %ROM% -emulator %EMULATOR% -core %CORE% -ratio %RATIO%</command>
 	<platform>amiga1200</platform>
     <theme>amiga1200</theme>
 </system>
 <system>
     <fullname>amigacd32</fullname>
     <name>amigacd32</name>
     <path>/recalbox/share/roms/amigacd32</path>
     <extension>.cue .CUE .iso .ISO</extension>
 	<!-- <command>/recalbox/scripts/amigalauncher.sh %ROM% 600</command> -->
    <command>python /usr/lib/python2.7/site-packages/configgen/emulatorlauncher.pyc %CONTROLLERSCONFIG% -system %SYSTEM% -rom %ROM% -emulator %EMULATOR% -core %CORE% -ratio %RATIO%</command>	
 	<platform>amigacd32</platform>
     <theme>amigacd32</theme>
 </system>
```



TODO :
- change filepath to use RecalboxFiles (wait for 4.1)
- use Command instead of popen
- better controller config (SDL1)
- video conf may be needed
- compile uae4arm and check subdirs
- directory recursive copy using python instead of popn