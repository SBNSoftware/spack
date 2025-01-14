# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlCriticism(PerlPackage):
    """Perl pragma to enforce coding standards and best-practices."""

    homepage = "http://perlcritic.com"
    url = "https://cpan.metacpan.org/authors/id/T/TH/THALJEF/criticism/criticism-1.02.tar.gz"

    license("Artistic-1.0-Perl OR GPL-1.0-or-later", checked_by="greenc-FNAL")

    maintainers("gartung", "greenc-FNAL", "marcmengel")

    version("1.02", sha256="962a1e8602621118d8b031283cc1220561d166894ce206d9d0ecf0049dd83975")
    version("1.01", sha256="dbd5cf0299f098a2b27ae20d0c9f5b8f8c1eac4d5cc052e9e697e10b592fd9d9")

    depends_on("perl-module-build", type="build")

    depends_on("perl-io-string", type="build")
    depends_on("perl-perl-critic@1.89:", type="run")
