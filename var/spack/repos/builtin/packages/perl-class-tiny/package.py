# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlClassTiny(PerlPackage):
    """Minimalist class construction"""

    homepage = "https://metacpan.org/pod/Class::Tiny"
    url = "https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/Class-Tiny-1.008.tar.gz"

    maintainers("greenc-FNAL", "EbiArnie", "gartung", "marcmengel", "vitodb")

    license("Apache-2.0")

    version("1.008", sha256="ee058a63912fa1fcb9a72498f56ca421a2056dc7f9f4b67837446d6421815615")

    provides("perl-class-tiny-object")

    depends_on("perl@5.6.0:", type=("build", "link", "run", "test"))
    depends_on("perl-test-failwarnings", type=("build", "test"))
    depends_on("perl-extutils-makemaker@6.17:", type="build")
    depends_on("perl-extutils-makemaker", type="test")
