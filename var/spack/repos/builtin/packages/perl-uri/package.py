# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlUri(PerlPackage):
    """Uniform Resource Identifiers (absolute and relative)"""

    homepage = "https://metacpan.org/pod/URI"
    url = "https://cpan.metacpan.org/authors/id/O/OA/OALDERS/URI-5.12.tar.gz"

    skip_modules = ["URI::urn::isbn"]  # required missing Business::ISBN

    license("GPL-1.0-or-later OR Artistic-1.0-Perl")

    version("5.12", sha256="66abe0eaddd76b74801ecd28ec1411605887550fc0a45ef6aa744fdad768d9b3")
    version("5.11", sha256="d3b62a69a6ab288021167d428ac4673c399d42e4de69eb49c7953a30821843c9")
    version("5.10", sha256="16325d5e308c7b7ab623d1bf944e1354c5f2245afcfadb8eed1e2cae9a0bd0b5")
    version("5.09", sha256="03e63ada499d2645c435a57551f041f3943970492baa3b3338246dab6f1fae0a")
    version(
        "5.08",
        url="https://cpan.metacpan.org/authors/id/E/ET/ETHER/URI-5.08.tar.gz",
        sha256="7e2c6fe3b1d5947da334fa558a96e748aaa619213b85bcdce5b5347d4d26c46e",
    )
    version("1.76", sha256="b2c98e1d50d6f572483ee538a6f4ccc8d9185f91f0073fd8af7390898254413e")
    version("1.75", sha256="bdfcee61ca7f390b0fe68b98a52f7e96b827a4e918a7727f87f8b3e56f5cb440")
    version(
        "1.74",
        url="https://cpan.metacpan.org/authors/id/E/ET/ETHER/URI-1.74.tar.gz",
        sha256="a9c254f45f89cb1dd946b689dfe433095404532a4543bdaab0b71ce0fdcdd53d",
    )
    version(
        "1.73",
        url="https://cpan.metacpan.org/authors/id/E/ET/ETHER/URI-1.73.tar.gz",
        sha256="cca7ab4a6f63f3ccaacae0f2e1337e8edf84137e73f18548ec7d659f23efe413",
    )
    version(
        "1.72",
        url="https://cpan.metacpan.org/authors/id/E/ET/ETHER/URI-1.72.tar.gz",
        sha256="35f14431d4b300de4be1163b0b5332de2d7fbda4f05ff1ed198a8e9330d40a32",
    )
    version(
        "1.71",
        url="https://cpan.metacpan.org/authors/id/E/ET/ETHER/URI-1.71.tar.gz",
        sha256="9c8eca0d7f39e74bbc14706293e653b699238eeb1a7690cc9c136fb8c2644115",
    )

    provides("perl-uri-escape")
    provides("perl-uri-heuristic")
    provides("perl-uri-iri")
    provides("perl-uri-queryparam")
    provides("perl-uri-split")
    provides("perl-uri-url")
    provides("perl-uri-withbase")
    provides("perl-uri-data")
    provides("perl-uri-file")
    provides("perl-uri-file-base")
    provides("perl-uri-file-fat")
    provides("perl-uri-file-mac")
    provides("perl-uri-file-os2")
    provides("perl-uri-file-qnx")
    provides("perl-uri-file-unix")
    provides("perl-uri-file-win32")
    provides("perl-uri-ftp")
    provides("perl-uri-gopher")
    provides("perl-uri-http")
    provides("perl-uri-https")
    provides("perl-uri-ldap")
    provides("perl-uri-ldapi")
    provides("perl-uri-ldaps")
    provides("perl-uri-mailto")
    provides("perl-uri-mms")
    provides("perl-uri-news")
    provides("perl-uri-nntp")
    provides("perl-uri-nntps")
    provides("perl-uri-pop")
    provides("perl-uri-rlogin")
    provides("perl-uri-rsync")
    provides("perl-uri-rtsp")
    provides("perl-uri-rtspu")
    provides("perl-uri-sftp")
    provides("perl-uri-sip")
    provides("perl-uri-sips")
    provides("perl-uri-snews")
    provides("perl-uri-ssh")
    provides("perl-uri-telnet")
    provides("perl-uri-tn3270")
    provides("perl-uri-urn")
    provides("perl-uri-urn-isbn")
    provides("perl-uri-urn-oid")
    depends_on("perl@5.8.1:", type="run")
    depends_on("perl-extutils-makemaker", type=("build", "test"))
    depends_on("perl-test-needs", type=("build", "test"))
    depends_on("perl-scalar-util", type="run")
    depends_on("perl-data-dumper", type="run")
