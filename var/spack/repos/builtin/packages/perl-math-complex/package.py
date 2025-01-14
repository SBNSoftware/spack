# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlMathComplex(PerlPackage):
    """Trigonometric functions."""

    homepage = "https://cpan.metacpan.org/authors/id/Z/ZE/ZEFRAM"
    url = "https://cpan.metacpan.org/authors/id/Z/ZE/ZEFRAM/Math-Complex-1.59.tar.gz"

    license("Artistic-1.0-Perl OR GPL-1.0-or-later", checked_by="greenc-FNAL")

    maintainers("gartung", "greenc-FNAL", "marcmengel")

    version("1.59", sha256="f35eb4987512c51d2c47294a008ede210d8dd759b90b887d04847c69b42dd6d1")
    version("1.58", sha256="304511599eb997fde7e21f7ea4105f0882f7cddb94537f56d2a46d618a8bb3d8")

    provides("perl-math-trig@1.23")
    depends_on("perl-extutils-makemaker", type=("build", "run"))
    depends_on("perl-scalar-util@1.11:", type="run")
