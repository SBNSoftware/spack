# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlModuleUtil(PerlPackage):
    """Module name tools and transformations"""

    homepage = "https://metacpan.org/pod/Module::Util"
    url = "https://cpan.metacpan.org/authors/id/M/MA/MATTLAW/Module-Util-1.09.tar.gz"

    maintainers("greenc-FNAL", "EbiArnie", "gartung", "marcmengel", "vito")

    license("Artistic-1.0-Perl OR GPL-1.0-or-later")

    version("1.09", sha256="6cfbcb6a45064446ec8aa0ee1a7dddc420b54469303344187aef84d2c7f3e2c6")
    version("1.08", sha256="d9eba5621fe3890de299be9d65265357979fe612429d0ce1d319122d442bc7ba")

    depends_on("perl@5.5.3:", type=("build", "run", "test"))

    depends_on("perl-module-build@0.40:", type=("build", "test"))
