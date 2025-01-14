# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlBHooksEndofscope(PerlPackage):
    """Execute code after a scope finished compilation."""

    homepage = "https://metacpan.org/pod/B::Hooks::EndOfScope"
    url = "https://cpan.metacpan.org/authors/id/E/ET/ETHER/B-Hooks-EndOfScope-0.21.tar.gz"

    maintainers("EbiArnie")

    license("GPL-1.0-or-later OR Artistic-1.0-Perl")

    version("0.26", sha256="39df2f8c007a754672075f95b90797baebe97ada6d944b197a6352709cb30671")
    version("0.25", sha256="da1b6a9f7c7424776363182f9673e666b06136f13dc744241f7adce3d1ad0c1a")
    version("0.24", sha256="03aa3dfe5d0aa6471a96f43fe8318179d19794d4a640708f0288f9216ec7acc6")
    version("0.21", sha256="90f3580880f1d68b843c142cc86f58bead1f3e03634c63868ac9eba5eedae02c")

    provides("perl-b-hooks-endofscope-pp")
    provides("perl-b-hooks-endofscope-xs")

    depends_on("perl@5.6.1:", type="run")
    depends_on("perl-module-implementation@0.5:", type=("build", "run", "test"))
    depends_on("perl-sub-exporter-progressive@0.1.6:", type=("build", "run", "test"))
    depends_on("perl-extutils-makemaker", type=("build", "test"))
    depends_on("perl-scalar-util", type=("run", "test"))
