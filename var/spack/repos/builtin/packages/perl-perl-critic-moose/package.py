# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlPerlCriticMoose(PerlPackage):
    """Policies for Perl::Critic concerned with using Moose"""

    homepage = "https://metacpan.org/pod/Perl::Critic::Moose"
    url = "https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/Perl-Critic-Moose-1.05.tar.gz"

    maintainers("greenc-FNAL", "EbiArnie", "gartung", "marcmengel")

    license("Artistic-1.0-Perl OR GPL-1.0-or-later")

    version("1.05", sha256="52eb8e22c42643f17fe297a21714017efdb9e2986c24e3337e030f3650f92201")
    version("1.04", sha256="7a441cd9e08090c3e676c904e452efeff6f42f171cd38c5e2e609f8c45692a3d")

    provides("perl-perl-critic-policy-moose-prohibitdestroymethod")
    provides("perl-perl-critic-policy-moose-prohibitlazybuild")
    provides("perl-perl-critic-policy-moose-prohibitmultiplewiths")
    provides("perl-perl-critic-policy-moose-prohibitnewmethod")
    provides("perl-perl-critic-policy-moose-requirecleannamespace")
    provides("perl-perl-critic-policy-moose-requiremakeimmutable")

    depends_on("perl-readonly", type=("build", "run", "test"))
    depends_on("perl-namespace-autoclean", type=("build", "run", "test"))
    depends_on("perl-extutils-makemaker", type=("build", "test"))
    depends_on("perl@5.8:", type=("build", "run", "test"))
    depends_on("perl-perl-critic-policy", type=("build", "run", "test"))
    depends_on("perl-perl-critic-utils", type=("build", "run", "test"))
    depends_on("perl-test-perl-critic-policy", type=("build", "test"))
    depends_on("perl-perl-critic-utils-ppi", type=("build", "run", "test"))
