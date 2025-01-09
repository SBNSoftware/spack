# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlHttpCookiejar(PerlPackage):
    """A minimalist HTTP user agent cookie jar"""

    homepage = "https://metacpan.org/pod/HTTP::CookieJar"
    url = "https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/HTTP-CookieJar-0.014.tar.gz"

    maintainers("greenc-FNAL", "EbiArnie", "gartung", "marcmengel", "vitodb")

    license("Apache-2.0")

    version("0.014", sha256="7094ea5c91f536d263b85e83ab4e9a963e11c4408ce08ecae553fa9c0cc47e73")

    provides("perl-http-cookiejar-lwp")

    depends_on("perl-extutils-makemaker@6.17:", type="build")
    depends_on("perl-extutils-makemaker", type="test")
    depends_on("perl-time-local@1.19.1:", type=("build", "run", "test"))
    depends_on("perl@5.8.1:", type=("build", "run", "test"))
    depends_on("perl-uri", type=("build", "test"))
    depends_on("perl-test-deep", type=("build", "test"))
    depends_on("perl-test-requires", type=("build", "test"))
    depends_on("perl-http-date", type="run")
    depends_on("perl-mozilla-publicsuffix", type="run")
