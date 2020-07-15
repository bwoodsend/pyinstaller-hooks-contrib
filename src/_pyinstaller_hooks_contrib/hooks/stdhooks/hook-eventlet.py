#-----------------------------------------------------------------------------
# Copyright (c) 2005-2020, PyInstaller Development Team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
#
# The full license is in the file COPYING.txt, distributed with this software.
#
# SPDX-License-Identifier: Apache-2.0
#-----------------------------------------------------------------------------

"""
Collects hiddenimports for eventlet. See
https://github.com/pyinstaller/pyinstaller/issues/4897

"""

from PyInstaller.utils.hooks import collect_submodules

hiddenimports = collect_submodules("eventlet")
hiddenimports += collect_submodules("dns")
hiddenimports.append("engineio.async_drivers.threading")

