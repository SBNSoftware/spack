# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlHashFieldhash(PerlPackage):
    """Lightweight field hash for inside-out objects."""

    homepage = "https://github.com/gfx/p5-Hash-FieldHash"
    url = "https://cpan.metacpan.org/authors/id/G/GF/GFUJI/Hash-FieldHash-0.15.tar.gz"

    license("Artistic-1.0-Perl OR GPL-1.0-or-later", checked_by="greenc-FNAL")

    maintainers("gartung", "greenc-FNAL", "marcmengel")

    version("0.15", sha256="5c515707a5433796a5697b118ddbf1f216d13c5cd52f2b64292e76f7d9b7e8f1")
    version("0.14", sha256="e1f7d0e97dd14afb2dddf64052e503c05467f73f51756ea7b647d59cab0cf721")

    depends_on("perl@5.8.5:", type="run")
    depends_on("perl-extutils-parsexs@2.21:", type="build")
    depends_on("perl-devel-ppport@3.19:", type="build")
    depends_on("perl-module-build@0.40.5:", type="build")
    depends_on("perl-test-leaktrace@0.7:", type="build")
    depends_on("perl-extutils-makemaker@6.59:", type="build")

    def setup_build_environment(self, env):
        env.prepend_path("PERL5LIB", self.stage.source_path)
