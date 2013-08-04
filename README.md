epk
===

WIP standard for Snap! extensions


Standard (WIP)
------------

EPK (extension package) files are zip files. In the archive is a .conf file that sets the name, version, author, and dependencies of an extension. The archive also contains the extension's XML block module file and Python file.

.conf file structure
~~~~~~~~~~~~~~~~~~~~

[info]
name: Extension name
version: 0.1.33.7
author: Technoboy10
[dependencies]
dependencies: this, that, other
