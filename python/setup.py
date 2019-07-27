#!/usr/bin/env python3

"""
Setup for SWIG Python bindings for lttoolbox
"""
import platform
from os import path
from distutils.core import Extension, setup
from distutils.command.build import build
import distutils.cygwinccompiler


class CustomBuild(build):
    if platform.system() == 'Windows':
        distutils.cygwinccompiler.get_msvcr = lambda: []

        def initialize_options(self):
            super(CustomBuild, self).initialize_options()
            self.compiler = 'mingw32'

    sub_commands = [
        ('build_ext', build.has_ext_modules),
        ('build_py', build.has_pure_modules),
        ('build_clib', build.has_c_libraries),
        ('build_scripts', build.has_scripts),
    ]


def get_sources():
    sources = ['lttoolbox.i']
    cc_sources = ['alphabet.cc', 'compression.cc', 'fst_processor.cc', 'lt_locale.cc',
                  'node.cc', 'state.cc', 'trans_exe.cc', 'xml_parse_util.cc']
    rel_path = '../lttoolbox/'
    sources.extend(path.join(rel_path, f) for f in cc_sources)
    return sources

lttoolbox_module = Extension(
    name='_lttoolbox',
    sources=get_sources(),
    swig_opts = ["-c++", "-I..", "-Wall"],
    include_dirs=['..', '/usr/include/libxml2',
    r'../../externallibs/win64/libxml2-2.9.3-win32-x86_64/include/libxml2',
    r'../utf8',
    r'../../externallibs/win64/iconv-1.14-win32-x86_64/include',
    ],
    library_dirs=['/usr/include/libxml2',
    r'../../externallibs/win64/libxml2-2.9.3-win32-x86_64/lib',
    r'C:/Python37/libs',
    ],
    extra_compile_args='-Wall -Wextra -g -O2 -std=c++2a'.split(),
    extra_link_args=['-lxml2'],
)

setup(
    name='lttoolbox',
    version='3.5.0',
    description='SWIG interface to lttoolbox/lttoolbox.h',
    long_description="SWIG interface to lttoolbox/lttoolbox.h for use in apertium-python",
    # TODO: author, maintainer, url
    author_email='sortiz@users.sourceforge.net',
    license='GPL-3.0+',
    maintainer_email='sortiz@users.sourceforge.net',
    cmdclass={'build': CustomBuild},
    ext_modules=[lttoolbox_module],
    py_modules=['lttoolbox'],
)
