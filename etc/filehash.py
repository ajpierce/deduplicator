class FileHash:
    """ FileHash is a slotted object that contains a file hash and the path to
    the file to which the hash belongs

    The __slots__ declaration takes a sequence of instance variables and 
    reserves just enough space in each instance to hold a value for each 
    variable. Space is saved because __dict__ is not created for each instance.
    """

    __slots__ = ( 'file_hash', 'file_path' )

    def __init__( self, file_hash, file_path ):
        """ You must pass in the hash and path on object instantiation """
        self.file_hash = file_hash
        self.file_path = file_path

    def get_hash( self ):
        return self.file_hash

    def get_path( self ):
        return self.file_path

    def __str__( self ):
        return '( {0} | {1} )'.format( self.file_hash, self.file_path )

    def __eq__( self, other ):
        """ When comparing FileHashes, we only want to look at the hash, not
        at the path. This allows us to catch collisions easier in the 
        FileHashDict """
        return self.file_hash == other.file_hash
