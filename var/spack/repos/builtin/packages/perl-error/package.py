# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlError(PerlPackage):
    """The Error package provides two interfaces. Firstly Error provides a
    procedural interface to exception handling. Secondly Error is a base class
    for errors/exceptions that can either be thrown, for subsequent catch, or
    can simply be recorded."""

    homepage = "https://metacpan.org/pod/Error"
    url = "https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/Error-0.17029.tar.gz"

    license("GPL-1.0-or-later OR Artistic-1.0-Perl")

    version(
        "0.17.029",
        sha256="1a23f7913032aed6d4b68321373a3899ca66590f4727391a091ec19c95bf7adc",
        url="https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/Error-0.17029.tar.gz",
    )
    version(
        "0.17.028",
        sha256="3ad85c5e58b31c8903006298424a51bba39f1840e324f5ae612eabc8b935e960",
        url="https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/Error-0.17028.tar.gz",
    )

    provides("perl-error-simple")
    provides("perl-error-warndie")
    provides("perl-error-subs")

    depends_on("perl@5.6:", type=("build", "run", "test"))
    depends_on("perl-module-build@0.28:", type="build")
    depends_on("perl-extutils-makemaker", type="build")
    depends_on("perl-scalar-util", type="run")
