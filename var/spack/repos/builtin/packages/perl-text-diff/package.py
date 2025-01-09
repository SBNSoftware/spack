# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlTextDiff(PerlPackage):
    """Provides a basic set of services akin to the GNU diff utility."""

    homepage = "https://metacpan.org/pod/Text::Diff"
    url = "https://cpan.metacpan.org/authors/id/N/NE/NEILB/Text-Diff-1.45.tar.gz"

    license("GPL-1.0-or-later OR Artistic-1.0-Perl")

    version("1.45", sha256="e8baa07b1b3f53e00af3636898bbf73aec9a0ff38f94536ede1dbe96ef086f04")

    provides("perl-text-diff-base")
    provides("perl-text-diff-config@1.44")
    provides("perl-text-diff-table@1.44")
    depends_on("perl@5.6:", type="run")
    depends_on("perl-algorithm-diff@1.19:", type="run")
    depends_on("perl-extutils-makemaker", type="build")
