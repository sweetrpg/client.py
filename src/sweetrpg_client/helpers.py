# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""Helpers.
"""

import logging


__logger = logging.getLogger(__name__)


def _flatten_object(obj):
    """

    """
    __logger.debug("obj: %s", obj)

    fields = list(filter(lambda s: not s.startswith('_'), dir(obj.fields)))
    __logger.debug("fields: %s", fields)
    flattened = {'id': obj.id}
    for k in fields:
        try:
            flattened[k] = obj.attributes[k]
        except:
            __logger.debug("value not found for key %s in object %s", k, obj)
    __logger.debug("flattened: %s", flattened)

    return flattened
