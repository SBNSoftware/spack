# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlMooxTypesMooselike(PerlPackage):
    """Some Moosish types and a type builder"""

    homepage = "https://metacpan.org/pod/MooX::Types::MooseLike"
    url = "https://cpan.metacpan.org/authors/id/M/MA/MATEU/MooX-Types-MooseLike-0.29.tar.gz"

    maintainers("greenc-FNAL", "EbiArnie", "gartung", "marcmengel")

    version("0.29", sha256="1d3780aa9bea430afbe65aa8c76e718f1045ce788aadda4116f59d3b7a7ad2b4")
    version("0.28", sha256="635e57c26cacbf30647418eb1895c8d33927bf4f35d8ce25df2466756b174e95")

    provides("perl-moox-types-mooselike-base")

    depends_on("perl-test-fatal@0.3:", type=("build", "test"))
    depends_on("perl-strictures@2:", type=("build", "run", "test"))
    depends_on("perl-module-runtime@0.14:", type=("build", "run", "test"))
    depends_on("perl-extutils-makemaker", type="build")
    depends_on("perl-moo@1.4.2:", type=("build", "test"))
