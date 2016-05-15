import os, sys

PROJECT_HOME = '/Users/tsoporan/Desktop/projects/envs/fittrack'
PATH_TO_ACTIVATE = '/Users/tsoporan/Desktop/projects/envs/fittrack/bin/activate_this.py'

# We need to activate our env and add project root to sys to access needed modules
if PROJECT_HOME not in sys.path:
    sys.path.insert(0, PROJECT_HOME)

execfile(PATH_TO_ACTIVATE, dict(__file__ = PATH_TO_ACTIVATE))

from fittrack import app
