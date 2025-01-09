# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlYaml(PerlPackage):
    """This module has been released to CPAN as YAML::Old, and soon YAML.pm
    will be changed to just be a frontend interface module for all the
    various Perl YAML implementation modules, including YAML::Old"""

    homepage = "https://metacpan.org/pod/YAML"
    url = "https://cpan.metacpan.org/authors/id/T/TI/TINITA/YAML-1.27.tar.gz"

    license("GPL-1.0-or-later OR Artistic-1.0-Perl")

    version("1.30", sha256="5030a6d6cbffaf12583050bf552aa800d4646ca9678c187add649227f57479cd")
    version("1.27", sha256="c992a1e820de0721b62b22521de92cdbf49edc306ab804c485b4b1ec25f682f9")
    provides("perl-yaml-any")
    provides("perl-yaml-dumper")
    provides("perl-yaml-dumper-base")
    provides("perl-yaml-error")
    provides("perl-yaml-loader")
    provides("perl-yaml-loader-base")
    provides("perl-yaml-marshall")
    provides("perl-yaml-mo")
    provides("perl-yaml-node")
    provides("perl-yaml-tag")
    provides("perl-yaml-type-blessed")
    provides("perl-yaml-type-code")
    provides("perl-yaml-type-glob")
    provides("perl-yaml-type-ref")
    provides("perl-yaml-type-regexp")
    provides("perl-yaml-type-undef")
    provides("perl-yaml-types")
    provides("perl-yaml-warning")
    provides("perl-yaml-mapping")
    provides("perl-yaml-scalar")
    provides("perl-yaml-sequence")
    depends_on("perl@5.8.1:", type="run")
    depends_on("perl-test-deep", type=("build", "test"))
    depends_on("perl-extutils-makemaker", type="build")
    depends_on("perl-test-yaml@1.5:", type=("build", "test"))
