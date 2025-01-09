# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlTimeDuration(PerlPackage):
    """Rounded or exact English expression of durations"""

    homepage = "https://metacpan.org/pod/Time::Duration"
    url = "https://cpan.metacpan.org/authors/id/N/NE/NEILB/Time-Duration-1.21.tar.gz"

    maintainers("greenc-FNAL", "EbiArnie", "gartung", "marcmengel", "vito")

    license("Artistic-1.0-Perl OR GPL-1.0-or-later")

    version("1.21", sha256="fe340eba8765f9263694674e5dff14833443e19865e5ff427bbd79b7b5f8a9b8")
    version("1.20", sha256="458205b528818e741757b2854afac5f9af257f983000aae0c0b1d04b5a9cbbb8")

    depends_on("perl@5.6.0:", type=("build", "link", "run", "test"))

    depends_on("perl-extutils-makemaker", type="build")
