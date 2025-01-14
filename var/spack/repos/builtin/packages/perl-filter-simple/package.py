# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlFilterSimple(PerlPackage):
    """Simplified source filtering."""

    homepage = "https://cpan.metacpan.org/authors/id/S/SM/SMUELLER"
    url = "https://cpan.metacpan.org/authors/id/S/SM/SMUELLER/Filter-Simple-0.94.tar.gz"

    license("Artistic-1.0-Perl OR GPL-1.0-or-later", checked_by="greenc-FNAL")

    maintainers("gartung", "greenc-FNAL", "marcmengel")

    version("0.94", sha256="cffc0b960d783dfbcf7b247f5fea65c84de230ee2f091f142ca9b8aeb07e79d2")
    version("0.91", sha256="c75a4945e94ecfe97e1409f49df036700d2e072e288497e205c4d319a80f694d")

    provides("perl-demo1@0.01")
    provides("perl-demo2a@0.01")
    provides("perl-demo2b@0.01")
    provides("perl-demodata@0.01")
    provides("perl-demorevcat@0.01")
    provides("perl-demoswear@0.01")
    provides("perl-demounpod@0.01")
    provides("perl-demo-data@0.01")
    provides("perl-demo-exporter@0.01")
    provides("perl-demo-importer@0.01")
    provides("perl-demo-rem@0.01")
    provides("perl-dotsforarrows")
    depends_on("perl-extutils-makemaker", type="build")
    depends_on("perl-text-balanced@1.97:", type="run")
