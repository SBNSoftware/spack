# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlArchiveZip(PerlPackage):
    """Archive::Zip - Provide an interface to ZIP archive files."""

    homepage = "https://metacpan.org/pod/Archive::Zip"
    url = "https://cpan.metacpan.org/authors/id/P/PH/PHRED/Archive-Zip-1.68.tar.gz"

    license("GPL-1.0-or-later OR Artistic-1.0-Perl")

    maintainers("gartung", "greenc-FNAL", "marcmengel")

    version("1.68", sha256="984e185d785baf6129c6e75f8eb44411745ac00bf6122fb1c8e822a3861ec650")
    version("1.67", sha256="be2274344c7659bf9189838dc6b9a59ec6f957c74ddfd35ff2780d56f4592774")

    depends_on("perl@5.6:", type="run")
    depends_on("perl-extutils-makemaker", type="build")
    depends_on("perl-time-local", type="run")
    depends_on("perl-compress-raw-zlib@2.17:", type="run")
