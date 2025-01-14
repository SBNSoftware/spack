# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlTestObject(PerlPackage):
    """Thoroughly testing objects via registered handlers"""

    homepage = "https://metacpan.org/pod/Test::Object"
    url = "https://cpan.metacpan.org/authors/id/E/ET/ETHER/Test-Object-0.08.tar.gz"

    maintainers("greenc-FNAL", "EbiArnie", "gartung", "marcmengel")

    license("Artistic-1.0-Perl OR GPL-1.0-or-later")

    version("0.08", sha256="65278964147837313f4108e55b59676e8a364d6edf01b3dc198aee894ab1d0bb")

    provides("perl-test-object-test")

    depends_on("perl@5.6.0:", type=("build", "link", "run", "test"))

    depends_on("perl-extutils-makemaker", type=("build", "test"))

    depends_on("perl-scalar-util@1.16:", type=("build", "run", "test"))
