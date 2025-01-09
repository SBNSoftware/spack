# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlMetacpanClient(PerlPackage):
    """A comprehensive, DWIM-featured client to the MetaCPAN API"""

    homepage = "https://metacpan.org/pod/MetaCPAN::Client"
    url = "https://cpan.metacpan.org/authors/id/M/MI/MICKEY/MetaCPAN-Client-2.031000.tar.gz"

    maintainers("greenc-FNAL", "EbiArnie", "gartung", "marcmengel", "vito")

    license("Artistic-1.0-Perl OR GPL-1.0-or-later")

    version(
        "2.031.000",
        sha256="c6ceaf886a74120e2bffe2ec1f09d0fdc330acbfdb9ec876ef925ee687ec7cf5",
        url="https://cpan.metacpan.org/authors/id/M/MI/MICKEY/MetaCPAN-Client-2.031000.tar.gz",
    )
    version(
        "2.030.000",
        sha256="d9b765c5237754f17262696382a7385d90b2d01986979817862b1664b06dd3af",
        url="https://cpan.metacpan.org/authors/id/M/MI/MICKEY/MetaCPAN-Client-2.030000.tar.gz",
    )
    version(
        "2.029.000",
        sha256="c5d883903b379a5a6adb02e016ec5b52288af05652d564c895316593f3c7e57c",
        url="https://cpan.metacpan.org/authors/id/M/MI/MICKEY/MetaCPAN-Client-2.029000.tar.gz",
    )

    provides("perl-metacpan-client-author")
    provides("perl-metacpan-client-cover")
    provides("perl-metacpan-client-distribution")
    provides("perl-metacpan-client-downloadurl")
    provides("perl-metacpan-client-favorite")
    provides("perl-metacpan-client-file")
    provides("perl-metacpan-client-mirror")
    provides("perl-metacpan-client-module")
    provides("perl-metacpan-client-package")
    provides("perl-metacpan-client-permission")
    provides("perl-metacpan-client-pod")
    provides("perl-metacpan-client-rating")
    provides("perl-metacpan-client-release")
    provides("perl-metacpan-client-request")
    provides("perl-metacpan-client-resultset")
    provides("perl-metacpan-client-role-entity")
    provides("perl-metacpan-client-role-hasua")
    provides("perl-metacpan-client-scroll")
    provides("perl-metacpan-client-types")

    depends_on("perl@5.10.0:", type=("build", "link", "run", "test"))
    depends_on("perl-extutils-makemaker", type="test")
    depends_on("perl-extutils-makemaker@7.11_1:", type="build")

    depends_on("perl-http-tiny-mech@1.1.2:", type=("build", "test"))
    depends_on("perl-http-tiny@0.56:", type=("build", "run", "test"))
    depends_on("perl-io-socket-ssl@1.42:", type=("build", "run", "test"))
    depends_on("perl-json-maybexs", type=("build", "run", "test"))
    depends_on("perl-lwp-protocol-https", type=("build", "test"))
    depends_on("perl-moo", type=("build", "run", "test"))
    depends_on("perl-moo-role", type=("build", "run", "test"))
    depends_on("perl-net-ssleay@1.49:", type=("build", "run", "test"))
    depends_on("perl-ref-util", type=("build", "run", "test"))
    depends_on("perl-safe-isa", type=("build", "run", "test"))
    depends_on("perl-test-fatal", type=("build", "test"))
    depends_on("perl-test-needs@0.2.5:", type=("build", "test"))
    depends_on("perl-type-tiny", type=("build", "run", "test"))
    depends_on("perl-uri-escape", type=("build", "run", "test"))
    depends_on("perl-www-mechanize-cached@1.54:", type=("build", "test"))
