#!/usr/bin/env python3
"""function that lists all documents in a collection"""




def list_all(mongo_collection):
    """retrieve all document from the collection"""
    all_documents = mongo_collection.find({})
    document_list = list(all_documents)
    return document_list
