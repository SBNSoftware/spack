# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlExtutilsMakemaker(PerlPackage):
    """ExtUtils::MakeMaker - Create a module Makefile. This utility is designed
    to write a Makefile for an extension module from a Makefile.PL. It is based
    on the Makefile.SH model provided by Andy Dougherty and the perl5-porters.
    """

    homepage = "https://github.com/Perl-Toolchain-Gang/ExtUtils-MakeMaker"
    url = "https://cpan.metacpan.org/authors/id/B/BI/BINGOS/ExtUtils-MakeMaker-7.24.tar.gz"

    license("GPL-1.0-or-later OR Artistic-1.0-Perl")

    version("7.70", sha256="f108bd46420d2f00d242825f865b0f68851084924924f92261d684c49e3e7a74")
    version("7.68", sha256="270238d253343b833daa005fb57a3a5d8916b59da197698a632b141e7acad779")
    version("7.65_02", sha256="a933a21ec1fe340dad272334e6a0623d3140cb649568ec0d2aa1f0c00a423986")
    version("7.64", sha256="4a6ac575815c0413b1f58967043cc9f2e166446b73c687f9bc62b5eaed9464a0")
    version("7.24", sha256="416abc97c3bb2cc72bef28852522f2859de53e37bf3d0ae8b292067d78755e69")

    provides("perl-dynaloader")
    provides("perl-extutils-command")
    provides("perl-extutils-command-mm")
    provides("perl-extutils-liblist")
    provides("perl-extutils-liblist-kid")
    provides("perl-extutils-mm")
    provides("perl-extutils-mm-aix")
    provides("perl-extutils-mm-any")
    provides("perl-extutils-mm-beos")
    provides("perl-extutils-mm-cygwin")
    provides("perl-extutils-mm-dos")
    provides("perl-extutils-mm-darwin")
    provides("perl-extutils-mm-macos")
    provides("perl-extutils-mm-nw5")
    provides("perl-extutils-mm-os2")
    provides("perl-extutils-mm-os390")
    provides("perl-extutils-mm-qnx")
    provides("perl-extutils-mm-uwin")
    provides("perl-extutils-mm-unix")
    provides("perl-extutils-mm-vms")
    provides("perl-extutils-mm-vos")
    provides("perl-extutils-mm-win32")
    provides("perl-extutils-mm-win95")
    provides("perl-extutils-my")
    provides("perl-extutils-makemaker-config")
    provides("perl-extutils-makemaker-locale")
    provides("perl-extutils-makemaker--version")
    provides("perl-extutils-makemaker-charstar")
    provides("perl-extutils-makemaker-version")
    provides("perl-extutils-makemaker-version-regex")
    provides("perl-extutils-makemaker-version-vpp")
    provides("perl-extutils-mkbootstrap")
    provides("perl-extutils-mksymlists")
    provides("perl-extutils-testlib")
    provides("perl-mm")
    provides("perl-my")
    provides("perl-version")
    depends_on("perl@5.6:", type="run")
    depends_on("perl-data-dumper", type="run")
