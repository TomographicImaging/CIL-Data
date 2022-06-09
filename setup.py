# -*- coding: utf-8 -*-
#  CCP in Tomographic Imaging (CCPi) Core Imaging Library (CIL).

#   Copyright 2017 UKRI-STFC
#   Copyright 2017 University of Manchester

#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at

#   http://www.apache.org/licenses/LICENSE-2.0

#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

from setuptools import setup
import os
import sys


cil_version='22.0.0'

setup(
    name="cil-data",
    version=cil_version,
    data_files = [('share/cil', [ '24737_fd_normalised.nxs',
                                  'boat.tiff',
                                  'camera.png',
                                  'peppers.tiff',
                                  'rainbow.png',
                                  'resolution_chart.tiff',
                                  'shapes.png',
                                  'sim_volume.nxs',
                                  'sim_cone_beam.nxs',
                                  'sim_parallel_beam.nxs',
                                  'headsq.mha'
                                  ])],

    # metadata for upload to PyPI
    author="CCPi developers",
    maintainer="Edoardo Pasca",
    maintainer_email="edoardo.pasca@stfc.ac.uk",
    description='CCPi Core Imaging Library - Example Data',
    license="Apache v2.0",
    keywords="Dataset",
    url="http://www.ccpi.ac.uk/cil",   # project home page, if any

)
