**********************
Command Line Interface
**********************

To use command line interface, first install the package using pip3. You can then
access Fetcher functions using ``ref-seq-fetcher``

.. code-block:: bash

    ref-seq-fetcher --help

    ref-seq-fetcher [OPTIONS] COMMAND [ARGS]...

    Options:
    --help  Show this message and exit.

    Commands:
    metadata  retrieve metadata using base_url and checksum
    sequence  retrieve sequence using base_url and checksum


To retrieve a sequence
======================

.. code-block:: bash

    ref-seq-fetcher sequence --help

    sequence [OPTIONS] BASE_URL CHECKSUM

    retrieve sequence using base_url and checksum

    Options:
     -s, --start INTEGER   first byte of the checksum. 0-start inclusive
     -e, --end INTEGER     last byte of the checksum. 0-start exclusive
     --help                Show this message and exit.

server_base_url and checksum are required arguments while rest are optional. It internally
invokes classmethod sequence of Fetcher.

Examples
--------

.. code-block:: bash

    ref-seq-fetcher sequence https://www.ebi.ac.uk/ena/cram/ 6681ac2f62509cfc220d78751b8dc524
    CCACA........GTGGG

.. code-block:: bash

    ref-seq-fetcher sequence https://www.ebi.ac.uk/ena/cram/ 6681ac2f62509cfc220d78751b8dc524 --start 10 --end 20
    CCCACACACC


.. code-block:: bash

    ref-seq-fetcher sequence https://www.ebi.ac.uk/ena/cram/ 3332ed720ac7eaa9b3655c06f6b9e196 -s 5374 -e 5
    ATCCAACCTGCAGAGTT


To retrieve a metadata
======================

.. code-block:: bash

    ref-seq-fetcher metadata --help

    retrieve metadata using base_url and checksum

    Options:
      --help                Show this message and exit.


server_base_url and checksum are required arguments while rest are optional. It internally
invokes classmethod metadata of Fetcher.

Examples
--------

.. code-block:: bash

    ref-seq-fetcher metadata https://www.ebi.ac.uk/ena/cram/ 3332ed720ac7eaa9b3655c06f6b9e196 > metadata.json
