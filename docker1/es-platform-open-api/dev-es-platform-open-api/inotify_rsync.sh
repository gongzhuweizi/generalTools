#!/bin/sh
apt-get update && apt-get install  -y inotify-tools rsync && rsync -avPz --delete /tmp/gc_logs /home/wx/services/es-platform-open-api/logs/
inotifywait -mrq /tmp/gc_logs  --format '%w%f'  -e create,,delete,close_write,moved_to|\      
while read line
do
  rsync -avPz --delete /tmp/gc_logs /home/wx/services/es-platform-open-api/logs/
done
