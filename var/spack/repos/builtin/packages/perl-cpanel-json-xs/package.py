# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlCpanelJsonXs(PerlPackage):
    """CPanel fork of JSON::XS, fast and correct serializing"""

    homepage = "https://metacpan.org/pod/Cpanel::JSON::XS"
    url = "https://cpan.metacpan.org/authors/id/R/RU/RURBAN/Cpanel-JSON-XS-4.37.tar.gz"

    maintainers("greenc-FNAL", "EbiArnie", "gartung", "marcmengel", "vitodb")

    license("GPL-1.0-or-later OR Artistic-1.0-Perl")

    version("4.37", sha256="c241615a0e17ff745aaa86bbf466a6e29cd240515e65f06a7a05017b619e6d4b")
    version("4.32", sha256="ece9d35914175e6c47b62fd936244278365ebce0905fe92b037e484e6d501895")
    version("4.31", sha256="02a67acee3de24a728c396486800e2a235591a543d0794449ad388fe3d5cff29")

    provides("perl-cpanel-json-xs-type")
    depends_on("perl-math-bigint", type="run")
    depends_on("perl-math-bigfloat@1.16:", type="run")
    depends_on("perl-time-piece", type=("build", "test"))
    depends_on("perl-extutils-makemaker", type="build")
    depends_on("perl-data-dumper", type=("build", "test"))
