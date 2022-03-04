#!/usr/bin/python3
"""
Import modules
"""

from models.engine import file_storage
import relad

storage = file_storage.FileStorage()
storage.reload()

