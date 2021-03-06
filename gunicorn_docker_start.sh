#!/bin/bash

# As seen in http://tutos.readthedocs.org/en/latest/source/ndg.html

CMJ_DIR="/var/cmjatai/cmj"

# Seta um novo diretório foi passado como raiz para o SAPL
# caso esse tenha sido passado como parâmetro
if [ "$1" ]
then
    CMJ_DIR="$1"
fi

NAME="CMJ"                                     # Name of the application (*)
DJANGODIR=/var/cmjatai/cmj/                    # Django project directory (*)
SOCKFILE=/var/cmjatai/cmj/run/gunicorn.sock    # we will communicate using this unix socket (*)
USER=`whoami`                                   # the user to run as (*)
GROUP=`whoami`                                  # the group to run as (*)
NUM_WORKERS=3                                   # how many worker processes should Gunicorn spawn (*)
                                                # NUM_WORKERS = 2 * CPUS + 1
TIMEOUT=60
MAX_REQUESTS=100                                # number of requests before restarting worker
DJANGO_SETTINGS_MODULE=cmj.settings            # which settings file should Django use (*)
DJANGO_WSGI_MODULE=cmj.wsgi                    # WSGI module name (*)

echo "Starting $NAME as `whoami` on base dir $CMJ_DIR"

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

mkdir -p /var/log/cmj/

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --log-level debug \
  --timeout $TIMEOUT \
  --workers $NUM_WORKERS \
  --max-requests $MAX_REQUESTS \
  --user $USER \
  --access-logfile /var/log/cmj/access.log \
  --error-logfile /var/log/cmj/error.log \
  --bind=unix:$SOCKFILE
