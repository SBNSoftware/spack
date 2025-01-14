# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlFileSlurper(PerlPackage):
    """A simple, sane and efficient module to slurp a file"""

    homepage = "https://metacpan.org/pod/File::Slurper"
    url = "https://cpan.metacpan.org/authors/id/L/LE/LEONT/File-Slurper-0.011.tar.gz"

    license("GPL-1.0-or-later OR Artistic-1.0-Perl")

    version("0.014", sha256="d5a36487339888c3cd758e648160ee1d70eb4153cacbaff57846dbcefb344b0c")
    version("0.013", sha256="e2f6a4029a6a242d50054044f1fb86770b9b5cc4daeb1a967f91ffb42716a8c5")
    version("0.012", sha256="4efb2ea416b110a1bda6f8133549cc6ea3676402e3caf7529fce0313250aa578")
    version("0.011", sha256="f6494844b9759b3d1dd8fc4ffa790f8e6e493c4eb58e88831a51e085f2e76010")
    depends_on("perl@5.8:", type=("build", "run", "test"))
    depends_on("perl-perlio-utf8-strict", type="run")
    depends_on("perl-test-warnings", type=("build", "test"))
    depends_on("perl-extutils-makemaker", type="build")
