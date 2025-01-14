# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlBKeywords(PerlPackage):
    """Lists of reserved barewords and symbol names."""

    homepage = "https://metacpan.org/pod/B::Keywords"
    url = "https://cpan.metacpan.org/authors/id/R/RU/RURBAN/B-Keywords-1.26.tar.gz"

    maintainers("greenc-FNAL", "EbiArnie", "gartung", "marcmengel")

    version("1.26", sha256="2daa155d2f267fb0dedd87f8a4c4fb5663879fc106517b1ee258353ef87aed34")
    version("1.24", sha256="a5cf6bb285d06d17cee227783b723bb274213fd4153a5dee311d240e1169606e")
    version("1.23", sha256="13689a4c4273c0b9b4aa855764b34b7ad8bf7da1451b7468a5cef82f677b3aaa")

    depends_on("perl-extutils-makemaker", type="build")
