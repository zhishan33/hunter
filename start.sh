#! /bin/bash
echo 'start uwsgi' >> /tmp/hunter.monitor.log
uwsgi uwsgi.ini &
