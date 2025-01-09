# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlDataDump(PerlPackage):
    """Pretty printing of data structures"""

    homepage = "https://metacpan.org/pod/Data::Dump"
    url = "https://cpan.metacpan.org/authors/id/G/GA/GARU/Data-Dump-1.25.tar.gz"

    maintainers("greenc-FNAL", "EbiArnie", "gartung", "marcmengel", "vitodb")

    license("Artistic-1.0-Perl OR GPL-1.0-or-later")

    version("1.25", sha256="a4aa6e0ddbf39d5ad49bddfe0f89d9da864e3bc00f627125d1bc580472f53fbd")
    version("1.24", sha256="cc0275545125ee6ab985fe1e844c3723b0b137b8bb727e8834362ef5cd6d9d1a")

    provides("perl-data-dump-filtercontext")
    provides("perl-data-dump-filtered")
    provides("perl-data-dump-trace@0.02")
    provides("perl-data-dump-trace-call")
    provides("perl-data-dump-trace-wrapper")

    depends_on("perl@5.6:", type=("build", "run", "test"))
    depends_on("perl-extutils-makemaker", type="build")
