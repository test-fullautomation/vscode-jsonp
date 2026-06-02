.. Copyright 2020-2023 Robert Bosch GmbH

.. Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

.. http://www.apache.org/licenses/LICENSE-2.0

.. Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

jsonp - vscode extension
========================

Table of Contents
-----------------

-  `Getting Started <#getting-started>`__

   -  `How to install <#how-to-install>`__
-  `Features <#features>`__
-  `Building the Extension <#building-the-extension>`__
-  `Contribution <#contribution>`__
-  `Package Documentation <#package-documentation>`__
-  `Feedback <#feedback>`__
-  `About <#about>`__

   -  `Maintainers <#maintainers>`__
   -  `Contributors <#contributors>`__
   -  `License <#license>`__

Getting Started
---------------

**VSCodeJsonp** is a VSCodium extension to support the enhanced JSON syntax (*jsonp*) used by
packages like the
`JsonPreprocessor <https://github.com/test-fullautomation/python-jsonpreprocessor>`_
and the
`RobotFramework_Testsuitesmanagement <https://github.com/test-fullautomation/robotframework-testsuitesmanagement>`_.


How to install
~~~~~~~~~~~~~~

This extension is currently not available on `Visual Studio Marketplace`_ or
`Open VSX Registry`_, so you can install it manually as  following steps:

- Get the latest extension *jsonp-x.x.x.vsix* file from this repo.
- Open `Visual Studio Code`_ or `VSCodium`_, select **Extensions** Tab then chose
  **Install from VSIX**
- Browse to the downloaded *jsonp-x.x.x.vsix* file then install.

As soon as the installtion is completed, the files with *.jsonp* will be
recognized properly.


Features
--------

Besides the basic JSON syntax, this extension helps to recognize and highlight the `jsonp` which includes:

- `"[import]"` syntax
- `param-assignment` syntax
- Updated `value` and `object` syntax for `jsonp`.
- Enabled `python inline code` syntax within `jsonp` files.

Extension Settings
------------------

When installing this vscode extension successfully, all files with `.jsonp` extension will be automatically highlighted as `jsonp` syntax.

In case you want files with `.json` to also be recognized as `jsonp` syntax, the below setting is required in vscode `settings.json` files

.. code::

   "files.associations": {
      "*.json": "jsonp"
   }

Building the Extension
----------------------

To build this extension from source, follow these steps:

1. Ensure you have Node.js and npm installed on your system.
2. Clone this repository to your local machine.
3. Navigate to the project directory in your terminal and browse to **VSCodeJsonp** folder.
4. Run the following commands

.. code::

   npm install
   npm run build

5. The built `.vsix` file will be available in the project directory.

Contribution
------------

We are always searching for support and you are cordially invited to help improve this vscode extension.

Package Documentation
---------------------

A detailed documentation of the **VSCodeJsonp** can be found here:
`VSCodeJsonp.pdf <https://github.com/test-fullautomation/vscode-jsonp/blob/develop/VSCodeJsonp/VSCodeJsonp.pdf>`_

Feedback
--------

To give us a feedback, you can send an email to `Thomas Pollerspöck <mailto:Thomas.Pollerspoeck@de.bosch.com>`_

In case you want to report a bug or request any interesting feature, please don't hesitate to raise a ticket.

About
-----

Maintainers
~~~~~~~~~~~

`Thomas Pollerspöck`_

`Tran Duy Ngoan`_

Contributors
~~~~~~~~~~~~

`Holger Queckenstedt`_

License
~~~~~~~

Copyright 2020-2023 Robert Bosch GmbH

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    |License: Apache v2|

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.


.. |License: Apache v2| image:: https://img.shields.io/pypi/l/robotframework.svg
   :target: http://www.apache.org/licenses/LICENSE-2.0.html
.. _Visual Studio Marketplace: https://marketplace.visualstudio.com/vscode
.. _Open VSX Registry: https://open-vsx.org/
.. _Visual Studio Code: https://code.visualstudio.com/
.. _VSCodium: https://vscodium.com/
.. _Thomas Pollerspöck: mailto:Thomas.Pollerspoeck@de.bosch.com
.. _Tran Duy Ngoan: mailto:Ngoan.TranDuy@vn.bosch.com
.. _Holger Queckenstedt: mailto:Holger.Queckenstedt@de.bosch.com
