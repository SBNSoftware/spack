# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlRegexpUtil(PerlPackage):
    """A selection of general-utility regexp subroutines."""

    homepage = "https://metacpan.org/release/Regexp-Util"
    url = "https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/Regexp-Util-0.005.tar.gz"

    license("Artistic-1.0-Perl OR GPL-1.0-or-later", checked_by="greenc-FNAL")

    maintainers("gartung", "greenc-FNAL", "marcmengel")

    version("0.005", sha256="a08871fca2054c464ec6cd663fbdb2fce99cc0346256acf0a4936681ed8a0e00")
    version("0.004", sha256="21f34ef3d445c20695ae35302167cc1db709ac697591eb17140635400c8901ee")

    depends_on("perl@5.10:", type="run")
    depends_on("perl-exporter-tiny", type="run")
    depends_on("perl-extutils-makemaker@6.17:", type="build")
