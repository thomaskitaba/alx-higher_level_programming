#!/usr/bin/python3
"""
    get object discription
"""
import json



def class_to_json(obj):
    """ get dictionary description """

    my_dict = obj.__dict__
    return(json.dumps(my_dict))
