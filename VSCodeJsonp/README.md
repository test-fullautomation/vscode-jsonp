# jsonp - vscode extension

## Table of Contents

- [Getting Started](#getting-started)
  - [How to install](#how-to-install)
- [Features](#features)
- [Building the Extension](#building-the-extension)
- [Contribution](#contribution)
- [Package Documentation](#package-documentation)
- [Feedback](#feedback)
- [About](#about)
  - [Maintainers](#maintainers)
  - [Contributors](#contributors)
  - [License](#license)

## Getting Started

**VSCodeJsonp** is a VSCodium extension to support the enhanced JSON
syntax (*jsonp*) used by packages like the
[JsonPreprocessor](https://github.com/test-fullautomation/python-jsonpreprocessor)
and the
[RobotFramework_Testsuitesmanagement](https://github.com/test-fullautomation/robotframework-testsuitesmanagement).

### How to install

This extension is currently not available on [Visual Studio
Marketplace](https://marketplace.visualstudio.com/vscode) or [Open VSX
Registry](https://open-vsx.org/), so you can install it manually as
following steps:

- Get the latest extension *jsonp-x.x.x.vsix* file from this repo.
- Open [Visual Studio Code](https://code.visualstudio.com/) or
  [VSCodium](https://vscodium.com/), select **Extensions** Tab then
  choose **Install from VSIX**
- Browse to the downloaded *jsonp-x.x.x.vsix* file then install.

As soon as the installation is completed, the files with *.jsonp* will be
recognized properly.

## Features

Besides the basic JSON syntax, this extension helps to recognize and
highlight the [jsonp]{.title-ref} which includes:

- `"[import]"` syntax:

   ![jsonp-import](https://github.com/test-fullautomation/vscode-jsonp/blob/develop/VSCodeJsonp/images/jsonp-import.png?raw=true)

- `param-assignment` syntax:

   ![jsonp-param-assignment](https://github.com/test-fullautomation/vscode-jsonp/blob/develop/VSCodeJsonp/images/jsonp-param-assignment.png?raw=true)

With new supported `jsonp` syntax, the JSON value and object syntax are
updated as below:

- `value`:

   ![jsonp-value](https://github.com/test-fullautomation/vscode-jsonp/blob/develop/VSCodeJsonp/images/jsonp-value.png?raw=true)

- `object`:

   ![jsonp-object](https://github.com/test-fullautomation/vscode-jsonp/blob/develop/VSCodeJsonp/images/jsonp-object.png?raw=true)

## Extension Settings

When installing this vscode extension successfully, all files with
[.jsonp]{.title-ref} extension will be automatically highlighted as
[jsonp]{.title-ref} syntax.

In case you want files with [.json]{.title-ref} to also be recognized as
[jsonp]{.title-ref} syntax, the below setting is required in vscode
[settings.json]{.title-ref} files

```
"files.associations": {
   "*.json": "jsonp"
}
```

## Building the Extension

To build this extension from source, follow these steps:

1.  Ensure you have Node.js and npm installed on your system.
2.  Clone this repository to your local machine.
3.  Navigate to the project directory in your terminal and browse to
    **VSCodeJsonp** folder.
4.  Run the following commands

```
npm install
npm run build
```

5.  The built [.vsix]{.title-ref} file will be available in the project
    directory.

## Contribution

We are always searching for support and you are cordially invited to
help improve this vscode extension.

## Package Documentation

A detailed documentation of the **VSCodeJsonp** can be found here:
[VSCodeJsonp.pdf](https://github.com/test-fullautomation/vscode-jsonp/blob/develop/VSCodeJsonp/VSCodeJsonp.pdf)

## Feedback

To give us a feedback, you can send an email to [Thomas
Pollerspöck](mailto:Thomas.Pollerspoeck@de.bosch.com)

In case you want to report a bug or request any interesting feature,
please don\'t hesitate to raise a ticket.

## About

### Maintainers

[Thomas Pollerspöck](mailto:Thomas.Pollerspoeck@de.bosch.com)

[Tran Duy Ngoan](mailto:Ngoan.TranDuy@vn.bosch.com)

### Contributors

[Holger Queckenstedt](mailto:Holger.Queckenstedt@de.bosch.com)

### License

Copyright 2020-2023 Robert Bosch GmbH

Licensed under the Apache License, Version 2.0 (the \"License\"); you
may not use this file except in compliance with the License. You may
obtain a copy of the License at

> [![License: Apache
> v2](https://img.shields.io/pypi/l/robotframework.svg)](http://www.apache.org/licenses/LICENSE-2.0.html)

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an \"AS IS\" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
