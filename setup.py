#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Setup script for PyGraphviz
"""
from __future__ import absolute_import
from __future__ import print_function
from __future__ import division

from glob import glob

import os
from setuptools import setup, Extension, find_packages
import sys

from setup_commands import AddExtensionDevelopCommand, AddExtensionInstallCommand

if sys.version_info < (2, 6):
    print("PyGraphviz requires Python version 2.6 or later (%d.%d detected)." %
          sys.version_info[:2])
    sys.exit(-1)

docdirbase = 'share/doc/pygraphviz'
data = [
    (docdirbase, glob("*.txt")),
    (os.path.join(docdirbase, 'examples'), glob("examples/*.py")),
    (os.path.join(docdirbase, 'examples'), glob("examples/*.dat")),
    (os.path.join(docdirbase, 'examples'), glob("examples/*.dat.gz")),
]
package_data = {'': ['*.txt'], }

with open('pygraphviz/release.py') as fp:
    exec(fp.read(), None)

if __name__ == "__main__":
    define_macros = []
    if sys.platform == "win32":
        define_macros.append(('WIN32', None))

    extension = [
        Extension(
            "pygraphviz._graphviz",
            ["pygraphviz/graphviz_wrap.c"],
            include_dirs=[],
            library_dirs=[],
            # cdt does not link to cgraph, whereas cgraph links to cdt.
            # thus, cdt needs to come first in the library list to be sure
            # that both libraries are linked in the final built .so (if cgraph
            # is first, the implicit inclusion of cdt can lead to an incomplete
            # link list, having only cdt and preventing the module from being loaded with
            # undefined symbol errors. seen under PyPy on Linux.)
            libraries=["cdt", "cgraph"],
            define_macros=define_macros
        )
    ]

    setup(
        name=name,
        use_scm_version={
            'version_scheme': 'guess-next-dev',
            'local_scheme': 'dirty-tag',
            'write_to': 'pygraphviz/_version.py'
        },

        setup_requires=[
            'setuptools>=18.0',
            'setuptools-scm>1.5.4'
        ],
        author=authors['Hagberg'][0],
        author_email=authors['Hagberg'][1],
        description=description,
        keywords=keywords,
        long_description=long_description,
        license=license,
        platforms=platforms,
        url=url,
        download_url=download_url,
        classifiers=classifiers,
        packages=find_packages(),
        data_files=data,
        ext_modules=extension,
        cmdclass={
            'install': AddExtensionInstallCommand,
            'develop': AddExtensionDevelopCommand,
            },
        package_data=package_data,
        include_package_data = True,
        test_suite='nose.collector',
        tests_require=['nose>=0.10.1', 'doctest-ignore-unicode>=0.1.0',],
    )
