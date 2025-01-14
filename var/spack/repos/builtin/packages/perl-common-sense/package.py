# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlCommonSense(PerlPackage):
    """Save a tree AND a kitten, use common::sense!"""

    homepage = "https://metacpan.org/pod/common::sense"
    url = "https://cpan.metacpan.org/authors/id/M/ML/MLEHMANN/common-sense-3.75.tar.gz"

    maintainers("greenc-FNAL", "EbiArnie", "gartung", "marcmengel")

    license("GPL-1.0-or-later OR Artistic-1.0-Perl")

    version("3.75", sha256="a86a1c4ca4f3006d7479064425a09fa5b6689e57261fcb994fe67d061cba0e7e")
    version("3.74", sha256="771f7d02abd1ded94d9e37d3f66e795c8d2026d04defbeb5b679ca058116bbf3")

    depends_on("perl-extutils-makemaker", type="build")
