# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlMooxTypesMooselikeNumeric(PerlPackage):
    """Moo types for numbers"""

    homepage = "https://metacpan.org/pod/MooX::Types::MooseLike::Numeric"
    url = (
        "https://cpan.metacpan.org/authors/id/M/MA/MATEU/MooX-Types-MooseLike-Numeric-1.03.tar.gz"
    )

    maintainers("greenc-FNAL", "EbiArnie", "gartung", "marcmengel", "vito")

    license("Artistic-1.0-Perl OR GPL-1.0-or-later")

    version("1.03", sha256="16adeb617b963d010179922c2e4e8762df77c75232e17320b459868c4970c44b")
    version("1.02", sha256="6186f75ab2747723fd979249ec6ee0c4550f5b47aa50c0d222cc7d3590182bb6")

    depends_on("perl@5.6:", type=("build", "run", "test"))
    depends_on("perl-moox-types-mooselike@0.23:", type=("build", "run", "test"))
    depends_on("perl-test-fatal@0.3:", type=("build", "test"))
    depends_on("perl-extutils-makemaker", type="build")
    depends_on("perl-moo@1.4.2:", type=("build", "test"))
