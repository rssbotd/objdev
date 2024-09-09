# This file is placed in the Public Domain.


"objects broker"


rpr = object.__repr__


from .object import Object, values


class Broker:

    "Fleet"

    objs = Object()

    @staticmethod
    def all():
        "return all objects."
        return values(Broker.objs)

    @staticmethod
    def get(orig):
        "return object by matching repr."
        return getattr(Broker.objs, orig, None)

    @staticmethod
    def register(obj):
        "add bot."
        setattr(Broker.objs, rpr(obj), obj)


def __dir__():
    return (
        'Broker',
    )
