********************
Retrieving sequences
********************

.. |n| raw:: html

    <br />

Complete sequence query
=======================
Complete sequence can be retrieved using only the required parameter checksum in
``fetch_sequence`` function or ``Fetcher.sequence`` class method.

.. code-block:: python

    from reference_sequence_fetcher import fetcher
    fetcher = Fetcher(<server_base_url>)
    print(fetcher.fetch_sequence('<checksum>'))

    print(Fetcher.sequence(<server_base_url>, <checksum>))


Sub-sequence query
==================

User can also retrieve sub-sequences either of the two given ways

Using start-end parameters
--------------------------

start and end used to retrieve sub-subsequence of specified bytes. Start is inclusive
and end is exclusive. |n|
0 <= start < length of sequence ; 0 <= end <= length of sequence

For ex sequence A is given as ``ATGCATGCATGC`` |n|
Length is 12 |n|

.. code-block:: python


    >>fetcher = Fetcher(<server_base_url>)
    >>print(fetcher.fetch_sequence('<checksum>'), start=0, end=5)
    >>ATGCA

start and end can also used to retrieve circular sequences in a circular manner

.. code-block:: python


    >>fetcher = Fetcher(<server_base_url>)
    >>print(fetcher.fetch_sequence('<checksum>'), start=5, end=2)
    >>TGCATGCATG

so TGCATGC + ATG is the retrieved sequence.

.. note ::

    Only start and end can be used to retrieve circular sequences.




Using fbs-lbs parameters
------------------------

fbs(first-byte-spec) and lbs(last-byte-spec) used to retrieve sub-subsequence of specified bytes. fbs
and lbs are inclusive. |n|
0 <= fbs <= lbs < length of sequence

For ex sequence A is given as ``ATGCATGCATGC`` |n|
Length is 12 |n|

.. code-block:: python


    >>fetcher = Fetcher(<server_base_url>)
    >>print(fetcher.fetch_sequence('<checksum>'), fbs=0, lbs=5)
    >>ATGCA

.. warning ::

    fbs lbs can not be used to retrieve circular sequences in a circular manner as fbs <= lbs must be True


Important Points
----------------

 * start-end passes as query params where fbs-lbs are byte values passed in Range header
 * fbs-lbs should be used in case of non-circular retrieval
 * start-end must be used in case of circular retrieval
 * start and end can be used alone. If only start is given, end is assumed to be equal to length of the sequences. When only end is given start is assumed to be equal to 0.
 * fbs and lbs can not used alone
 * start-end can not be used with fbs-lbs
