# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyPyjwt(PythonPackage):
    """JSON Web Token implementation in Python"""

    homepage = "https://github.com/jpadilla/pyjwt"
    url      = "https://pypi.io/packages/source/P/PyJWT/PyJWT-1.7.1.tar.gz"

    version('2.0.1', sha256='a5c70a06e1f33d81ef25eecd50d50bd30e34de1ca8b2b9fa3fe0daaabcf69bf7')
    version('1.7.1', sha256='8d59a976fb773f3e6a39c85636357c4f0e242707394cadadd9814f5cbaa20e96')

    variant('crypto', default=False, description='Build with cryptography support')

    depends_on('python@2.7:2.8,3.4:', type=('build', 'run'))
    depends_on('py-setuptools', type='build')
    depends_on('py-cryptography@1.4:', when='+crypto', type=('build', 'run'))
    depends_on('py-pytest@4.0.1:4.99.99', type='test')
    depends_on('py-pytest-cov@2.6.0:2.99.99', type='test')
    depends_on('py-pytest-runner@4.2:4.99', type='test')
