# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlCpanMetaCheck(PerlPackage):
    """This module verifies if requirements described in a CPAN::Meta object
    are present."""

    homepage = "https://metacpan.org/pod/CPAN::Meta::Check"
    url = "https://cpan.metacpan.org/authors/id/L/LE/LEONT/CPAN-Meta-Check-0.014.tar.gz"

    license("GPL-1.0-or-later OR Artistic-1.0-Perl")

    version("0.017", sha256="0454ab93f12780b1d579df15b5f939e09702e954be82028fadd40e8bc9b0f091")
    version("0.014", sha256="28a0572bfc1c0678d9ce7da48cf521097ada230f96eb3d063fcbae1cfe6a351f")

    depends_on("perl@5.6:", type=("build", "run", "test"))
    depends_on("perl-test-deep", type=("build", "test"))
    depends_on("perl-extutils-makemaker", type="build")
    depends_on("perl-module-metadata@1.0.23:", type="run")
