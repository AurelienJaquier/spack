# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyEquation(PythonPackage):
    """General Equation Parser and Evaluator"""

    homepage = "https://github.com/glenfletcher/Equation"
    url = "https://pypi.io/packages/source/e/equation/Equation-1.2.01.tar.gz"

    version('1.2.01', sha256='c8a21dc47d6c748fd19b6485978cf8c42fe31c43db7f44789d95fb5e9752b81c', preferred=True)

    depends_on('py-setuptools', type=('build', 'run'))
