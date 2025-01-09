# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlCacheCache(PerlPackage):
    """Extends Cache::SizeAwareMemoryCache"""

    homepage = "https://metacpan.org/pod/Cache::Cache"
    url = "https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Cache-Cache-1.08.tar.gz"

    license("Artistic-1.0-Perl OR GPL-1.0-or-later")

    maintainers("greenc-FNAL", "EbiArnie", "gartung", "marcmengel", "vitodb")

    version("1.08", sha256="d2c7fd5dba5dd010b7d8923516890bb6ccf6b5f188ccb69f35cb0fd6c031d1e8")
    version("1.07", sha256="c1afe8fff07f05385468f78f3fdbf1dbb5fd2bb70b50c25163d5be540bdc8d12")

    provides("perl-cache-basecache")
    provides("perl-cache-basecachetester")
    provides("perl-cache-cachemetadata")
    provides("perl-cache-cachesizer")
    provides("perl-cache-cachetester")
    provides("perl-cache-cacheutils")
    provides("perl-cache-filebackend")
    provides("perl-cache-filecache")
    provides("perl-cache-memorybackend")
    provides("perl-cache-memorycache")
    provides("perl-cache-nullcache")
    provides("perl-cache-object")
    provides("perl-cache-sharedmemorybackend")
    provides("perl-cache-sharedmemorycache")
    provides("perl-cache-sizeawarecache")
    provides("perl-cache-sizeawarecachetester")
    provides("perl-cache-sizeawarefilecache")
    provides("perl-cache-sizeawarememorycache")
    provides("perl-cache-sizeawaresharedmemorycache")

    depends_on("perl-extutils-makemaker", type="build")

    depends_on("perl-error@0.15:", type=("build", "run", "test"))
    depends_on("perl-ipc-sharelite@0.9:", type=("build", "run", "test"))
    depends_on("perl-digest-sha1@2.2:", type=("build", "run", "test"))
