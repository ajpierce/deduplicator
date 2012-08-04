class FileHash:
    """ FileHash is a slotted object that contains a file hash and the path to
    the file to which the hash belongs

    The __slots__ declaration takes a sequence of instance variables and 
    reserves just enough space in each instance to hold a value for each 
    variable. Space is saved because __dict__ is not created for each instance.
    """

    __slots__ = ( 'hash_value', 'file_path' )

    def __init__( self, hash_value, file_path ):
        """ You must pass in the hash and path on object instantiation """
        self.hash_value = hash_value
        self.file_path = file_path

    def get_hash( self ):
        return self.hash_value

    def get_path( self ):
        return self.file_path

    def __str__( self ):
        return '( {0} | {1} )'.format( self.hash_value, self.file_path )

    def __eq__( self, other ):
        """ When comparing FileHashes, we only want to look at the hash, not
        at the path. This allows us to catch collisions easier in the 
        FileHashDict """
        return self.hash_value == other.hash_value

    def __comp__( self, other ):
        return cmp( self.hash_value, other.hash_value )

    def __hash__( self ):
        #return self.hash_value
        return id(self.hash_value)
