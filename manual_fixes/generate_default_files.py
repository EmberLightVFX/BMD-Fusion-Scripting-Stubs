def generateBuiltins() -> str:
    return '''\
"""
v1.3
Generated with FMD Fusion Scriptsing Stubs
https://github.com/EmberLightVFX/BMD-Fusion-Scripting-Stubs

Generated with Fusion Studio 18.5 build 73

"""

# Fusion objects
from _tool_scripts import (
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


def generateToolClass() -> str:
    return """\
from Operator import Operator_

Tool_ = Operator_

"""


def generateToolScripts() -> str:
    return """\
from Fusion import Fusion_
from Composition import Composition_
from Tool import Tool_

fusion = Fusion_()
fu = Fusion_()
app = Fusion_()

composition = Composition_()
comp = Composition_()

tool = Tool_()

"""
