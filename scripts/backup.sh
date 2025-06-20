#!/bin/bash

SRC=~/Documents
DEST=~/Backups
DATE=$(date +%Y-%m-%d_%H-%M-%S)
FILENAME="backup_$DATE.zip"

mkdir -p "$DEST"
zip -r "$DEST/$FILENAME" "$SRC" > /dev/null

echo "✅ Backup completed: $DEST/$FILENAME"
