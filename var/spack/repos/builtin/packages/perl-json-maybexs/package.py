# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlJsonMaybexs(PerlPackage):
    """Use Cpanel::JSON::XS with a fallback to JSON::XS and JSON::PP"""

    homepage = "https://metacpan.org/pod/JSON::MaybeXS"
    url = "https://cpan.metacpan.org/authors/id/E/ET/ETHER/JSON-MaybeXS-1.004005.tar.gz"

    maintainers("greenc-FNAL", "EbiArnie", "gartung", "marcmengel")

    version(
        "1.004.005",
        sha256="f5b6bc19f579e66b7299f8748b8ac3e171936dc4e7fcb72a8a257a9bd482a331",
        url="https://cpan.metacpan.org/authors/id/E/ET/ETHER/JSON-MaybeXS-1.004005.tar.gz",
    )
    version(
        "1.004.003",
        sha256="5bee3b17ff9dcffd6e99ab8cf7f35747650bfce1dc622e3ad10b85a194462fbf",
        url="https://cpan.metacpan.org/authors/id/E/ET/ETHER/JSON-MaybeXS-1.004003.tar.gz",
    )
    version(
        "1.004.002",
        sha256="3b8e2fdc3b36d0c5edbc78121840dced63798ad49cabcf875d5c5e32336d77b5",
        url="https://cpan.metacpan.org/authors/id/E/ET/ETHER/JSON-MaybeXS-1.004002.tar.gz",
    )

    depends_on("perl-cpanel-json-xs@2.33.10:", type=("build", "run", "test"))
    depends_on("perl@5.6:", type=("build", "run", "test"))
    depends_on("perl-extutils-makemaker", type="build")
    depends_on("perl-test-needs@0.2.6:", type=("build", "test"))
    depends_on("perl-scalar-util", type="run")
