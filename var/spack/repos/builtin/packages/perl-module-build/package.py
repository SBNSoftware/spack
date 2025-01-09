# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlModuleBuild(PerlPackage):
    """Module::Build is a system for building, testing, and installing Perl
    modules. It is meant to be an alternative to ExtUtils::MakeMaker.
    Developers may alter the behavior of the module through subclassing in a
    much more straightforward way than with MakeMaker. It also does not
    require a make on your system - most of the Module::Build code is
    pure-perl and written in a very cross-platform way.
    """

    homepage = "https://metacpan.org/pod/Module::Build"
    url = "https://cpan.metacpan.org/authors/id/L/LE/LEONT/Module-Build-0.4224.tar.gz"

    license("GPL-1.0-or-later OR Artistic-1.0-Perl")

    version(
        "0.42.34",
        sha256="66aeac6127418be5e471ead3744648c766bd01482825c5b66652675f2bc86a8f",
        url="https://cpan.metacpan.org/authors/id/L/LE/LEONT/Module-Build-0.4234.tar.gz",
    )
    version(
        "0.42.32",
        sha256="67c82ee245d94ba06decfa25572ab75fdcd26a9009094289d8f45bc54041771b",
        url="https://cpan.metacpan.org/authors/id/L/LE/LEONT/Module-Build-0.4232.tar.gz",
    )
    version(
        "0.42.31",
        sha256="7e0f4c692c1740c1ac84ea14d7ea3d8bc798b2fb26c09877229e04f430b2b717",
        url="https://cpan.metacpan.org/authors/id/L/LE/LEONT/Module-Build-0.4231.tar.gz",
    )
    version("0.42_30", sha256="77a185663ffcd17d7b3fc3c9b6a334f6806978b518e57b1753f35ec5e63e232c")
    version(
        "0.42.29",
        sha256="1fe491a6cda914b01bc8e592faa2b5404e9f35915ca15322f8f2a8d8f9008c18",
        url="https://cpan.metacpan.org/authors/id/L/LE/LEONT/Module-Build-0.4229.tar.gz",
    )
    version(
        "0.42.24",
        sha256="a6ca15d78244a7b50fdbf27f85c85f4035aa799ce7dd018a0d98b358ef7bc782",
        url="https://cpan.metacpan.org/authors/id/L/LE/LEONT/Module-Build-0.4224.tar.gz",
    )
    version(
        "0.42.20",
        sha256="fb1207c7e799366f7a8adda3f135bf8141c4d6068505650d4db2b2d3ce34b5a2",
        url="https://cpan.metacpan.org/authors/id/L/LE/LEONT/Module-Build-0.4220.tar.gz",
    )

    provides("perl-module-build-base")
    provides("perl-module-build-compat")
    provides("perl-module-build-config")
    provides("perl-module-build-cookbook")
    provides("perl-module-build-dumper")
    provides("perl-module-build-notes")
    provides("perl-module-build-ppmmaker")
    provides("perl-module-build-platform-default")
    provides("perl-module-build-platform-macos")
    provides("perl-module-build-platform-unix")
    provides("perl-module-build-platform-vms")
    provides("perl-module-build-platform-vos")
    provides("perl-module-build-platform-windows")
    provides("perl-module-build-platform-aix")
    provides("perl-module-build-platform-cygwin")
    provides("perl-module-build-platform-darwin")
    provides("perl-module-build-platform-os2")
    provides("perl-module-build-podparser")
    depends_on("perl-extutils-parsexs@2.21:", type="run")
    depends_on("perl-text-abbrev", type="run")
    depends_on("perl-tap-harness@3.29:", type=("build", "run", "test"))
    depends_on("perl-perl-ostype@1:", type="run")
    depends_on("perl-extutils-mkbootstrap", type="run")
    depends_on("perl@5.6.1:", type="run")
    depends_on("perl-extutils-cbuilder@0.27:", type="run")
    depends_on("perl-extutils-manifest@1.54:", type="run")
    depends_on("perl-module-metadata@1.0.2:", type="run")
    depends_on("perl-cpan-meta-yaml@0.3:", type=("build", "test"))
    depends_on("perl-data-dumper", type="run")
