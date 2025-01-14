# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PySphinxBookTheme(PythonPackage):
    """Lightweight Sphinx theme designed to mimic the look-and-feel of an interactive book."""

    homepage = "https://sphinx-book-theme.readthedocs.io/en/latest"
    pypi = "sphinx_book_theme/sphinx_book_theme-1.0.1.tar.gz"

    license("BSD-3-Clause")

    maintainers("gartung", "greenc-FNAL", "marcmengel")

    version("1.0.1", sha256="927b399a6906be067e49c11ef1a87472f1b1964075c9eea30fb82c64b20aedee")
    version("0.3.3", sha256="0ec36208ff14c6d6bf8aee1f1f8268e0c6e2bfa3cef6e41143312b25275a6217")

    depends_on("python@3.7:", type=("build", "run"))

    depends_on("py-sphinx-theme-builder@0.2.0a7:", type="build")

    depends_on("py-sphinx@4:6", type=("build", "run"))
    depends_on("py-pydata-sphinx-theme@0.13.3:", type=("build", "run"))
