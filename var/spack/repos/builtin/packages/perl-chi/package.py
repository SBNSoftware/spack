# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlChi(PerlPackage):
    """Unified cache handling interface."""

    homepage = "https://metacpan.org/pod/CHI"
    url = "https://cpan.metacpan.org/authors/id/A/AS/ASB/CHI-0.61.tar.gz"

    maintainers("greenc-FNAL", "EbiArnie", "gartung", "marcmengel", "vitodb")

    license("Artistic-1.0-Perl OR GPL-1.0-or-later")

    version("0.61", sha256="583545c9e5312bb4193ab16de9f55ff8f4b4a7ded128cee8dd2cb021d4678b5b")

    provides("perl-chi-cacheobject")
    provides("perl-chi-driver")
    provides("perl-chi-driver-base-cachecontainer")
    provides("perl-chi-driver-cachecache")
    provides("perl-chi-driver-fastmmap")
    provides("perl-chi-driver-file")
    provides("perl-chi-driver-memory")
    provides("perl-chi-driver-metacache")
    provides("perl-chi-driver-null")
    provides("perl-chi-driver-rawmemory")
    provides("perl-chi-driver-role-hassubcaches")
    provides("perl-chi-driver-role-issizeaware")
    provides("perl-chi-driver-role-issubcache")
    provides("perl-chi-stats")

    depends_on("perl-cache-cache", type=("build", "run", "test"))
    depends_on("perl-carp-assert@0.20:", type=("build", "run", "test"))
    depends_on("perl-class-load", type=("build", "run", "test"))
    depends_on("perl-data-uuid", type=("build", "run", "test"))
    depends_on("perl-digest-jhash", type=("build", "run", "test"))
    depends_on("perl-hash-moreutils", type=("build", "run", "test"))
    depends_on("perl-json-maybexs@1.003.003:", type=("build", "run", "test"))
    depends_on("perl-list-moreutils@0.13:", type=("build", "run", "test"))
    depends_on("perl-log-any@0.08:", type=("build", "run", "test"))
    depends_on("perl-module-mask", type=("build", "run", "test"))
    depends_on("perl-moo@1.003:", type=("build", "run", "test"))
    depends_on("perl-moox-types-mooselike-base", type=("build", "run", "test"))
    depends_on("perl-moox-types-mooselike-numeric", type=("build", "run", "test"))
    depends_on("perl-moox-types-mooselike@0.23:", type=("build", "run", "test"))
    depends_on("perl-string-rewriteprefix", type=("build", "run", "test"))
    depends_on("perl-task-weaken", type=("build", "run", "test"))
    depends_on("perl-test-class", type=("build", "run", "test"))
    depends_on("perl-test-deep", type=("build", "run", "test"))
    depends_on("perl-test-exception", type=("build", "run", "test"))
    depends_on("perl-test-warn", type=("build", "run", "test"))
    depends_on("perl-time-duration-parse@0.03:", type=("build", "run", "test"))
    depends_on("perl-time-duration@1.06:", type=("build", "run", "test"))
    depends_on("perl-time-hires", type=("build", "run", "test"))
    depends_on("perl-timedate", type=("build", "run", "test"))
    depends_on("perl-try-tiny@0.05:", type=("build", "run", "test"))
