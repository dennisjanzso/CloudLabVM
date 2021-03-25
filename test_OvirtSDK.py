#!/usr/local/Cellar/ansible/2.7.10/libexec/bin/python3

from distutils.version import LooseVersion
from enum import Enum
import ovirtsdk4 as sdk
import ovirtsdk4.version as sdk_version
HAS_SDK = (LooseVersion(sdk_version.VERSION) >= LooseVersion('4.2.4'))
if HAS_SDK:
  print("Version OK")
else:
  print("Version FAIL")