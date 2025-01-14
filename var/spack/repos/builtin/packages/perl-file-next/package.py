# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlFileNext(PerlPackage):
    """File-finding iterator."""

    homepage = "https://cpan.metacpan.org/authors/id/P/PE/PETDANCE"
    url = "https://cpan.metacpan.org/authors/id/P/PE/PETDANCE/File-Next-1.18.tar.gz"

    license("Artistic-2.0", checked_by="greenc-FNAL")

    maintainers("gartung", "greenc-FNAL", "marcmengel")

    version("1.18", sha256="f900cb39505eb6e168a9ca51a10b73f1bbde1914b923a09ecd72d9c02e6ec2ef")
    version("1.17_01", sha256="8b4b31369f3cc38ceceb87eb91e82c2d5b7923163a9f2bd005e621940a444a11")

    depends_on("perl-extutils-makemaker", type="build")
