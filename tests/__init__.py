import personlib

import os
import shutil

# remove existing database to avoid conflicts
if os.path.exists(personlib.DB_DIR):
    shutil.rmtree(personlib.DB_DIR)
