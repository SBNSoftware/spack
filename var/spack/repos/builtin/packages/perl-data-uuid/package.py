# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlDataUuid(PerlPackage):
    """Globally/Universally Unique Identifiers (GUIDs/UUIDs)"""

    homepage = "https://metacpan.org/pod/Data::UUID"
    url = "https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Data-UUID-1.226.tar.gz"

    maintainers("greenc-FNAL", "EbiArnie", "gartung", "marcmengel", "vitodb")

    license("BSD")

    version("1.226", sha256="093d57ffa0d411a94bafafae495697db26f5c9d0277198fe3f7cf2be22996453")
    version("1.225", sha256="d2e4cdaddc12a2ea2e512585b537290d3067e5b742f1f0ba40f66d747c26ece9")

    depends_on("perl-extutils-makemaker", type="build")
    depends_on("perl-digest-md5", type=("run", "test"))
