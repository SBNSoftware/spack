# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlCarpAssert(PerlPackage):
    """Carp::Assert - executable comments."""

    homepage = "https://metacpan.org/pod/Carp::Assert"
    url = "https://cpan.metacpan.org/authors/id/Y/YV/YVES/Carp-Assert-0.22.tar.gz"

    license("GPL-1.0-or-later OR Artistic-1.0-Perl")

    maintainers("gartung", "greenc-FNAL", "marcmengel")

    version("0.22", sha256="807ea97c6bed76ac2e4969efba7dae48fefeb9f28797f112671b3ac8a49355f7")
    version(
        "0.21",
        url="https://cpan.metacpan.org/authors/id/N/NE/NEILB/Carp-Assert-0.21.tar.gz",
        sha256="924f8e2b4e3cb3d8b26246b5f9c07cdaa4b8800cef345fa0811d72930d73a54e",
    )

    depends_on("perl@5.6:", type="run")

    depends_on("perl-extutils-makemaker", type="build")
