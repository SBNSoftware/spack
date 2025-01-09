# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlWant(PerlPackage):
    """A generalisation of wantarray."""

    homepage = "https://metacpan.org/pod/Want"
    url = "https://cpan.metacpan.org/authors/id/R/RO/ROBIN/Want-0.29.tar.gz"

    license("GPL-1.0-or-later OR Artistic-1.0-Perl")

    version("0.29", sha256="b4e4740b8d4cb783591273c636bd68304892e28d89e88abf9273b1de17f552f7")
