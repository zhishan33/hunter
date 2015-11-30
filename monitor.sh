#! /bin/bash

SHELL=/bin/bash
STARTFILE=/opt/hunteramos/hunter/start.sh
LOG=/tmp/hunter.monitor.log
echo 'check uwsgi' >> $LOG
set -x

pid=`ps aux | grep uwsgi | grep -v 'grep' | grep -v shell | awk '{{printf"%s ", $2}}'`


# find process
if [ -n "$pid" ]; then
    echo "pid:$pid"
    echo "uwsgi are running"
    exit

else
    echo "uwsgi are not running" >> $LOG
    $SHELL $STARTFILE >> $LOG 

    if [ -z "$pid" ]; then
        echo "[Failed]"
    fi
fi
