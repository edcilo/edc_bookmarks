#!/bin/sh

set -e

echo $(date '+%F %T.%3N %Z') "[flask] INFO: running start.sh"

env=${FLASK_ENV:-development}

echo $(date '+%F %T.%3N %Z') "[flask] INFO: start cron"
/usr/sbin/crond -b -l 8

if [ $env = "production" ]
then
    echo $(date '+%F %T.%3N %Z') "[flask] INFO: running production environment"
    gunicorn --bind 0.0.0.0:5000 --chdir ./ms ms:app --timeout 120 --workers=2 --access-logfile /var/log/gunicorn-access.log --error-logfile /var/log/gunicorn-error.log --log-level info
elif [ $env = 'testing' ]
then
    echo $(date '+%F %T.%3N %Z') "[flask] INFO: running testing environment"
    coverage run -m pytest
    coverage report
else
    echo $(date '+%F %T.%3N %Z') "[flask] INFO: running development environment"
    flask run --host=0.0.0.0
fi
