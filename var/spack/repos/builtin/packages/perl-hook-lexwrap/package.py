# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlHookLexwrap(PerlPackage):
    """Lexically scoped subroutine wrappers"""

    homepage = "https://metacpan.org/pod/Hook::LexWrap"
    url = "https://cpan.metacpan.org/authors/id/E/ET/ETHER/Hook-LexWrap-0.26.tar.gz"

    maintainers("greenc-FNAL", "EbiArnie", "gartung", "marcmengel")

    license("Artistic-1.0-Perl OR GPL-1.0-or-later")

    version("0.26", sha256="b60bdc5f98f94f9294b06adef82b1d996da192d5f183f9f434b610fd1137ec2d")
    version("0.25", sha256="08ab9af6bd9b4560702d9d994ad9d905af0c2fd24090d1480ff640f137c1430d")

    depends_on("perl@5.6:", type=("build", "run", "test"))
    depends_on("perl-extutils-makemaker", type=("build", "test"))
