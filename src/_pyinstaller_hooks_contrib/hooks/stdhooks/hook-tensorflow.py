# ------------------------------------------------------------------
# Copyright (c) 2020 PyInstaller Development Team.
#
# This file is distributed under the terms of the GNU General Public
# License (version 2.0 or later).
#
# The full license is available in LICENSE.GPL.txt, distributed with
# this software.
#
# SPDX-License-Identifier: GPL-2.0-or-later
# ------------------------------------------------------------------

from PyInstaller.utils.hooks import is_module_satisfies

if is_module_satisfies("tensorflow < 2.2.0"):
    # Pre 2.2.0: add tensorflow_core to hidden imports and let
    # the tensorflow_core.python hook collect submodules and data
    # from tensorflow_core
    hiddenimports = ['tensorflow_core']

    # 1.15.x: hidden import for tensorflow_core fails to pull in
    # tensorflow_core.python, so we need to add it manually. And even
    # then, we fail to collect a specific module...
    if is_module_satisfies("tensorflow >= 1.15.0") and is_module_satisfies("tensorflow < 2.0.0"):
        hiddenimports += ['tensorflow_core.python']
        hiddenimports += ['tensorflow_core._api.v1.compat.v2.summary.experimental']
else:
    # 2.2.0 and newer: tensorflow_core is gone; collect submodules
    # and data from tensorflow itself
    from PyInstaller.utils.hooks import collect_submodules, collect_data_files

    hiddenimports = collect_submodules('tensorflow')
    datas = collect_data_files('tensorflow')
