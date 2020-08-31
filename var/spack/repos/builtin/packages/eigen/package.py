# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Eigen(CMakePackage):
    """Eigen is a C++ template library for linear algebra matrices,
    vectors, numerical solvers, and related algorithms.
    """

    homepage = 'http://eigen.tuxfamily.org/'
    url      = 'https://gitlab.com/libeigen/eigen/-/archive/3.3.7/eigen-3.3.7.tar.gz'
    git      = 'https://gitlab.com/libeigen/eigen.git'

    version('3.3.7', sha256='d56fbad95abf993f8af608484729e3d87ef611dd85b3380a8bad1d5cbc373a57')
    version('3.3.6', sha256='e7cd8c94d6516d1ada9893ccc7c9a400fcee99927c902f15adba940787104dba')
    version('3.3.5', sha256='383407ab3d0c268074e97a2cbba84ac197fd24532f014aa2adc522355c1aa2d0')
    version('3.3.4', sha256='c5ca6e3442fb48ae75159ca7568854d9ba737bc351460f27ee91b6f3f9fd1f3d')
    version('3.3.3', sha256='837d5f54393d1310cb4eae680b198dd49e3902f561d9c8ce7ed64f29630fbf6c')
    version('3.3.2', sha256='8d7611247fba1236da4dee7a64607017b6fb9ca5e3f0dc44d480e5d33d5663a5')
    version('3.3.1', sha256='50dd21a8997fce0857b27a126811ae8ee7619984ab5425ecf33510cec649e642')
    version('3.3.0', sha256='de82e01f97e1a95f121bd3ace87aa1237818353c14e38f630a65f5ba2c92f0e1')
    version('3.2.10', sha256='0920cb60ec38de5fb509650014eff7cc6d26a097c7b38c7db4b1aa5df5c85042')
    version('3.2.9', sha256='f683b20259ad72c3d384c00278166dd2a42d99b78dcd589ed4a6ca74bbb4ca07')
    version('3.2.8', sha256='64c54781cfe9eefef2792003ab04b271d4b2ec32eda6e9cdf120d7aad4ebb282')
    version('3.2.7', sha256='0ea9df884873275bf39c2965d486fa2d112f3a64b97b60b45b8bc4bb034a36c1')

    variant('metis', default=False,
            description='Enables metis permutations in sparse algebra')
    variant('scotch', default=False,
            description='Enables scotch/pastix sparse factorization methods')
    variant('fftw', default=False,
            description='Enables FFTW backend for the FFT plugin')
    variant('suitesparse', default=False,
            description='Enables SuiteSparse sparse factorization methods')
    variant('mpfr', default=False,
            description='Enables the multi-precisions floating-point plugin')
    variant('build_type', default='RelWithDebInfo',
            description='The build type to build',
            values=('Debug', 'Release', 'RelWithDebInfo'))

    # TODO : dependency on googlehash, superlu, adolc missing
    depends_on('metis@5:', when='+metis')
    depends_on('scotch', when='+scotch')
    depends_on('fftw', when='+fftw')
    depends_on('suite-sparse', when='+suitesparse')
    depends_on('mpfr@2.3.0:', when='+mpfr')
    depends_on('gmp', when='+mpfr')

    patch('find-ptscotch.patch', when='@3.3.4')

    def setup_environment(self, spack_env, run_env):
        run_env.prepend_path('CPATH',
                             join_path(self.prefix, 'include', 'eigen3'))

    @property
    def headers(self):
        headers = find_all_headers(self.prefix.include)
        headers.directories = [self.prefix.include.eigen3]
        return headers
