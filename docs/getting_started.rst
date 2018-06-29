***************
Getting Started
***************

The first thing you’ll need to do to get started is install ChatterBot.

.. code-block:: bash

   pip install reference_sequence_fetcher

See Installation for options for alternative installation methods.

Create a new Fetcher instance
==============================
.. code-block:: python

   from reference_sequence_fetcher import Fetcher
   fetcher = Fetcher('<server_base_url>')

The only required parameter for the `Fetcher` is a server url. This will be the server which will be queried for fetching data

Fetch sequence data
===================

After creating a new Fetcher instance you can use ``fetch_sequence`` to get the
sequence which has only one required parameter i.e. checksum. You can query for
subsequence using start and end parameters. A detailed description
will be given in the API documentaion section.

.. code-block:: python

   print(fetcher.fetch_sequence('<checksum>'))

   print(fetcher.fetch_sequence('<checksum>', start=0, end=10))

Fetch metadata
==============

You can use ``fetch_metdata`` to get the metadata associated with a sequence
which has only one required parameter i.e. checksum.
A detailed description will be given in the API documentaion section.

.. code-block:: python

    print(fetcher.fetch_metadata('<checksum>'))
