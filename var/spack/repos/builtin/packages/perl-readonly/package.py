# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlReadonly(PerlPackage):
    """Readonly - Facility for creating read-only scalars, arrays, hashes"""

    homepage = "https://metacpan.org/pod/Readonly"
    url = "https://cpan.metacpan.org/authors/id/S/SA/SANKO/Readonly-2.05.tar.gz"

    version("2.05", sha256="4b23542491af010d44a5c7c861244738acc74ababae6b8838d354dfb19462b5e")

    provides("perl-readonly-array")
    provides("perl-readonly-hash")
    provides("perl-readonly-scalar")
    depends_on("perl@5.5:", type="run")
    depends_on("perl-module-build-tiny@0.35:", type="build")
