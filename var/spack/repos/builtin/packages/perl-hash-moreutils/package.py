# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlHashMoreutils(PerlPackage):
    """Provide the stuff missing in Hash::Util"""

    homepage = "https://metacpan.org/pod/Hash::MoreUtils"
    url = "https://cpan.metacpan.org/authors/id/R/RE/REHSACK/Hash-MoreUtils-0.06.tar.gz"

    maintainers("greenc-FNAL", "EbiArnie", "gartung", "marcmengel")

    license("Artistic-1.0-Perl OR GPL-1.0-or-later")

    version("0.06", sha256="db9a8fb867d50753c380889a5e54075651b5e08c9b3b721cb7220c0883547de8")
    version("0.05", sha256="5e9c8458457eb18315a5669e3bef68488cd5ed8c2220011ac7429ff983288ab1")

    depends_on("perl@5.8.1:", type=("build", "run", "test"))
    depends_on("perl-extutils-makemaker", type="build")
