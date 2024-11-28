@echo off

set MAX_RAM=3584
set JAR_DATEI="SERVER DATEI"

start "" java -Xmx%MAX_RAM%M -Xms512M -jar %JAR_DATEI% nogui
