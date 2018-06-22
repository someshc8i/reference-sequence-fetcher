.. reference-sequence-fetcher documentation master file, created by
   sphinx-quickstart on Wed Jun 20 18:39:03 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

reference-sequence-fetcher's documentation
==========================================

reference-sequence-fetcher is a python client to retrieve sequence and metadata
from reference servers in a user friendly and easy to use manner. It has requests
library at its heart and allows you to fetch sequences using a Fetcher object.

An example would be like::

    >>from reference_sequence_fetcher import fetcher
    >>fethcer = Fetcher('yourserver.com')
    >>fetcher.fetch_sequence('<checksum>')
    >>ATGCATCGACTG.......ATGCATCGACTG

Fetcher object typically has two methods:
 * `fetch_sequence` to fetch the sequence metadata
 * `fetch_metadata` to fetch the metadata of the sequence

and two class methods `sequenece` and `metadata`

.. note::

    reference-sequence-fetcher is stable only for Python3

.. toctree::
   :maxdepth: 3

   installation
   getting_started
   sequences
   api_documentation
   examples
   cli
   development



Report an Issue
===============

Please direct all bug reports and feature requests to the project’s issue tracker on GitHub.

Indices and tables
==================
 * :ref:`genindex`
 * :ref:`modindex`
 * :ref:`search`
