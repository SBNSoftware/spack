# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlIncLatest(PerlPackage):
    """Use modules bundled in inc/ if they are newer than installed ones."""  # AUTO-CPAN2Spack

    homepage = "https://github.com/dagolden/inc-latest"  # AUTO-CPAN2Spack
    url = "https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/inc-latest-0.500.tar.gz"

    license("Apache-2.0", checked_by="greenc-FNAL")

    maintainers("gartung", "greenc-FNAL", "marcmengel")  # AUTO-CPAN2Spack

    version("0.500", sha256="daa905f363c6a748deb7c408473870563fcac79b9e3e95b26e130a4a8dc3c611")

    provides("perl-inc-latest-private")  # AUTO-CPAN2Spack
    depends_on("perl@5.6:", type=("build", "run", "test"))  # AUTO-CPAN2Spack
    depends_on("perl-extutils-makemaker@6.17:", type="build")  # AUTO-CPAN2Spack
    depends_on("perl-extutils-makemaker", type=("run", "test"))  # AUTO-CPAN2Spack
