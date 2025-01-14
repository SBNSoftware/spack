# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlPodSpell(PerlPackage):
    """A formatter for spellchecking Pod"""

    homepage = "https://metacpan.org/pod/Pod::Spell"
    url = "https://cpan.metacpan.org/authors/id/H/HA/HAARG/Pod-Spell-1.26.tar.gz"

    maintainers("greenc-FNAL", "EbiArnie", "gartung", "marcmengel")

    license("Artistic-2.0")

    version("1.26", sha256="2f05bfc9cfb04b96fcbfa2c8544d1e6ae908596d3696c46e0e26556b750afbbf")
    version("1.20", sha256="6383f7bfe22bc0d839a08057a0ce780698b046184aea935be4833d94986dd03c")
    version("1.19_91", sha256="b1e2f8303d2b01184ce189f45eedb0001bad4fd4707d42b6af507184ab6ddf42")

    provides("perl-pod-wordlist")

    depends_on("perl@5.8:", type=("build", "run", "test"))

    depends_on("perl-file-sharedir", type=("build", "run", "test"))
    depends_on("perl-file-sharedir-install@0.06:", type=("build"))
    depends_on("perl-path-tiny", type=("build", "run", "test"))
    depends_on("perl-extutils-makemaker", type=("build", "test"))
    depends_on("perl-text-wrap", type=("build", "run", "test"))
    depends_on("perl-class-tiny", type=("build", "run", "test"))
    depends_on("perl-lingua-en-inflect", type=("build", "run", "test"))
    depends_on("perl-test-deep", type=("build", "test"))
    depends_on("perl-pod-parser", type=("build", "run", "test"))
