# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlStringRewriteprefix(PerlPackage):
    """Rewrite strings based on a set of known prefixes"""

    homepage = "https://metacpan.org/pod/String::RewritePrefix"
    url = "https://cpan.metacpan.org/authors/id/R/RJ/RJBS/String-RewritePrefix-0.009.tar.gz"

    maintainers("greenc-FNAL", "EbiArnie", "gartung", "marcmengel", "vito")

    license("Artistic-1.0-Perl OR GPL-1.0-or-later")

    version("0.009", sha256="44918bec96a54af8ca37ca897e436709ec284a07b28516ef3cce4666869646d5")
    version("0.008", sha256="e45a31d6914e8f5fc722ef48d8819400dafc02105e0c61414aabbf01bce208eb")
    version("0.007", sha256="5cbbccd5636315a90ddec3610c718411b971ae4b74d5e9e2c9a0b3f976a0dda2")

    depends_on("perl@5.12.0:", type=("build", "link", "run", "test"))

    depends_on("perl-extutils-makemaker", type=("build", "test"))
    depends_on("perl-sub-exporter@0.972:", type=("build", "run", "test"))
