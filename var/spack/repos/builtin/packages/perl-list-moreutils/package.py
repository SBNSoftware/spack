# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlListMoreutils(PerlPackage):
    """Provide the stuff missing in List::Util"""

    homepage = "https://metacpan.org/pod/List::MoreUtils"
    url = "http://cpan.metacpan.org/authors/id/R/RE/REHSACK/List-MoreUtils-0.428.tar.gz"

    license("Apache-2.0")

    version("0.430", sha256="63b1f7842cd42d9b538d1e34e0330de5ff1559e4c2737342506418276f646527")
    version("0.428", sha256="713e0945d5f16e62d81d5f3da2b6a7b14a4ce439f6d3a7de74df1fd166476cc2")

    depends_on("perl-exporter-tiny", type=("build", "run"))
    depends_on("perl-list-moreutils-xs", type=("build", "run"))
    provides("perl-list-moreutils-pp")
    depends_on("perl-exporter-tiny@0.38:", type="run")
    depends_on("perl-extutils-makemaker", type="build")
    depends_on("perl-test-leaktrace", type=("build", "test"))
    depends_on("perl-list-moreutils-xs@0.430:", type="run")
