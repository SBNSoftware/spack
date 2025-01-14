# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlPerlCriticCompatibility(PerlPackage):
    """Policies for Perl::Critic concerned with compatibility with
    various versions of Perl."""

    homepage = "http://perlcritic.com"
    url = (
        "https://cpan.metacpan.org/authors/id/E/EL/ELLIOTJS/Perl-Critic-Compatibility-1.001.tar.gz"
    )

    license("Artistic-1.0-Perl OR GPL-1.0-or-later", checked_by="greenc-FNAL")

    maintainers("gartung", "greenc-FNAL", "marcmengel")

    version("1.001", sha256="6d45c8778fa9315f1ba21f99ea95ed1f48b66d9616b7ba7810df6af4a27f9b32")
    version("1.000", sha256="f9f25f4ec4b35dcb6d80d086b4fd0150d407a0c88893e020ab49304653afa322")

    depends_on("perl-module-build", type="build")

    provides("perl-perl-critic-policy-compatibility-prohibitthreeargumentopen")
    depends_on("perl-perl-critic@1.83_001:", type="run")
