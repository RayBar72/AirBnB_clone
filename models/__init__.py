#!/usr/bin/python3
"""Module that creates storage var"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
