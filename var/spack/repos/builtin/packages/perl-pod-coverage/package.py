# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlPodCoverage(PerlPackage):
    """Checks if the documentation of a module is comprehensive"""

    homepage = "https://metacpan.org/pod/Pod::Coverage"
    url = "https://cpan.metacpan.org/authors/id/R/RC/RCLAMP/Pod-Coverage-0.23.tar.gz"

    maintainers("greenc-FNAL", "EbiArnie", "gartung", "marcmengel", "vito")

    version("0.23", sha256="30b7a0b0c942f44a7552c0d34e9b1f2e0ba0b67955c61e3b1589ec369074b107")
    version("0.22", sha256="20adf0049c07c30046b0f881ab48f0d7efcd466732b86dad6c468ef4ed27b9f2")

    provides("perl-pod-coverage-countparents")
    provides("perl-pod-coverage-exportonly")
    provides("perl-pod-coverage-extractor")
    provides("perl-pod-coverage-overloader")

    depends_on("perl-extutils-makemaker", type="build")

    depends_on("perl-pod-find@0.21:", type=("build", "run", "test"))
    depends_on("perl-devel-symdump@2.1:", type=("build", "run", "test"))
    depends_on("perl-pod-parser@1.13:", type=("build", "run", "test"))
