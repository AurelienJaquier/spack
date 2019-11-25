# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack import *


class Mvdtool(CMakePackage):
    """Reader library and tool for neuroscientific node formats (MVD, Sonata).
    For the Python bindings please see py-mvdtool
    """

    homepage = "https://github.com/BlueBrain/MVDTool"
    url      = "https://github.com/BlueBrain/MVDTool.git"
    git      = "https://github.com/BlueBrain/MVDTool.git"

    version('develop', clean=False, submodules=True)
    version('2.3.1', tag='v2.3.1', clean=False)
    version('2.3.0', tag='v2.3.0', clean=False)
    version('2.2.1', tag='v2.2.1', clean=False)
    version('2.2.0', tag='v2.2.0', clean=False)
    version('2.1.0', tag='v2.1.0', clean=False)
    version('2.0.0', tag='v2.0.0', clean=False)
    version('1.5.1', tag='v1.5.1')
    version('1.5', tag='v1.5')
    version('1.4', tag='v1.4')

    variant('mpi', default=True, description="Enable MPI backend")

    depends_on('boost')
    depends_on('cmake', type='build')

    depends_on('hdf5+mpi', when='+mpi')
    depends_on('hdf5~mpi', when='~mpi')
    depends_on('highfive+mpi', when='+mpi')
    depends_on('highfive~mpi', when='~mpi')
    depends_on('mpi', when='+mpi')

    depends_on('libsonata+mpi', when='@2.1: +mpi')
    depends_on('libsonata~mpi', when='@2.1: ~mpi')

    def cmake_args(self):
        args = []
        if self.spec.satisfies('+mpi'):
            args.extend([
                '-DCMAKE_C_COMPILER:STRING={}'.format(self.spec['mpi'].mpicc),
                '-DCMAKE_CXX_COMPILER:STRING={}'.format(self.spec['mpi'].mpicxx),
            ])
        return args

