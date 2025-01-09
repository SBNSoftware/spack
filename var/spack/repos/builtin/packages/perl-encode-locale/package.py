# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlEncodeLocale(PerlPackage):
    """Determine the locale encoding"""

    homepage = "https://metacpan.org/pod/Encode::Locale"
    url = "https://cpan.metacpan.org/authors/id/G/GA/GAAS/Encode-Locale-1.05.tar.gz"

    license("GPL-1.0-or-later OR Artistic-1.0-Perl")

    version("1.05", sha256="176fa02771f542a4efb1dbc2a4c928e8f4391bf4078473bd6040d8f11adb0ec1")
    depends_on("perl@5.8:", type="run")
    depends_on("perl-extutils-makemaker", type="build")
