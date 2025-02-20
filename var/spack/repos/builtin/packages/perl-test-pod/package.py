# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlTestPod(PerlPackage):
    """Check for POD errors in files"""

    homepage = "https://metacpan.org/pod/Test::Pod"
    url = "https://cpan.metacpan.org/authors/id/E/ET/ETHER/Test-Pod-1.52.tar.gz"

    maintainers("greenc-FNAL", "EbiArnie", "gartung", "marcmengel", "vito")

    license("GPL-1.0-or-later OR Artistic-1.0-Perl")

    version("1.52", sha256="60a8dbcc60168bf1daa5cc2350236df9343e9878f4ab9830970a5dde6fe8e5fc")
    version("1.51", sha256="c1a1d3cedf4a579e3aad89c36f9878a8542b6656dbe71f1581420f49582d7efb")

    depends_on("perl@5.8.0:", type=("build", "link", "run", "test"))

    depends_on("perl-extutils-makemaker", type="build")
