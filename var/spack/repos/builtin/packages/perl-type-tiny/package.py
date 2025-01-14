# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlTypeTiny(PerlPackage):
    """Tiny, yet Moo(se)-compatible type constraint"""

    homepage = "https://metacpan.org/pod/Type::Tiny"
    url = "https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/Type-Tiny-2.004000.tar.gz"

    maintainers("greenc-FNAL", "EbiArnie", "gartung", "marcmengel")

    license("GPL-1.0-or-later OR Artistic-1.0-Perl")

    version(
        "2.004.000",
        sha256="697e7f775edfc85f4cf07792d04fd19b09c25285f98f5938e8efc4f74507a128",
        url="https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/Type-Tiny-2.004.000.tar.gz",
    )
    version(
        "1.016.009",
        sha256="69794c37111ae92cd5b36626e6aa914b40b633df136dff7283dffacaf4562e38",
        url="https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/Type-Tiny-1.016009.tar.gz",
    )
    version(
        "1.016.008",
        sha256="d554f024d5da0833d623b29a1c0e1aa6147e267266725e9cf322b6d70c60dd0f",
        url="https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/Type-Tiny-1.016008.tar.gz",
    )

    provides("perl-devel-typetiny-perl56compat")
    provides("perl-devel-typetiny-perl58compat")
    provides("perl-error-typetiny")
    provides("perl-error-typetiny-assertion")
    provides("perl-error-typetiny-compilation")
    provides("perl-error-typetiny-wrongnumberofparameters")
    provides("perl-eval-typetiny")
    provides("perl-eval-typetiny-codeaccumulator")
    provides("perl-reply-plugin-typetiny")
    provides("perl-test-typetiny")
    provides("perl-type-coercion")
    provides("perl-type-coercion-frommoose")
    provides("perl-type-coercion-union")
    provides("perl-type-library")
    provides("perl-type-params")
    provides("perl-type-params-parameter")
    provides("perl-type-params-signature")
    provides("perl-type-parser")
    provides("perl-type-parser-astbuilder")
    provides("perl-type-parser-token")
    provides("perl-type-parser-tokenstream")
    provides("perl-type-registry")
    provides("perl-type-tiny-class")
    provides("perl-type-tiny-constrainedobject")
    provides("perl-type-tiny-duck")
    provides("perl-type-tiny-enum")
    provides("perl-type-tiny-intersection")
    provides("perl-type-tiny-role")
    provides("perl-type-tiny-union")
    provides("perl-type-utils")
    provides("perl-types-common-numeric")
    provides("perl-types-common-string")
    provides("perl-types-standard")
    provides("perl-types-standard-arrayref")
    provides("perl-types-standard-cycletuple")
    provides("perl-types-standard-dict")
    provides("perl-types-standard-hashref")
    provides("perl-types-standard-map")
    provides("perl-types-standard-scalarref")
    provides("perl-types-standard-strmatch")
    provides("perl-types-standard-tied")
    provides("perl-types-standard-tuple")
    provides("perl-types-typetiny")

    depends_on("perl@5.10.1:", type=("build", "run", "test"))

    depends_on("perl-extutils-makemaker@6.17:", type="build")

    depends_on("perl-ref-util-xs@0.100:", type=("build", "run", "test"))
    depends_on("perl-test-warnings", type="test")
    depends_on("perl-type-tiny-xs@0.16:", type=("build", "run", "test"))
    depends_on("perl-devel-lexalias@0.5:", type=("build", "run", "test"))
    depends_on("perl-devel-stacktrace", type=("build", "run", "test"))
    depends_on("perl-sub-util", type=("build", "run", "test"))
    depends_on("perl-exporter-tiny@1.0.0:", when="@:1", type=("build", "run", "test"))
    depends_on("perl-exporter-tiny@1.6.0:", when="@2:", type=("build", "run", "test"))
    depends_on("perl-regexp-util@0.3:", type=("build", "run", "test"))
    depends_on("perl-type-tie", type=("build", "run", "test"))
