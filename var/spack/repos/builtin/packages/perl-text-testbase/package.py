# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlTextTestbase(PerlPackage):
    """Parser for Test::Base format."""

    homepage = "https://github.com/tokuhirom/Text-TestBase"
    url = "https://cpan.metacpan.org/authors/id/T/TO/TOKUHIROM/Text-TestBase-0.13.tar.gz"

    license("Artistic-1.0-Perl OR GPL-1.0-or-later", checked_by="greenc-FNAL")

    maintainers("gartung", "greenc-FNAL", "marcmengel")

    version("0.13", sha256="25a512d6f64099607bef799a58516524fdbe6e9a458959a4747c4d7443c4d2fa")
    version("0.12", sha256="5348ffed8238a19f731e91b0c553c474b62e1d81ed887471be99e0b0b1bc801e")

    depends_on("perl-module-build", type="build")

    provides("perl-data-section-testbase")
    provides("perl-test-base-less")
    provides("perl-test-base-less-filter")
    provides("perl-text-testbase-block")
    depends_on("perl@5.8.1:", type="run")
    depends_on("perl-test-requires", type=("build", "test"))
    depends_on("perl-module-build@0.38:", type="build")
    depends_on("perl-digest-md5", type=("build", "test"))
    depends_on("perl-class-accessor-lite@0.5:", type="run")
