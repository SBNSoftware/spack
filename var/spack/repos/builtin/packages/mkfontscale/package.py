# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Mkfontscale(AutotoolsPackage, XorgPackage):
    """mkfontscale creates the fonts.scale and fonts.dir index files used by the
    legacy X11 font system."""

    homepage = "https://cgit.freedesktop.org/xorg/app/mkfontscale"
    xorg_mirror_path = "app/mkfontscale-1.1.2.tar.gz"

    version("1.1.3", sha256="449b8ccd44133e260eafab55f18937c09fd4846b87f288f1c9611e4810e13bb2")
    version("1.1.2", sha256="8bba59e60fbc4cb082092cf6b67e810b47b4fe64fbc77dbea1d7e7d55312b2e4")

    depends_on("libfontenc")
    depends_on("freetype")

    depends_on("xproto@7.0.25:")
    depends_on("pkgconfig", type="build")
    depends_on("util-macros", type="build")
