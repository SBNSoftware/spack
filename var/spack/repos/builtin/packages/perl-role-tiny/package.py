# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class PerlRoleTiny(PerlPackage):
    """Roles: a nouvelle cuisine portion size slice of Moose."""

    homepage = "https://cpan.metacpan.org/authors/id/H/HA/HAARG"
    url = "https://cpan.metacpan.org/authors/id/H/HA/HAARG/Role-Tiny-2.002004.tar.gz"

    maintainers("gartung", "greenc-FNAL", "marcmengel")

    license("GPL-1.0-or-later OR Artistic-1.0-Perl")

    version(
        "2.002.004",
        sha256="d7bdee9e138a4f83aa52d0a981625644bda87ff16642dfa845dcb44d9a242b45",
        url="https://cpan.metacpan.org/authors/id/H/HA/HAARG/Role-Tiny-2.002004.tar.gz",
    )
    version(
        "2.002.003",
        sha256="6981e5f2d0beded157840199d678da462b22a9a3753333cab322ab6efb0fbb89",
        url="https://cpan.metacpan.org/authors/id/H/HA/HAARG/Role-Tiny-2.002003.tar.gz",
    )

    provides("perl-role-tiny-with")

    depends_on("perl-exporter-tiny", type=("build", "run"))
    depends_on("perl@5.6:", type="run")
    depends_on("perl-class-method-modifiers@1.5:", type="run")
