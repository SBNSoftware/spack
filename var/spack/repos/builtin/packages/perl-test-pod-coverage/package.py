# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlTestPodCoverage(PerlPackage):
    """Check for pod coverage in your distribution"""

    homepage = "https://metacpan.org/pod/Test::Pod::Coverage"
    url = "https://cpan.metacpan.org/authors/id/N/NE/NEILB/Test-Pod-Coverage-1.10.tar.gz"

    maintainers("greenc-FNAL", "EbiArnie", "gartung", "marcmengel")

    license("Artistic-2.0")

    version("1.10", sha256="48c9cca9f7d99eee741176445b431adf09c029e1aa57c4703c9f46f7601d40d4")
    version("1.09_01", sha256="d0d5df9063bec4d652b780a4c39ddf48530f52c5f419146089b693b3ea265000")

    depends_on("perl@5.6.0:", type=("build", "link", "run", "test"))

    depends_on("perl-extutils-makemaker", type="build")

    depends_on("perl-pod-coverage", type=("build", "run", "test"))
