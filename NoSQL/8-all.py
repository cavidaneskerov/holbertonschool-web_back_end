#!/usr/bin/python3
"""List mongo collection"""

def list_all(mongo_collection):
    """List mongo collection"""
    return list(mongo_collection.find({}))
