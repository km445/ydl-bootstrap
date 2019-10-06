# JYDL flask/celery/socketio/jquery/bootstrap application
JYDL - Jquery Youtube Downloader application

## Application demo instructions

1. Clone the project `git clone https://github.com/km445/ydl-bootstrap.git`
1. Install application virtualenv(python3.6 is recommended)/libraries which are specified in requirements.txt `pip install -r requirements.txt`. 
1. Celery configuration uses redis as result backend and rabbitmq as message broker. Install them too `sudo apt-get install redis`, `sudo apt-get install rabbitmq-server`.
1. Socketio uses separate namespace to open a socket. Configure rabbitmq like so `sudo rabbitmqctl add_vhost socketio`, `sudo rabbitmqctl set_permissions -p socketio guest "." "." ".*"`.
1. Using application virtualenv open a terminal in project root folder and run a celery worker `celery -A proj worker --loglevel=info --concurrency=50 -Q io_bound --pool=eventlet -n io_bound_worker@%h --logfile=proj/logs/celery.log`.
1. Using application virtualenv, run `python runserver.py` in a separate terminal.
1. Go to `localhost:5888` in your browser to use the application.
