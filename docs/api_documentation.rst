*****************
API Documentation
*****************
.. class:: Fetcher(base_url)

    Act as a factory class for sequence and metadata

    :param base_url: Base url of the server from which data to be fetched
    :type base_url: string

    .. py:method:: get_base_url()

        Return base_url of the Fetcher object

        :rtype: string

    .. py:method:: set_base_url(base_url)

        Set base_url of the Fetcher object. Used to change the base url of already instantiated object on the fly.

        :param base_url: Base url of the server from which data to be fetched
        :type base_url: string

        :rtype: void

    .. py:method:: fetch_sequence(checksum, [start=None, end=None, fbs=None, lbs=None, encoding=None])

        Act as factory method for retrieving sequences

        :param checksum: Checksum identifier of the sequence to be retrieved
        :type checksum: string

        :param start: Used to define start location of the sequence to be retrieved (inclusive)
        :type start: integer

        :param end: Used to define end location of the sequence to be retrieved (exclusive)
        :type end: integer

        :param fbs: first-byte-spec used to define start location of the sequence to be retrieved (inclusive)
        :type fbs: integer

        :param lbs: last-byte-spec used to define end location of the sequence to be retrieved (inclusive)
        :type lbs: integer

        :param encoding: To be passed in Accept header of the http request. Default used by the server is text/plain
        :type encoding: string

        :rtype: string

    .. py:method:: fetch_metadata(checksum, [encoding=None])

        Act as factory method for retrieving sequences

        param checksum: Checksum identifier of the sequence to be retrieved
        :type checksum: string

        :param encoding: To be passed in Accept header of the http request. Default used by the server is application/json
        :type encoding: string

        :rtype: dict

    .. py:classmethod:: sequence(base_url, checksum, [start=None, end=None, fbs=None, lbs=None, encoding=None])

        A class method for easily fetching single sequence without creating Fetcher object.
        Parameters definitions as per defined above

    .. py:classmethod:: metdata(base_url, checksum, [encoding=None])

        A class method for easily fetching single metadata without creating Fetcher object.
        Parameters definitions as per defined above
