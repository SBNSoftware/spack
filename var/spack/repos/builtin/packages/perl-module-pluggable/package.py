# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlModulePluggable(PerlPackage):
    """Automatically give your module the ability to have plugins"""

    homepage = "https://metacpan.org/pod/Module::Pluggable"
    url = "https://cpan.metacpan.org/authors/id/S/SI/SIMONW/Module-Pluggable-5.2.tar.gz"

    maintainers("greenc-FNAL", "EbiArnie", "gartung", "marcmengel")

    license("GPL-1.0-or-later OR Artistic-1.0-Perl")

    version("5.2", sha256="b3f2ad45e4fd10b3fb90d912d78d8b795ab295480db56dc64e86b9fa75c5a6df")
    version("5.1", sha256="e2dc354043bb16f1f3df8c4bb26070b26e594819f218cf8b8ac19e79c720916f")

    provides("perl-devel-innerpackage@0.4")
    provides("perl-module-pluggable-object")

    depends_on("perl@5.5.3:", type=("build", "run", "test"))
    depends_on("perl-extutils-makemaker", type=("build", "test"))

    depends_on("perl-module-runtime@0.12:", type=("build", "run", "test"))
    depends_on("perl-data-dumper", type=("build", "test"))
