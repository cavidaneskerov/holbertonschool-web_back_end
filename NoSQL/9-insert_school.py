#!/usr/bin/env python3
"""Python with mongodb"""

def insert_school(mongo_collection, **kwargs):
    """Insert new elements"""
    new_doc = mongo_collection.insert_one(kwargs)
    return new_doc.inserted_id
