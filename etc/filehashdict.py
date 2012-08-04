from filehash import FileHash
import hashlib
import sys

class FileHashDict:
    """ FileHashDict is a dictionary of FileHashes. You can pass filenames to be
    hashed and catalogued.

    Keys are FileHashes
    Values are the number of collisions for a given hash """

    def __init__( self ):
        self.hash_dict = {}
        self.duplicates = []

    def purge_dict( self ):
        """ Deletes all records from the dict """
        self.hash_dict = {}

    def add_file( self, path ):
        """ Adds the file at the given path to FileHashDict in the following
        steps:

        1. Ensure that the file exists; throw an error otherwise
        2. Hash the file
        3. Create a FileHash with the hash and the path
        4. Insert the FileHash into the FileHashDict """

        # -- Step 1
        try:
            with open(path) as f: pass
        except IOError as e:
            print "Specified path does not exist! {0}".format( e )

        # -- Step 2
        hash_value = self._hash_file( path )

        # -- Step 3
        file_hash = FileHash( file_hash=hash_value, file_path=path )

        # -- Step 4
        if self.hash_dict.get(file_hash, False):
            self.hash_dict[file_hash] += 1
            self.duplicates.append( file_hash )
        else:
            self.hash_dict[file_hash] = 0

    def print_dict( self ):
        print self.hash_dict

    def print_duplicates( self ):
        print self.duplicates

    def _hash_file( self, path ):
        hash_obj = hash()
        for chunk in _chunk_generator( open(path, 'rb') ):
            hash_obj.update( chunk )

        return hash_obj.digest()

    def _chunk_generator( self, fobj, chunk_size=1024 ):
        """ Generator that reads a file in chunks of bytes """
        while True:
            chunk = fobj.read(chunk_size)
            if not chunk:
                return
            yield chunk
