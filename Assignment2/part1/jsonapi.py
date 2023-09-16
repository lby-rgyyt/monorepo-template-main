import json


class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        objName = type(obj).__name__
        try:
            encoder = getattr(self, f"encode_{objName}")
        except AttributeError:
            super().default(obj)
        else:
            encode = encoder(obj)
            encode["__extendedJsonType__"] = objName
            return encode

    def encode_complex(self, obj):
        return {"real": obj.real, "imag": obj.imag}

    def encode_range(self, obj):
        return {"start": obj.start, "stop": obj.stop, "step": obj.step}


class MyDecoder(json.JSONDecoder):
    def __init__(self, **kwargs):
        kwargs["object_hook"] = self.object_hook
        super().__init__(**kwargs)

    def object_hook(self, obj):
        try:
            objName = obj["__extendedJsonType__"]
            decoder = getattr(self, f"decode_{objName}")
        except (KeyError, AttributeError):
            return obj
        else:
            return decoder(obj)

    def decode_complex(self, obj):
        return complex(obj["real"], obj["imag"])

    def decode_range(self, obj):
        return range(obj["start"], obj["stop"], obj["step"])
