from __future__ import print_function

import json
import logging

log = logging.getLogger()
log.setLevel(logging.DEBUG)


def handler(event, context):
    log.error("Received event {}".format(json.dumps(event)))
    response = "I recieved - {}".format(event.get("message", "no get param"))
    return {"message": response}
