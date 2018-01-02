
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

class openconfig_segment_routing(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-segment-routing - based on the path /openconfig-segment-routing. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration and operational state parameters relating to the
segment routing. This module defines a number of elements which are
instantiated in multiple places throughout the OpenConfig collection
of models.

Particularly:
 - SRGB+LB dataplane instances - directly instantied by SR.
 - SRGB+LB dataplane reservations - instantiated within MPLS and future SR
                                 dataplanes.
 - SR SID advertisements - instantiated within the relevant IGP.
 - SR-specific counters - instantied within the relevant dataplane.
  """
  _pyangbind_elements = {}

  

