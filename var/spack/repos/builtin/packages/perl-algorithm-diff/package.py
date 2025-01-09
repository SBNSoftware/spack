# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlAlgorithmDiff(PerlPackage):
    """Compute 'intelligent' differences between two files / lists"""

    homepage = "https://metacpan.org/pod/Algorithm::Diff"
    url = "https://cpan.metacpan.org/authors/id/T/TY/TYEMQ/Algorithm-Diff-1.1903.tar.gz"

    license("GPL-1.0-or-later OR Artistic-1.0-Perl")

    version(
        "1.19.03",
        sha256="30e84ac4b31d40b66293f7b1221331c5a50561a39d580d85004d9c1fff991751",
        url="https://cpan.metacpan.org/authors/id/T/TY/TYEMQ/Algorithm-Diff-1.1903.tar.gz",
    )

    provides("perl-algorithm-diff--impl")
    depends_on("perl-extutils-makemaker", type="build")
