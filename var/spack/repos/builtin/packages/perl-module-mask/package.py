# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlModuleMask(PerlPackage):
    """Pretend certain modules are not installed"""

    homepage = "https://metacpan.org/pod/Module::Mask"
    url = "https://cpan.metacpan.org/authors/id/M/MA/MATTLAW/Module-Mask-0.06.tar.gz"

    maintainers("greenc-FNAL", "EbiArnie", "gartung", "marcmengel")

    license("Artistic-1.0-Perl OR GPL-1.0-or-later")

    version("0.06", sha256="2d73f81ff21c9fa28102791e546ff257164b3025f7832544c8223fb87c1e7e77")
    version("0.05", sha256="c7bfbd35d144412e5a213a2f4b6e2ad2885d93e71fdfb1f9bff467d75fb47eb7")

    depends_on("perl-module-build", type="build")

    depends_on("perl@5.8.0:", type=("build", "run", "test"))
    depends_on("perl-module-build@0.40:", type=("build", "test"))
    depends_on("perl-test-pod-coverage@1.4:", type=("build", "run", "test"))
    depends_on("perl-scalar-util@1.1:", type=("build", "run", "test"))
    depends_on("perl-test-pod@1.14:", type=("build", "run", "test"))
    depends_on("perl-module-util@1.0:", type=("build", "run", "test"))
