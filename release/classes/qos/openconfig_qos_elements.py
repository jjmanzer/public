
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

class openconfig_qos_elements(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-qos-elements - based on the path /openconfig-qos-elements. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This submodule defines configuration and operational state
data associated with QoS elements.  The primary elements of
the model include:

 classifiers: match packets with a specific characteristic

 forwarding groups: logical class of packets that receive
 common forwarding treatment

 queues:  collection of packets to be scheduled, including
 a queue management scheme

 schedulers: sequence of one more elements that schedule
 packets for transmission, including policer and shaper
 functions
  """
  _pyangbind_elements = {}

  

