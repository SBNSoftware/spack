# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlRefUtil(PerlPackage):
    """Utility functions for checking references"""

    homepage = "https://metacpan.org/pod/Ref::Util"
    url = "https://cpan.metacpan.org/authors/id/A/AR/ARC/Ref-Util-0.204.tar.gz"

    maintainers("greenc-FNAL", "EbiArnie", "gartung", "marcmengel")

    license("MIT")

    version("0.204", sha256="415fa73dbacf44f3d5d79c14888cc994562720ab468e6f71f91cd1f769f105e1")
    version("0.203", sha256="6425ffd7ec0c1799086daf5b4e848211ca5d058bd75b7629dbab7b739dfb6dfb")

    provides("perl-ref-util-pp")

    depends_on("perl@5.6:", type=("build", "run", "test"))
    depends_on("perl-extutils-makemaker", type=("build", "test"))
