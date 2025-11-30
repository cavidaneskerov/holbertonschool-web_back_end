#!/usr/bin/env python3
"""Select with specifics"""

def schools_by_topic(mongo_collection, topic):
    """Select with pymongo"""
   return list(mongo_collection.find({ "topic": topic}))
