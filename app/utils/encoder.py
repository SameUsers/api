from pydantic import BaseModel

def encode_model(obj: BaseModel) -> bytes:
    return obj.model_dump_json().encode("utf-8")