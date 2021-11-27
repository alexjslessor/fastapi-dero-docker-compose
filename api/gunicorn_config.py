"""gunicorn server configuration."""
from os import environ
# from .backend.config.config import get_settings
# from multiprocessing import cpu_count

# settings = get_settings()
# PORT = settings.PORT
# assert PORT == 8080

# set these next
# --graceful-timeout 300000
# --keep-alive 300000
    
    
# https://docs.gunicorn.org/en/latest/settings.html#loglevel
# loglevel = 'error'

# https://docs.gunicorn.org/en/latest/settings.html#errorlog
# log_file = ''

# https://docs.gunicorn.org/en/latest/settings.html#capture-output
# capture_output = True

# https://pythonspeed.com/articles/gunicorn-in-docker/
# https://docs.gunicorn.org/en/latest/settings.html#workers
# DEFAULT: 1
workers = 1
# workers = 4

# workers = cpu_count() * 2 + 1

# https://docs.gunicorn.org/en/latest/settings.html#threads
# DEFAULT: 1
# threads = 0
threads = 2
# threads = 8
# threads = (2 - 4) * workers


# https://docs.gunicorn.org/en/latest/settings.html#timeout
# Workers silent for more than this many seconds are killed and restarted.
# Default: 30

# try this next?
# timeout = 30

timeout = 300
# timeout is 300

# Default: ['127.0.0.1:8000']
bind = f":{environ.get('PORT', '8080')}"
# bind = "127.0.0.1:8000"

# https://docs.gunicorn.org/en/latest/faq.html#how-do-i-avoid-gunicorn-excessively-blocking-in-os-fchmod
# DEFAULT: None
worker_temp_dir = '/dev/shm'

# https://docs.gunicorn.org/en/latest/settings.html#worker-class
# DEFAULT: sync
worker_class = 'gthread'
worker_class = "uvicorn.workers.UvicornWorker"

# bind = f":{environ.get('PORT', '8080')}"
# workers = 4
# threads = 8
# timeout = 30
# worker_class = 'uvicorn.workers.UvicornWorker'