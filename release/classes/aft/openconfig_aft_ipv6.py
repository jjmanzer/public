
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

class openconfig_aft_ipv6(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-aft-ipv6 - based on the path /openconfig-aft-ipv6. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Submodule containing definitions of groupings for the abstract
forwarding tables for IPv6.
  """
  _pyangbind_elements = {}

  

class openconfig_aft_common(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-aft-common - based on the path /openconfig-aft-common. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Submodule containing definitions of groupings that are re-used
across multiple contexts within the AFT model.
  """
  _pyangbind_elements = {}

  

