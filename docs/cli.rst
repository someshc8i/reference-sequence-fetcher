**********************
Command Line Interface
**********************

To use command line interface, first install the package using pip3. You can then
access Fetcher functions using ``ref-seq-fetcher``

To retrieve a sequence
======================

.. code-block:: bash

    ref-seq-fetcher sequence <server_base_url> <checksum> --start --end --fbs --lbs --encoding

server_base_url and checksum are required arguments while rest are optional. It internally
invokes classmethod sequence of Fetcher. Go through API documentaion. to have better undersanding of the arguments.
You can also use ``ref-seq-fetcher sequence -h``

Examples
--------

.. code-block:: bash

    ref-seq-fetcher sequence 111.11.1.0 6681ac2f62509cfc220d78751b8dc524
    CCACA........GTGGG

.. code-block:: bash

    ref-seq-fetcher sequence 111.11.1.0 6681ac2f62509cfc220d78751b8dc524 -start 10 -end 20
    CCCACACACC

.. code-block:: bash

    ref-seq-fetcher sequence 111.11.1.0 6681ac2f62509cfc220d78751b8dc524  -end 20


.. code-block:: bash

    ref-seq-fetcher sequence 111.11.1.0 3332ed720ac7eaa9b3655c06f6b9e196 -start 5374 -end 5
    ATCCAACCTGCAGAGTT

.. code-block:: bash

    ref-seq-fetcher sequence 111.11.1.0 681ac2f62509cfc220d78751b8dc524 -fbs 10 -lbs 19
    CCCACACACC

To retrieve a metadata
======================

.. code-block:: bash

    ref-seq-fetcher metadata <server_base_url> <checksum> --encoding

server_base_url and checksum are required arguments while rest are optional. It internally
invokes classmethod metadata of Fetcher. Go through API documentaion. to have better undersanding of the arguments.
You can also use ``ref-seq-fetcher metadata -h``

Examples
--------

.. code-block:: bash

    ref-seq-fetcher metadata 111.11.1.0 3332ed720ac7eaa9b3655c06f6b9e196 > metadata.json
