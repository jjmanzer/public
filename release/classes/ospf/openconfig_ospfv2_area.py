
from operator import attrgetter
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType
from pyangbind.lib.yangtypes import RestrictedClassType
from pyangbind.lib.yangtypes import TypedListType
from pyangbind.lib.yangtypes import YANGBool
from pyangbind.lib.yangtypes import YANGListType
from pyangbind.lib.yangtypes import YANGDynClass
from pyangbind.lib.yangtypes import ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import six

# PY3 support of some PY2 keywords (needs improved)
if six.PY3:
  import builtins as __builtin__
  long = int
  unicode = str
elif six.PY2:
  import __builtin__

class openconfig_ospfv2_area(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-ospfv2-area - based on the path /openconfig-ospfv2-area. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This submodule provides OSPFv2 configuration and operational
state parameters that are specific to the area context
  """
  _pyangbind_elements = {}

  

class openconfig_ospfv2_area_interface(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-ospfv2-area-interface - based on the path /openconfig-ospfv2-area-interface. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This submodule provides OSPFv2 configuration and operational
state parameters that are specific to the area context
  """
  _pyangbind_elements = {}

  

class openconfig_ospfv2_lsdb(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-ospfv2-lsdb - based on the path /openconfig-ospfv2-lsdb. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: An OpenConfig model for the Open Shortest Path First (OSPF)
version 2 link-state database (LSDB)
  """
  _pyangbind_elements = {}

  

