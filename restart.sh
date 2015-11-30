#! /bin/bash
echo 'uwsgi are restarting' >> /tmp/hunter.monitor.log
killall -9 uwsgi
uwsgi uwsgi.ini &
echo 'uwsgi are running now' >> /tmp/hunter.monitor.log
