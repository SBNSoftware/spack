# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlTestLongstring(PerlPackage):
    """Tests strings for equality, with more helpful failures"""

    homepage = "https://metacpan.org/pod/Test::LongString"
    url = "https://cpan.metacpan.org/authors/id/R/RG/RGARCIA/Test-LongString-0.17.tar.gz"

    maintainers("greenc-FNAL", "EbiArnie", "gartung", "marcmengel", "vito")

    license("Artistic-1.0-Perl OR GPL-1.0-or-later")

    version("0.17", sha256="abc4349eaf04d1bec1e464166a3018591ea846d8f3c5c9c8af4ac4905d3e974f")
    version("0.16", sha256="2140532559280f0e0f19b4af1b9e5c1834835521fa39bc79e4e409b84daa49aa")

    depends_on("perl-extutils-makemaker", type="build")
