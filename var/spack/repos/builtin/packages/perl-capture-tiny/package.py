# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlCaptureTiny(PerlPackage):
    """Capture STDOUT and STDERR from Perl, XS or external programs"""

    homepage = "https://metacpan.org/pod/Capture::Tiny"
    url = "https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/Capture-Tiny-0.46.tar.gz"

    license("Apache-2.0")

    version("0.48", sha256="6c23113e87bad393308c90a207013e505f659274736638d8c79bac9c67cc3e19")
    version("0.46", sha256="5d7a6a830cf7f2b2960bf8b8afaac16a537ede64f3023827acea5bd24ca77015")
    depends_on("perl@5.6:", type="run")
    depends_on("perl-extutils-makemaker@6.17:", type="build")
    depends_on("perl-extutils-makemaker", type="test")
    depends_on("perl-scalar-util", type="run")
