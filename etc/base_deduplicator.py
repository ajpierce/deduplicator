import sys
import os
from filehashdict import FileHashDict

class Deduplicator( object ):

    def __init__( self ):
        self.file_hash_dict = FileHashDict()
        self.directory = None
        self.verbose = False

    def set_directory( self, path ):
        self.directory = path

    def dedupe( self ):
        """ Perform deduplication on all files in the given directory """
        if not self.directory:
            print "Warning: no path specified for deduplication"
            sys.exit()

        print "Beginning deduplication process"
        for dirpath, dirnames, filenames in os.walk( self.directory ):
            for filename in filenames:
                full_path = os.path.join( dirpath, filename )
                self.file_hash_dict.add_file( full_path )

        print "List of duplicates compiled."
        dupes = self.file_hash_dict.get_duplicates()
        i = 0

        sys.stdout.write("Deleting {0} files".format( len(dupes) ))
        for duplicate_file_hash in dupes:
            os.remove( duplicate_file_hash.get_path() )
            if i%10 == 0:
                sys.stdout.write(".")
            i+=1

        print "\ndone!"
        sys.exit()
