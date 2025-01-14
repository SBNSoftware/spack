# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlIoSocketIp(PerlPackage):
    """Family-neutral IP socket supporting both IPv4 and IPv6."""

    homepage = "https://cpan.metacpan.org/authors/id/P/PE/PEVANS"
    url = "https://cpan.metacpan.org/authors/id/P/PE/PEVANS/IO-Socket-IP-0.41.tar.gz"

    license("Artistic-1.0-Perl OR GPL-1.0-or-later", checked_by="greenc-FNAL")

    maintainers("gartung", "greenc-FNAL", "marcmengel")

    version("0.41", sha256="849a45a238f8392588b97722c850382c4e6d157cd08a822ddcb9073c73bf1446")
    version("0.40", sha256="db50cc58f02c63edec35ecfd27818312fdb6e3de6ba7de338197500e26b9fa30")

    depends_on("perl-module-build", type="build")

    depends_on("perl-module-build@0.40.4:", type="build")
