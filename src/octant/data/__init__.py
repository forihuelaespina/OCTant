"""
-*- coding: utf-8 -*-

File: __init__.py

This file is necessary to compile python as a package (not a module)

From: https://stackoverflow.com/questions/448271/what-is-init-py-for
The __init__.py is required to make Python treat the directories as
containing packages; this is done to prevent directories with a common
name, such as string, from unintentionally hiding valid modules that
occur later (deeper) on the module search path. In the simplest case,
__init__.py can just be an empty file, but it can also execute
initialization code for the package or set the __all__ variable.

:Log:

+-------------+--------+------------------------------------------------------+   
| Date        | Author | Description                                          |
+=============+========+======================================================+
| 28-Feb-2019 | FOE    | - Initial script.                                    |
+-------------+--------+------------------------------------------------------+   
|  3-Mar-2019 | FOE    | - Made subpackage classes visible.                   |
+-------------+--------+------------------------------------------------------+   
| 10-Mar-2019 | FOE    | - Added Settings class.                              |
+-------------+--------+------------------------------------------------------+   
|  4-Apr-2019 | FOE    | - Exported name OCTvolumeSegmentation.               |
+-------------+--------+------------------------------------------------------+   



.. seealso:: None
.. note:: None
.. todo:: None

.. sectionauthor:: Felipe Orihuela-Espina <f.orihuela-espina@inaoep.mx>
.. codeauthor:: Felipe Orihuela-Espina <f.orihuela-espina@inaoep.mx>

"""

#Make .data subpackage classes visible to main OCTant package
from .Document import Document
from .OCTscan import OCTscan
from .OCTscanSegmentation import OCTscanSegmentation
from .OCTvolume import OCTvolume
from .OCTvolumeSegmentation import OCTvolumeSegmentation
from .RetinalLayers import RetinalLayers
from .Settings import Settings


