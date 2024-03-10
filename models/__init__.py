#!/usr/bin/python3
'''
Initialization module for the models package.

This module creates a unique instance of the FileStorage class and loads
any existing data from the JSON file into memory.
'''

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
