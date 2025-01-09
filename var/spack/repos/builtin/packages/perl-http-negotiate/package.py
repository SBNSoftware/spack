# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlHttpNegotiate(PerlPackage):
    """Choose a variant to serve"""

    homepage = "https://metacpan.org/pod/HTTP::Negotiate"
    url = "https://cpan.metacpan.org/authors/id/G/GA/GAAS/HTTP-Negotiate-6.01.tar.gz"

    version("6.01", sha256="1c729c1ea63100e878405cda7d66f9adfd3ed4f1d6cacaca0ee9152df728e016")

    depends_on("perl@5.8.1:", type="run")
    depends_on("perl-extutils-makemaker", type="build")
    depends_on("perl-http-headers@6:", type="run")
