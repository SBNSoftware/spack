# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlTestBase(PerlPackage):
    """A Data Driven Testing Framework"""

    homepage = "https://metacpan.org/pod/Test::Base"
    url = "https://cpan.metacpan.org/authors/id/I/IN/INGY/Test-Base-0.89.tar.gz"

    maintainers("greenc-FNAL", "EbiArnie", "gartung", "marcmengel")

    license("GPL-1.0-or-later OR Artistic-1.0-Perl")

    version("0.89", sha256="2794a1aaaeb1d3a287dd2c7286258663796562f7db9ccc6b424bc4f1de8ad014")
    version("0.88", sha256="52368cc5a9cbbc4eaba33ed820672f92001b73d8bcba0bb95d5fdb1d370b9039")

    provides("perl-test-base-block")
    provides("perl-test-base-filter")
    provides("perl-test-base-handle")

    depends_on("perl@5.8.1:", type=("build", "link", "run", "test"))

    depends_on("perl-text-diff@0.35:", type=("build", "test"))
    depends_on("perl-extutils-makemaker@6.52:", type=("build", "test"))
    depends_on("perl-test-deep", type=("build", "run", "test"))
    depends_on("perl-algorithm-diff@1.15:", type=("build", "test"))
    depends_on("perl-scalar-util@1.7:", type=("build", "run", "test"))
    depends_on("perl-filter-util-call", type=("build", "run", "test"))
    depends_on("perl-spiffy@0.40:", type=("build", "run", "test"))
