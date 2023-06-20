# **************************************************************************************************************
#
#  Copyright 2020-2023 Robert Bosch GmbH
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
# **************************************************************************************************************
#
# setup.py
#
# XC-CT/ECA3-Queckenstedt
#
# Extends the standard setuptools installation by adding the documentation in PDF format
# (requires installation mode) and tidying up some folders.
#
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#
# This script deletes folders (as defined in config.CRepositoryConfig, depending on the position of this script):
# - previous builds within this repository folder
#
#                                         !!! USE WITH CAUTION !!!
#
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#
# --------------------------------------------------------------------------------------------------------------
#
# 25.10.2022
#
# --------------------------------------------------------------------------------------------------------------

import os, sys, platform, shlex, subprocess
import setuptools
from setuptools.command.install import install

from config.CRepositoryConfig import CRepositoryConfig # providing repository and environment specific information
from additions.CExtendedSetup import CExtendedSetup # providing functions to support the extended setup process

import colorama as col

col.init(autoreset=True)

COLBR = col.Style.BRIGHT + col.Fore.RED
COLBY = col.Style.BRIGHT + col.Fore.YELLOW
COLBG = col.Style.BRIGHT + col.Fore.GREEN

SUCCESS = 0
ERROR   = 1

# --------------------------------------------------------------------------------------------------------------

def printerror(sMsg):
    sys.stderr.write(COLBR + f"Error: {sMsg}!\n")

def printexception(sMsg):
    sys.stderr.write(COLBR + f"Exception: {sMsg}!\n")

# --------------------------------------------------------------------------------------------------------------

# !!! CURRENTLY UNDER DISCUSSION !!!

# # class ExtendedInstallCommand(install):
    # # """Extended setup for installation mode."""

    # # def run(self):

        # # listCmdArgs = sys.argv
        # # if ( ('install' in listCmdArgs) or ('build' in listCmdArgs) or ('sdist' in listCmdArgs) or ('bdist_wheel' in listCmdArgs) ):
            # # install.run(self)
        # # return SUCCESS

# # # eof class ExtendedInstallCommand(install):

# --------------------------------------------------------------------------------------------------------------

# -- Even in case of other command line parameters than 'install' or 'build' are used we need the following objects.
#    (Without repository configuration commands like '--author-email' would not be possible)

# -- setting up the repository configuration
oRepositoryConfig = None
try:
    oRepositoryConfig = CRepositoryConfig(os.path.abspath(sys.argv[0]))
except Exception as ex:
    print()
    printexception(str(ex))
    print()
    sys.exit(ERROR)

# -- setting up the extended setup
oExtendedSetup = None
try:
    oExtendedSetup = CExtendedSetup(oRepositoryConfig)
except Exception as ex:
    print()
    printexception(str(ex))
    print()
    sys.exit(ERROR)

# --------------------------------------------------------------------------------------------------------------

long_description = "long description" # variable is required even in case of other command line parameters than 'install' or 'build' are used

# !!! CURRENTLY UNDER DISCUSSION !!!
# listCmdArgs = sys.argv
# if ( ('install' in listCmdArgs) or ('build' in listCmdArgs) or ('sdist' in listCmdArgs) or ('bdist_wheel' in listCmdArgs) ):

print()
print(COLBY + "Entering extended installation")
print()

print(COLBY + "Extended setup step 1/2: Calling the documentation builder")
print()

nReturn = oExtendedSetup.genpackagedoc()
if nReturn != SUCCESS:
    sys.exit(nReturn)

print(COLBY + "Extended setup step 2/2: Converting the repository README")
print()

nReturn = oExtendedSetup.convert_repo_readme()
if nReturn != SUCCESS:
    sys.exit(nReturn)


# !!! CURRENTLY UNDER DISCUSSION !!!

# print(COLBY + "Extended setup step 3/4: Deleting previous setup outputs (build, dist, <package name>.egg-info within repository)")
# print()

# nReturn = oExtendedSetup.delete_previous_build()
# if nReturn != SUCCESS:
    # sys.exit(nReturn)

README_MD = str(oRepositoryConfig.Get('README_MD'))
with open(README_MD, "r", encoding="utf-8") as fh:
    long_description = fh.read()
fh.close()

# --------------------------------------------------------------------------------------------------------------

# !!! CURRENTLY UNDER DISCUSSION !!!

# -- the 'setup' itself

# # # print(COLBY + "Extended setup step 5/5: install.run(self)")
# # # print()

# # # setuptools.setup(
    # # # name         = str(oRepositoryConfig.Get('PACKAGENAME')),
    # # # version      = str(oRepositoryConfig.Get('PACKAGEVERSION')),
    # # # author       = str(oRepositoryConfig.Get('AUTHOR')),
    # # # author_email = str(oRepositoryConfig.Get('AUTHOREMAIL')),
    # # # description  = str(oRepositoryConfig.Get('DESCRIPTION')),
    # # # long_description = long_description,
    # # # long_description_content_type = str(oRepositoryConfig.Get('LONGDESCRIPTIONCONTENTTYPE')),
    # # # url = str(oRepositoryConfig.Get('URL')),
    # # # packages = [str(oRepositoryConfig.Get('PACKAGENAME')),
                # # # str(oRepositoryConfig.Get('PACKAGENAME')) + ".Comparison",
                # # # str(oRepositoryConfig.Get('PACKAGENAME')) + ".String",
                # # # str(oRepositoryConfig.Get('PACKAGENAME')) + ".Utils",
                # # # str(oRepositoryConfig.Get('PACKAGENAME')) + ".File",
                # # # str(oRepositoryConfig.Get('PACKAGENAME')) + ".Folder"],
    # # # classifiers = [
        # # # str(oRepositoryConfig.Get('PROGRAMMINGLANGUAGE')),
        # # # str(oRepositoryConfig.Get('LICENCE')),
        # # # str(oRepositoryConfig.Get('OPERATINGSYSTEM')),
        # # # str(oRepositoryConfig.Get('DEVELOPMENTSTATUS')),
        # # # str(oRepositoryConfig.Get('INTENDEDAUDIENCE')),
        # # # str(oRepositoryConfig.Get('TOPIC')),
    # # # ],
    # # # python_requires = str(oRepositoryConfig.Get('PYTHONREQUIRES')),
    # # # cmdclass={
        # # # 'install': ExtendedInstallCommand,
    # # # },
    # # # install_requires = oRepositoryConfig.Get('INSTALLREQUIRES'),
    # # # package_data={f"{oRepositoryConfig.Get('PACKAGENAME')}" : oRepositoryConfig.Get('PACKAGEDATA')},
# # # )

# --------------------------------------------------------------------------------------------------------------

print()
print(COLBG + "Extended installation done")
print()

# --------------------------------------------------------------------------------------------------------------

