# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PySphinxJinja2Compat(PythonPackage):
    """Patches Jinja2 v3 to restore compatibility with earlier Sphinx versions."""

    homepage = "https://github.com/sphinx-toolbox/sphinx-jinja2-compat"
    pypi = "sphinx_jinja2_compat/sphinx_jinja2_compat-0.2.0.post1.tar.gz"

    maintainers("gartung", "greenc-FNAL", "LydDeb", "marcmengel")

    license("MIT")

    version(
        "0.2.0.post1", sha256="974289a12a9f402108dead621e9c15f7004e945d5cfcaea8d6419e94d3fa95a3"
    )
    version("0.2.0", sha256="c41346d859653e202b623f4236da8936243ed734abf5984adc3bef59d6f9a946")

    depends_on("py-whey", type="build")
    depends_on("py-whey-pth", type="build")
    depends_on("py-jinja2@2.10:", type=("build", "run"))
    depends_on("py-markupsafe@1:", type=("build", "run"))
