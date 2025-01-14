# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlPerlTidy(PerlPackage):
    """Indent and reformat perl scripts"""

    homepage = "https://metacpan.org/pod/Perl::Tidy"
    url = "https://cpan.metacpan.org/authors/id/S/SH/SHANCOCK/Perl-Tidy-20240202.tar.gz"

    maintainers("greenc-FNAL", "EbiArnie", "gartung", "marcmengel")

    license("GPL-2.0-only")

    version("20240202", sha256="9451adde47c2713652d39b150fb3eeb3ccc702add46913e989125184cd7ec57d")
    version("20220613", sha256="50496a6952904ef28f495919fc0a67801a63c87779c61308ce1ca5b32467c5d4")
    version("20220217", sha256="bd8bc63043c8bc94aa04811b29f93af794d8871c793c8bd36015dcbdd8a51e83")

    provides("perl-perl-tidy-debugger")
    provides("perl-perl-tidy-devnull")
    provides("perl-perl-tidy-diagnostics")
    provides("perl-perl-tidy-filewriter")
    provides("perl-perl-tidy-formatter")
    provides("perl-perl-tidy-htmlwriter")
    provides("perl-perl-tidy-ioscalar")
    provides("perl-perl-tidy-ioscalararray")
    provides("perl-perl-tidy-indentationitem")
    provides("perl-perl-tidy-linebuffer")
    provides("perl-perl-tidy-linesink")
    provides("perl-perl-tidy-linesource")
    provides("perl-perl-tidy-logger")
    provides("perl-perl-tidy-tokenizer")
    provides("perl-perl-tidy-verticalaligner")
    provides("perl-perl-tidy-verticalaligner-alignment")
    provides("perl-perl-tidy-verticalaligner-line")

    depends_on("perl@5.8:", type=("build", "run", "test"))
    depends_on("perl-extutils-makemaker", type="build")
