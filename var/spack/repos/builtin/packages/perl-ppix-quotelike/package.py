# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlPpixQuotelike(PerlPackage):
    """Parse Perl string literals and string-literal-like things."""

    homepage = "https://metacpan.org/pod/PPIx::QuoteLike"
    url = "https://cpan.metacpan.org/authors/id/W/WY/WYANT/PPIx-QuoteLike-0.023.tar.gz"

    maintainers("greenc-FNAL", "EbiArnie", "gartung", "marcmengel")

    license("Artistic-1.0-Perl OR GPL-1.0-or-later")

    version("0.023", sha256="3576a3149d2c53e07e9737b7892be5cfb84a499a6ef1df090b713b0544234d21")
    version("0.022", sha256="e043488d3b561b65188ab8e7b778f682490bf710a7bddced521e77bd111d378a")
    version("0.021_01", sha256="72df53114cb6fb0bf847c0073b35bc8a3097fcdf4cbadd451174fb960787b9af")

    depends_on("perl-module-build", type="build")

    provides("perl-ppix-quotelike-constant")
    provides("perl-ppix-quotelike-dumper")
    provides("perl-ppix-quotelike-token")
    provides("perl-ppix-quotelike-token-control")
    provides("perl-ppix-quotelike-token-delimiter")
    provides("perl-ppix-quotelike-token-interpolation")
    provides("perl-ppix-quotelike-token-string")
    provides("perl-ppix-quotelike-token-structure")
    provides("perl-ppix-quotelike-token-unknown")
    provides("perl-ppix-quotelike-token-whitespace")
    provides("perl-ppix-quotelike-utils")

    depends_on("perl@5.6:", type=("build", "run", "test"))

    depends_on("perl-readonly", type=("build", "run", "test"))
    depends_on("perl-ppi-dumper@1.238:", type=("build", "run", "test"))
    depends_on("perl-ppi-document@1.238:", type=("build", "run", "test"))
    depends_on("perl-scalar-util", type=("build", "run", "test"))
    depends_on("perl-list-util", type=("build", "run", "test"))
