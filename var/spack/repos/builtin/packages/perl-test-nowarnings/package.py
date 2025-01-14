# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlTestNowarnings(PerlPackage):
    """Make sure you didn't emit any warnings while testing"""

    homepage = "https://metacpan.org/pod/Test::NoWarnings"
    url = "https://cpan.metacpan.org/authors/id/H/HA/HAARG/Test-NoWarnings-1.06.tar.gz"

    maintainers("greenc-FNAL", "EbiArnie", "gartung", "marcmengel")

    license("LGPL-2.1-only")

    version("1.06", sha256="c2dc51143b7eb63231210e27df20d2c8393772e0a333547ec8b7a205ed62f737")
    version("1.05_01", sha256="f8d4d7525f2dedee1cf15cda520382500c992bbcbfbc8e5fac1820ca13de8783")

    provides("perl-test-nowarnings-warning")

    depends_on("perl@5.6:", type=("build", "run", "test"))

    depends_on("perl-extutils-makemaker", type="build")
