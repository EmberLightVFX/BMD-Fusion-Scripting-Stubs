from typing import TypedDict, Any


class PropertyData(TypedDict):
    return_type: str
    short_help: str
    description: str
    access_class: str


class MethodData(TypedDict):
    usage: list[str]
    short_help: str
    description: str


class ObjectData(TypedDict):
    name: str
    methods: dict[str, MethodData]
    properties: dict[str, PropertyData]
    registry: list[dict[str, Any]]
