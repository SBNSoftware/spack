# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlNetSsleay(PerlPackage):
    """Perl extension for using OpenSSL"""

    homepage = "https://metacpan.org/pod/Net::SSLeay"
    url = "https://cpan.metacpan.org/authors/id/C/CH/CHRISN/Net-SSLeay-1.94.tar.gz"

    license("Artistic-2.0")

    version("1.94", sha256="9d7be8a56d1bedda05c425306cc504ba134307e0c09bda4a788c98744ebcd95d")
    version("1.93_01", sha256="876d022fbc719631b11d6bb4b6e78db3c19bbca578093c376c8f9900a4432aa3")
    version("1.92", sha256="47c2f2b300f2e7162d71d699f633dd6a35b0625a00cbda8c50ac01144a9396a9")
    version("1.90", sha256="f8696cfaca98234679efeedc288a9398fcf77176f1f515dbc589ada7c650dc93")
    version("1.85", sha256="9d8188b9fb1cae3bd791979c20554925d5e94a138d00414f1a6814549927b0c8")
    version("1.84", sha256="823ec3cbb428309d6a9e56f362a9300693ce3215b7fede109adb7be361fff177")
    version("1.83", sha256="c45857c829a48ebf9ecc46e904d20827ad38dde0eb8d5e8b47895260ae6827b7")
    version("1.82", sha256="5895c519c9986a5e5af88e3b8884bbdc70e709ee829dc6abb9f53155c347c7e5")

    depends_on("c", type="build")  # generated

    depends_on("openssl")

    provides("perl-net-ssleay-handle")
    depends_on("perl@5.8.1:", type="run")
    depends_on("perl-extutils-makemaker", type="build")
    depends_on("perl-scalar-util", type=("build", "test"))

    def configure(self, spec, prefix):
        self.build_method = "Makefile.PL"
        self.build_executable = make
        # Do you want to run external tests?
        config_answers = ["\n"]
        config_answers_filename = "spack-config.in"

        with open(config_answers_filename, "w") as f:
            f.writelines(config_answers)

        with open(config_answers_filename, "r") as f:
            env["OPENSSL_PREFIX"] = self.spec["openssl"].prefix
            perl("Makefile.PL", "INSTALL_BASE={0}".format(prefix), input=f)

    def url_for_version(self, version):
        if self.spec.satisfies("@1.86:"):
            return f"https://cpan.metacpan.org/authors/id/C/CH/CHRISN/Net-SSLeay-{version}.tar.gz"
        else:
            return f"http://search.cpan.org/CPAN/authors/id/M/MI/MIKEM/Net-SSLeay-{version}.tar.gz"
