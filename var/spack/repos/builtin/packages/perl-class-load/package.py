# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlClassLoad(PerlPackage):
    """A working (require "Class::Name") and more"""

    homepage = "https://metacpan.org/pod/Class::Load"
    url = "https://cpan.metacpan.org/authors/id/E/ET/ETHER/Class-Load-0.24.tar.gz"

    license("GPL-1.0-or-later OR Artistic-1.0-Perl")

    version("0.25", sha256="2a48fa779b5297e56156380e8b32637c6c58decb4f4a7f3c7350523e11275f8f")
    version("0.24", sha256="0bb983da46c146534fc77a556d6e40d925142f2eb43103534025ee545265ca36")
    provides("perl-class-load-pp")
    depends_on("perl-package-stash@0.14:", type="run")
    depends_on("perl-extutils-makemaker", type=("build", "test"))
    depends_on("perl-data-optlist@0.110:", type="run")
    depends_on("perl-test-needs", type=("build", "test"))
    depends_on("perl@5.6:", type=("build", "run", "test"))
    depends_on("perl-module-implementation@0.4:", type="run")
    depends_on("perl-test-fatal", type=("build", "test"))
    depends_on("perl-module-runtime@0.12:", type="run")
    depends_on("perl-scalar-util", type="run")
    depends_on("perl-try-tiny", type="run")
