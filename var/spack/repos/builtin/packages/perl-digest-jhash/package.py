# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlDigestJhash(PerlPackage):
    """Perl extension for 32 bit Jenkins Hashing Algorithm"""

    homepage = "https://metacpan.org/pod/Digest::JHash"
    url = "https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/Digest-JHash-0.10.tar.gz"

    maintainers("greenc-FNAL", "EbiArnie", "gartung", "marcmengel", "vitodb")

    license("Artistic-2.0")

    version("0.10", sha256="c746cf0a861a004090263cd54d7728d0c7595a0cf90cbbfd8409b396ee3b0063")
    version("0.09", sha256="ba77919b7b7a1b6f222f1bb5a7a34d88b1a92093e40a2aec37352cb38926ada3")

    depends_on("perl@5.8:", type=("build", "run", "test"))
    depends_on("perl-dynaloader", type="run")
    depends_on("perl-extutils-makemaker", type="build")
