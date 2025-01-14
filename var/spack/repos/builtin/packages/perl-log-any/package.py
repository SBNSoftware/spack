# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlLogAny(PerlPackage):
    """Bringing loggers and listeners together"""

    homepage = "https://metacpan.org/pod/Log::Any"
    url = "https://cpan.metacpan.org/authors/id/P/PR/PREACTION/Log-Any-1.717.tar.gz"

    maintainers("greenc-FNAL", "EbiArnie", "gartung", "marcmengel")

    license("GPL-1.0-or-later OR Artistic-1.0-Perl")

    version("1.717", sha256="56649da0f3900230c9e3d29252cb0a74806fb2ddebd22805acd7368959a65bca")
    version("1.710", sha256="bdb65fd0a8888fd4522f39f0fe95e94cb9267ef1fd9f7737564d46527b306f6f")
    version("1.709", sha256="80e4b00f494f365082650222b228d2925b37ed7efaf94052087c68b2f4291e85")

    provides("perl-log-any-adapter")
    provides("perl-log-any-adapter-base")
    provides("perl-log-any-adapter-capture")
    provides("perl-log-any-adapter-file")
    provides("perl-log-any-adapter-multiplex")
    provides("perl-log-any-adapter-null")
    provides("perl-log-any-adapter-stderr")
    provides("perl-log-any-adapter-stdout")
    provides("perl-log-any-adapter-syslog")
    provides("perl-log-any-adapter-test")
    provides("perl-log-any-adapter-util")
    provides("perl-log-any-manager")
    provides("perl-log-any-proxy")
    provides("perl-log-any-proxy-null")
    provides("perl-log-any-proxy-test")
    provides("perl-log-any-test")
    depends_on("perl-extutils-makemaker", type=("build", "test"))
