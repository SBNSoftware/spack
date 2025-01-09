# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlSpiffy(PerlPackage):
    """Spiffy Perl Interface Framework For You"""

    homepage = "https://metacpan.org/pod/Spiffy"
    url = "https://cpan.metacpan.org/authors/id/I/IN/INGY/Spiffy-0.46.tar.gz"

    maintainers("greenc-FNAL", "EbiArnie", "gartung", "marcmengel", "vito")

    license("GPL-1.0-or-later OR Artistic-1.0-Perl")

    version("0.46", sha256="8f58620a8420255c49b6c43c5ff5802bd25e4f09240c51e5bf2b022833d41da3")
    version("0.45", sha256="28858d63ceed43566da4eea61175ed51de8ecbe5f72f698389d5647340ca2f14")

    provides("perl-spiffy-mixin")

    depends_on("perl@5.8.1:", type=("build", "run", "test"))

    depends_on("perl-extutils-makemaker@6.30:", type="build")
