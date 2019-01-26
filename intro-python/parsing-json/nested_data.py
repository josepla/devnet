#!/usr/bin/env python
"""Working with nested data hands-on exercise / coding challenge."""


import json
import os


# Get the absolute path for the directory where this file is located "here"
here = os.path.abspath(os.path.dirname(__file__))


with open(os.path.join(here, "interfaces.json")) as file:
    # TODO: Parse the contents of the JSON file into a variable

    json_data=json.loads(file.read())

#    print(json_data)


# TODO: Loop through the interfaces in the JSON data and print out each
# interface's name, ip, and netmask.


for interface in json_data["ietf-interfaces:interfaces"]["interface"]:
    if interface["enabled"] == True:
        valor_enabled="Enabled Interface"
    else:
        valor_enabled="Disabled Interface"
    print("{name}: {ip}/{mask} - {enabled}".format(
    name=interface["name"],
    ip=interface["ietf-ip:ipv4"]["address"][0]["ip"],
    mask=interface["ietf-ip:ipv4"]["address"][0]["netmask"],
    enabled=valor_enabled,
    ))
