# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlBCow(PerlPackage):
    """B::COW additional B helpers to check COW status."""

    homepage = "https://metacpan.org/pod/B::COW"
    url = "https://cpan.metacpan.org/authors/id/A/AT/ATOOMIC/B-COW-0.007.tar.gz"

    license("GPL-1.0-or-later OR Artistic-1.0-Perl")

    maintainers("greenc-FNAL", "EbiArnie", "gartung", "marcmengel")

    version("0.007", sha256="1290daf227e8b09889a31cf182e29106f1cf9f1a4e9bf7752f9de92ed1158b44")
    version("0.004", sha256="fcafb775ed84a45bc2c06c5ffd71342cb3c06fb0bdcd5c1b51b0c12f8b585f51")
    version("0.003", sha256="9c7de86542871bc0ac8e6b4f7363bba4f6c5cc07e06fadc51d3a78832fcfca89")

    depends_on("perl@5.8:", type=("build", "run", "test"))
    depends_on("perl-extutils-makemaker", type=("build", "test"))
