# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlPpixUtilities(PerlPackage):
    """Extensions to PPI."""

    homepage = "https://cpan.metacpan.org/authors/id/E/EL/ELLIOTJS"
    url = "https://cpan.metacpan.org/authors/id/E/EL/ELLIOTJS/PPIx-Utilities-1.001000.tar.gz"

    license("Artistic-1.0-Perl OR GPL-1.0-or-later", checked_by="greenc-FNAL")

    maintainers("gartung", "greenc-FNAL", "marcmengel")

    version(
        "1.001.000",
        sha256="03a483386fd6a2c808f09778d44db06b02c3140fb24ba4bf12f851f46d3bcb9b",
        url="https://cpan.metacpan.org/authors/id/E/EL/ELLIOTJS/PPIx-Utilities-1.001000.tar.gz",
    )
    version(
        "1.000.001",
        sha256="f2785d111f79534d8fc8f73edb3a630829a7f97550c3cf58966a122e8d862a1b",
        url="https://cpan.metacpan.org/authors/id/E/EL/ELLIOTJS/PPIx-Utilities-1.000001.tar.gz",
    )
    version("1.000", sha256="cb7c80b1c7c67f32cb9a5041584c391fc3d4f229ba533a340479534b47c11435")

    depends_on("perl-module-build", type="build")

    provides("perl-ppix-utilities-exception-bug")
    provides("perl-ppix-utilities-node")
    provides("perl-ppix-utilities-statement")
    depends_on("perl-readonly", type="run")
    depends_on("perl-ppi-document-fragment@1.208:", type="run")
    depends_on("perl-readonly-xs", type="run")
    depends_on("perl-ppi@1.208:", type="run")
    depends_on("perl-task-weaken", type="run")
    depends_on("perl-exception-class", type="run")
    depends_on("perl-test-deep", type="build")
    depends_on("perl-ppi-dumper@1.208:", type="build")
    depends_on("perl-module-build@0.36:", type="build")
    depends_on("perl-scalar-util", type="run")
    depends_on("perl-ppi-document@1.208:", type="build")
    depends_on("perl-data-dumper", type="build")
