# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlGraph(PerlPackage):
    """Graph data structures and algorithms"""

    homepage = "https://metacpan.org/pod/Graph"
    url = "https://cpan.metacpan.org/authors/id/E/ET/ETJ/Graph-0.9726.tar.gz"

    license("GPL-1.0-or-later OR Artistic-1.0-Perl")

    version(
        "0.97.26",
        sha256="7a60c7746da3f2da43f4acea703be2ad8fa24b26a623a0745876020e6ecd970e",
        url="https://cpan.metacpan.org/authors/id/E/ET/ETJ/Graph-0.9726.tar.gz",
    )
    version(
        "0.97.04",
        sha256="325e8eb07be2d09a909e450c13d3a42dcb2a2e96cc3ac780fe4572a0d80b2a25",
        url="https://cpan.metacpan.org/authors/id/J/JH/JHI/Graph-0.9704.tar.gz",
    )
    version(
        "0.97.03",
        sha256="6e9eb559d9509d70506cd7f166866e680ec387ea63849d04749e5ddccc82098f",
        url="https://cpan.metacpan.org/authors/id/J/JH/JHI/Graph-0.9703.tar.gz",
    )

    depends_on("perl@5.6.0:")
