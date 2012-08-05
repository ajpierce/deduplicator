from filehash import FileHash
import hashlib
import sys

class FileHashDict:
    """ FileHashDict is a dictionary of FileHashes. You can pass filenames to be
    hashed and catalogued.

    Keys are FileHashes
    Values are the number of collisions for a given hash """

    def __init__( self ):
        self.file_dict = {}
        self.duplicates = []
        self.uniques = []

    def purge_dict( self ):
        """ Deletes all records from the dict """
        self.file_dict = {}

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
        #print "Hash value is: {0}".format(hash_value)

        # -- Step 3
        file_hash = FileHash( hash_value=hash_value, file_path=path )

        # -- Step 4
        if self.file_dict.has_key(file_hash.hash_value):
            self.file_dict[file_hash.hash_value] += 1
            self.duplicates.append( file_hash )
        else:
            self.file_dict[file_hash.hash_value] = 0
            self.uniques.append( file_hash )

    def print_dict( self ):
        print self.file_dict

    def get_duplicates( self ):
        return self.duplicates

    def get_uniques( self ):
        return self.uniques

    # -- Private Helper Functions
    def _hash_file( self, path ):
        hash_obj = hashlib.sha256()
        print "Hashing file: {0}".format(path)

        for chunk in self._chunk_generator( open(path, 'rb') ):
            hash_obj.update( chunk )

        return hash_obj.digest()

    def _chunk_generator( self, fobj, chunk_size=1024 ):
        """ Generator that reads a file in chunks of bytes """
        while True:
            chunk = fobj.read(chunk_size)
            if not chunk:
                return
            yield chunk

    # -- Overrides
    def __str__( self ):
        """
        return str( "\n".join([ "{0}:{1}".format(
            file_hash.get_path(), self.file_dict[file_hash] 
            ) for file_hash in self.file_dict ]) )
        """
        return str( "\n".join([ "{0} :: {1}".format(
            file_hash, self.file_dict[file_hash] 
            ) for file_hash in self.file_dict ]) )
