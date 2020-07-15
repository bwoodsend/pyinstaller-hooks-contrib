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
Runtime hook for eventlet. See
https://github.com/pyinstaller/pyinstaller/issues/4897

Without this hook we get an error along the lines of

Traceback (most recent call last):
  File "threading.py", line 916, in _bootstrap_inner
  File "threading.py", line 864, in run
  File "socket_io_server.py", line 11, in start_server
    eventlet.wsgi.server(eventlet.listen(('', 8008)), app)
AttributeError: module 'eventlet' has no attribute 'wsgi'

Adding eventlet.wsgi as a hiddenimport does not fix this.

"""

import eventlet.wsgi

