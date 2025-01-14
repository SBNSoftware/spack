# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlDistCheckconflicts(PerlPackage):
    """Declare version conflicts for your dist"""

    homepage = "https://metacpan.org/pod/Dist::CheckConflicts"
    url = "https://cpan.metacpan.org/authors/id/D/DO/DOY/Dist-CheckConflicts-0.11.tar.gz"

    license("GPL-1.0-or-later OR Artistic-1.0-Perl")

    version("0.11", sha256="ea844b9686c94d666d9d444321d764490b2cde2f985c4165b4c2c77665caedc4")
    depends_on("perl-test-fatal", type=("build", "test"))
    depends_on("perl@5.6:", type="run")
    depends_on("perl-module-runtime@0.9:", type="run")
    depends_on("perl-extutils-makemaker@6.30:", type="build")
