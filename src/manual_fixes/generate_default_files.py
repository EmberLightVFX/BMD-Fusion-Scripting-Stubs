def generate_builtins() -> str:
    return '''\
"""
v2.0
Generated with FMD Fusion Scriptsing Stubs
https://github.com/EmberLightVFX/BMD-Fusion-Scripting-Stubs

Generated with Fusion Studio 20.2.3

"""

# Fusion objects
from ._tool_scripts import (
    fusion,
    fu,
    app,
    composition,
    comp,
    tool,
)

__all__ = [
    "fusion",
    "fu",
    "app",
    "composition",
    "comp",
    "tool"
]

# Stubs objects
'''


def generate_tool_class() -> str:
    return """\
from Operator import Operator

Tool = Operator

"""


def generate_tool_scripts() -> str:
    return """\
from Fusion import Fusion
from Composition import Composition
from Tool import Tool

fusion = Fusion() # type: ignore
fu = Fusion() # type: ignore
app = Fusion() # type: ignore

composition = Composition() # type: ignore
comp = Composition() # type: ignore

tool = Tool() # type: ignore

"""
