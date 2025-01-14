# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlDevelPpport(PerlPackage):
    """Perl/Pollution/Portability."""

    homepage = "https://cpan.metacpan.org/authors/id/A/AT/ATOOMIC"
    url = "https://cpan.metacpan.org/authors/id/A/AT/ATOOMIC/Devel-PPPort-3.68.tar.gz"

    license("Artistic-1.0-Perl OR GPL-1.0-or-later", checked_by="greenc-FNAL")

    maintainers("gartung", "greenc-FNAL", "marcmengel")

    version("3.68", sha256="5290d5bb84cde9e9e61113a20c67b5d47267eb8e65a119a8a248cc96aac0badb")
    version("3.67", sha256="77954772eab2a0de4a49a77b334f73ef0b8f5251bdc0ddd70d2a4d8110f66227")

    depends_on("perl-extutils-makemaker", type="build")
