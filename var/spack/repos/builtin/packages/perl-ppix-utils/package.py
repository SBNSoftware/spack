# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlPpixUtils(PerlPackage):
    """Utility functions for PPI"""

    homepage = "https://metacpan.org/pod/PPIx::Utils"
    url = "https://cpan.metacpan.org/authors/id/D/DB/DBOOK/PPIx-Utils-0.003.tar.gz"

    maintainers("greenc-FNAL", "EbiArnie", "gartung", "marcmengel")

    license("Artistic-1.0-Perl OR GPL-1.0-or-later")

    version("0.003", sha256="2a9bccfc8ead03be01b67248fe8e152522040f798286fa4ef4432b7f2efdba11")
    version("0.002", sha256="df9957cc4a15fa516579e1552b8508ced045c482b77d7fc8257b2115fa8b7c27")

    provides("perl-ppix-utils-classification")
    provides("perl-ppix-utils-language")
    provides("perl-ppix-utils-traversal")

    depends_on("perl@5.6:", type=("build", "run", "test"))
    depends_on("perl-b-keywords@1.9:", type=("build", "run", "test"))
    depends_on("perl-ppi-dumper", type=("build", "test"))
    depends_on("perl-ppi@1.250:", type=("build", "run", "test"))
    depends_on("perl-extutils-makemaker", type=("build", "test"))
    depends_on("perl-scalar-util", type=("build", "run", "test"))
    depends_on("perl-data-dumper", type=("build", "test"))
