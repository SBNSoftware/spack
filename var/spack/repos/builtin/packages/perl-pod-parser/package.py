# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlPodParser(PerlPackage):
    """Modules for parsing/translating POD format documents"""

    homepage = "https://metacpan.org/pod/Pod::Parser"
    url = "https://cpan.metacpan.org/authors/id/M/MA/MAREKR/Pod-Parser-1.67.tar.gz"

    maintainers("greenc-FNAL", "EbiArnie", "gartung", "marcmengel")

    version("1.67", sha256="5deccbf55d750ce65588cd211c1a03fa1ef3aaa15d1ac2b8d85383a42c1427ea")
    version("1.65", sha256="3ba7bdec659416a51fe2a7e59f0883e9c6a3b21bc9d001042c1d6a32d401b28a")
    version("1.64", sha256="02f6649faa46ef8967743b0f5e50b8330bb3f0244da7a0bb40c96a1a44d6661d")

    provides("perl-pod-cache")
    provides("perl-pod-cache-item")
    provides("perl-pod-find")
    provides("perl-pod-hyperlink")
    provides("perl-pod-inputobjects")
    provides("perl-pod-inputsource")
    provides("perl-pod-interiorsequence")
    provides("perl-pod-list")
    provides("perl-pod-paragraph")
    provides("perl-pod-parsetree")
    provides("perl-pod-parseutils")
    provides("perl-pod-plaintext@2.07")
    provides("perl-pod-select")
    depends_on("perl-extutils-makemaker", type="build")
