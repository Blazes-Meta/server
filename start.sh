#!/bin/bash

MAX_RAM=3584
JAR_DATEI="SERVER DATEI"

screen -S minecraft-server -dm java -Xmx${MAX_RAM}M -Xms512M -jar ${JAR_DATEI} nogui
screen -r minecraft-server
