# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlTypesSerialiser(PerlPackage):
    """Simple data types for common serialisation formats"""

    homepage = "https://metacpan.org/pod/Types::Serialiser"
    url = "https://cpan.metacpan.org/authors/id/M/ML/MLEHMANN/Types-Serialiser-1.01.tar.gz"

    maintainers("greenc-FNAL", "EbiArnie", "gartung", "marcmengel")

    version("1.01", sha256="f8c7173b0914d0e3d957282077b366f0c8c70256715eaef3298ff32b92388a80")
    version("1.0", sha256="7ad3347849d8a3da6470135018d6af5fd8e58b4057cd568c3813695f2a04730d")

    provides("perl-json-pp-boolean")
    provides("perl-types-serialiser-booleanbase")
    provides("perl-types-serialiser-error")

    depends_on("perl-extutils-makemaker", type="build")

    depends_on("perl-common-sense", type=("build", "run", "test"))
