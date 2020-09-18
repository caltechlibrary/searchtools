Searchtools
=====================================================

This is a Python3 package for working with Elasticsearch and
LunrJS services and indexes. It provides a uniform approach
for our various library projects where one or both platforms
are appropriate.

[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg?style=flat-square)](https://choosealicense.com/licenses/bsd-3-clause)
[![Latest release](https://img.shields.io/github/v/release/caltechlibrary/template.svg?style=flat-square&color=b44e88)](https://github.com/caltechlibrary/template/releases)


Table of contents
-----------------

* [Introduction](#introduction)
* [Installation](#installation)
* [Usage](#usage)
* [Known issues and limitations](#known-issues-and-limitations)
* [Getting help](#getting-help)
* [License](#license)
* [Authors and history](#authors-and-history)
* [Acknowledgments](#authors-and-acknowledgments)


Introduction
------------

Caltech Library is working with both LunrJS for small site and offline
resources as well as Elasticsearch. Both consume JSON to build their
indexes and it seems reasonable to beable to build search ui and
indexers to support both using a common setup of calls based on
an application's configuration.

This package provides logging, configuration and other useful
elements for building an indexer and search UI 
for both LunrJS static site integration or Flask based
Python services that host the search UI.


Installation
------------

This package requires Python3.7 or better.

For Elasticsearch you'll need to have an Elasticsearch services available.
See https://www.elastic.co/ for more information about use their services
in the cloud or running locally. This package targets the current stable
release of Elasticsearch which at this time is 7.9 (2020-09-17).

LunrJS is a JavaScript library for providing search of small website
that are hosted on a static platform.  The typical usecase is to 
build the indexes using the LunrJS library and host the result on our
website.  See https://lunrjs.com/ for more details. There is a Python
package called Lunr that supports building indexes via Python without
the need to run NodeJS. This package uses https://pypi.org/project/lunr/
version 0.5.8.

Installation steps

1. clone this repository
2. change into your cloned repository directory
3. run setup.py


```bash
    git clone git@github.com:caltechlibrary/searchtools
    cd searchtools
    python3 setup.py install
```


Usage
-----

The repository is a Python package. You would use it to build other
applications (e.g. a specific website's search UI).

### _Example Usage_

FIXME: Need to write a basic example

Known issues and limitations
----------------------------

This library does not provide standalone general purpose 
search UI for Elasticsearch or LunrJS.

Getting help
------------

If you need help or have question use the repository's
GitHub [Issue](https://github.com/caltechlibrary/searchtools/issues) tracker.

License
-------

Software produced by the Caltech Library is Copyright (C) 2020, Caltech.  This software is freely distributed under a BSD/MIT type license.  Please see the [LICENSE](LICENSE) file for more information.


Authors and history
---------------------------

In this section, list the authors and contributors to your software project.  Adding additional notes here about the history of the project can make it more interesting and compelling.  This is also a place where you can acknowledge other contributions to the work and the use of other people's software or tools.


Acknowledgments
---------------

This work was funded by the California Institute of Technology Library.

(If this work was also supported by other organizations, acknowledge them here.  In addition, if your work relies on software libraries, or was inspired by looking at other work, it is appropriate to acknowledge this intellectual debt too.)

<div align="center">
  <br>
  <a href="https://www.caltech.edu">
    <img width="100" height="100" src=".graphics/caltech-round.svg">
  </a>
</div>
