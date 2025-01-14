# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class PerlMoo(PerlPackage):
    """Minimalist Object Orientation (with Moose compatibility)."""

    homepage = "https://cpan.metacpan.org/authors/id/H/HA/HAARG"
    url = "https://cpan.metacpan.org/authors/id/H/HA/HAARG/Moo-2.005004.tar.gz"

    license("GPL-1.0-or-later OR Artistic-1.0-Perl")

    maintainers("gartung", "greenc-FNAL", "marcmengel")

    version(
        "2.005.005",
        sha256="fb5a2952649faed07373f220b78004a9c6aba387739133740c1770e9b1f4b108",
        url="https://cpan.metacpan.org/authors/id/H/HA/HAARG/Moo-2.005005.tar.gz",
    )
    version(
        "2.005.004",
        sha256="e3030b80bd554a66f6b3c27fd53b1b5909d12af05c4c11ece9a58f8d1e478928",
        url="https://cpan.metacpan.org/authors/id/H/HA/HAARG/Moo-2.005004.tar.gz",
    )
    version(
        "2.005.003",
        sha256="bcb5ff4a4f806647ce16e1cbf85bdc0ab5d1e7ae3dc224ab6bcc774bc2e82b43",
        url="https://cpan.metacpan.org/authors/id/H/HA/HAARG/Moo-2.005003.tar.gz",
    )

    provides("perl-method-generate-accessor")
    provides("perl-method-generate-buildall")
    provides("perl-method-generate-constructor")
    provides("perl-method-generate-demolishall")
    provides("perl-moo-handlemoose")
    provides("perl-moo-handlemoose-fakeconstructor")
    provides("perl-moo-handlemoose-fakemetaclass")
    provides("perl-moo-handlemoose--typemap")
    provides("perl-moo-object")
    provides("perl-moo-role")
    provides("perl-moo--utils")
    provides("perl-moo-sification")
    provides("perl-oo")

    depends_on("perl@5.6:", type="run")
    depends_on("perl-class-method-modifiers@1.10:", type="run")
    depends_on("perl-class-xsaccessor@1.18:", type="run")
    depends_on("perl-exporter-tiny", type=("build", "run"))
    depends_on("perl-extutils-makemaker", type="build")
    depends_on("perl-role-tiny@2.2.3:", type="run")
    depends_on("perl-scalar-util@1.0:", type="run")
    depends_on("perl-sub-defer@2.6.6:", type="run")
    depends_on("perl-sub-quote@2.6.6:", type="run")
    depends_on("perl-sub-util", type="run")
    depends_on("perl-test-fatal@0.3:", type=("build", "test"))
