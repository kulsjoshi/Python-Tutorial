# Logging (use logging, not print)
# Set up a logger and use levels (DEBUG, INFO, WARNING, ERROR, CRITICAL). 
# Use .exception() in except blocks to log stack trace.

# Why logging > print
# Can change level (DEBUG/INFO) without code changes
# Can direct output to files, syslog, etc.
# Keeps timestamps and module info

import logging

logging.basicConfig(
    level = logging.INFO,
    format = "%(asctime)s %(levelname)s %(name)s: %(message)s"
)
logger = logging.getLogger(__name__)

def read_int_from_user():
    try:
        return int(input("Enter a number: "))
    except ValueError:
        logger.exception("User provided invalid integer")
        raise
    
read_int_from_user()