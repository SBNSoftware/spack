# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlHtmlForm(PerlPackage):
    """Class that represents an HTML form element."""  # AUTO-CPAN2Spack

    homepage = "https://github.com/libwww-perl/HTML-Form"  # AUTO-CPAN2Spack
    url = "https://cpan.metacpan.org/authors/id/S/SI/SIMBABQUE/HTML-Form-6.10.tar.gz"

    license("Artistic-1.0-Perl OR GPL-1.0-or-later", checked_by="greenc-FNAL")

    maintainers("gartung", "greenc-FNAL", "marcmengel")  # AUTO-CPAN2Spack

    version("6.10", sha256="df8393e35e495a0839f06a63fb65d6922842c180d260554137728a9f092df9d3")
    version("6.09", sha256="f6c06ce1e54f9cfe1fd800d886126b875c972716a27fc281d3fb00345132e230")

    provides("perl-html-form-fileinput")  # AUTO-CPAN2Spack
    provides("perl-html-form-ignoreinput")  # AUTO-CPAN2Spack
    provides("perl-html-form-imageinput")  # AUTO-CPAN2Spack
    provides("perl-html-form-input")  # AUTO-CPAN2Spack
    provides("perl-html-form-keygeninput")  # AUTO-CPAN2Spack
    provides("perl-html-form-listinput")  # AUTO-CPAN2Spack
    provides("perl-html-form-submitinput")  # AUTO-CPAN2Spack
    provides("perl-html-form-textinput")  # AUTO-CPAN2Spack
    depends_on("perl-http-response", type=("build", "test"))  # AUTO-CPAN2Spack
    depends_on("perl@5.8.1:", type="run")  # AUTO-CPAN2Spack
    depends_on("perl-uri@1.10:", type="run")  # AUTO-CPAN2Spack
    depends_on("perl-html-tokeparser", type="run")  # AUTO-CPAN2Spack
    depends_on("perl-http-request-common@6.3:", type="run")  # AUTO-CPAN2Spack
    depends_on("perl-extutils-makemaker", type=("build", "test"))  # AUTO-CPAN2Spack
    depends_on("perl-http-request@6:", type="run")  # AUTO-CPAN2Spack
