"""
this file is used to config the gunicorn WSGI server
"""
# bind the socket
bind = "korlev-osdna-testing:8000"
# specify log file for error output
errorlog = "osdna_api.log"
# redirect stdout/stderr to Error log file
capture_output = True
# create a daemon to run the API server on the background
daemon = True
