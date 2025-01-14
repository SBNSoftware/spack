# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlCanaryStability(PerlPackage):
    """Canary to check perl compatibility for schmorp's modules"""

    homepage = "https://metacpan.org/pod/Canary::Stability"
    url = "https://cpan.metacpan.org/authors/id/M/ML/MLEHMANN/Canary-Stability-2013.tar.gz"

    maintainers("greenc-FNAL", "EbiArnie", "gartung", "marcmengel")

    version("2013", sha256="a5c91c62cf95fcb868f60eab5c832908f6905221013fea2bce3ff57046d7b6ea")
    version("2012", sha256="fd240b111d834dbae9630c59b42fae2145ca35addc1965ea311edf0d07817107")

    depends_on("perl-extutils-makemaker", type="build")
