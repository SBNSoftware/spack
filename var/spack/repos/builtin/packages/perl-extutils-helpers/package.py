# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlExtutilsHelpers(PerlPackage):
    """ExtUtils::Helpers - Various portability utilities for module builders"""

    homepage = "https://metacpan.org/pod/ExtUtils::Helpers"
    url = "https://cpan.metacpan.org/authors/id/L/LE/LEONT/ExtUtils-Helpers-0.026.tar.gz"

    license("GPL-1.0-or-later OR Artistic-1.0-Perl")

    version("0.026", sha256="de901b6790a4557cf4ec908149e035783b125bf115eb9640feb1bc1c24c33416")
    provides("perl-extutils-helpers-unix")
    provides("perl-extutils-helpers-vms")
    provides("perl-extutils-helpers-windows")
    depends_on("perl@5.6:", type=("build", "run", "test"))
    depends_on("perl-extutils-makemaker", type="build")
