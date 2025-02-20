# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlIpcSharelite(PerlPackage):
    """Lightweight interface to shared memory"""

    homepage = "https://metacpan.org/pod/IPC::ShareLite"
    url = "https://cpan.metacpan.org/authors/id/A/AN/ANDYA/IPC-ShareLite-0.17.tar.gz"

    maintainers("greenc-FNAL", "EbiArnie", "gartung", "marcmengel", "vitodb")

    license("Artistic-1.0-Perl OR GPL-1.0-or-later")

    version("0.17", sha256="14d406b91da96d6521d0d1a82d22a306274765226b86b0a56e7ffddcf96ae7bf")
    version("0.16", sha256="9acc120d954dfa7d02a90d319130791d93a62abbdbf1727f366d0714396f291f")

    depends_on("c", type="build")  # generated
    depends_on("perl-extutils-makemaker", type="build")
