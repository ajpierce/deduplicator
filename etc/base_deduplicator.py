from filehashdict import FileHashDict

class Deduplicator( object ):

    def __init__( self ):
        self.file_hash_dict = FileHashDict()

    def set_directory( self, path ):
        self.directory = path

    def set_recursive( self, recursive ):
        self.recursive = recursive

    def dedupe( self ):
        """ Perform deduplication on all files in the given directory """
        print "Beginning deduplication process"
