# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlTestLeaktrace(PerlPackage):
    """Test::LeakTrace provides several functions that trace memory leaks. This module scans
    arenas, the memory allocation system, so it can detect any leaked SVs in given blocks."""

    homepage = "https://metacpan.org/release/Test-LeakTrace"
    url = "https://cpan.metacpan.org/authors/id/L/LE/LEEJO/Test-LeakTrace-0.17.tar.gz"

    license("GPL-1.0-or-later OR Artistic-1.0-Perl")

    maintainers("greenc-FNAL", "gartung", "marcmengel", "vitodb")

    version("0.17", sha256="777d64d2938f5ea586300eef97ef03eacb43d4c1853c9c3b1091eb3311467970")
    version("0.16", sha256="5f089eed915f1ec8c743f6d2777c3ecd0ca01df2f7b9e10038d316952583e403")

    provides("perl-test-leaktrace-script")
    depends_on("perl-extutils-makemaker", type="build")
