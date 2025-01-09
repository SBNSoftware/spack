# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlLinguaEnInflect(PerlPackage):
    """Convert singular to plural. Select "a" or "an"."""

    homepage = "https://metacpan.org/pod/Lingua::EN::Inflect"
    url = "https://cpan.metacpan.org/authors/id/D/DC/DCONWAY/Lingua-EN-Inflect-1.905.tar.gz"

    maintainers("greenc-FNAL", "EbiArnie", "gartung", "marcmengel", "vito")

    version("1.905", sha256="05c29ec3482e572313a60da2181b0b30c5db7cf01f8ae7616ad67e1b66263296")
    version("1.904", sha256="54d344884ba9b585680975bbd4049ddbf27bf654446fb00c7e1fc538e08c3173")

    depends_on("perl-extutils-makemaker", type="build")
