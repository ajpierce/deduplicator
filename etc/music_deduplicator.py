from base_deduplicator import Deduplicator

class MusicDeduplicator( Deduplicator ):

    def __init__( self ):
        super( MusicDeduplicator, self ).__init__()
        self.FILE_EXTENSIONS = [ 
            "3gp",
            "act",
            "AIFF ",
            "aac",
            "ALAC ",
            "amr",
            "Au",
            "awb",
            "dct",
            "dss",
            "dvf",
            "flac",
            "gsm",
            "iklax",
            "IVS",
            "m4a",
            "m4p",
            "mmf",
            "mp3",
            "mpc",
            "msv",
            "mxp4",
            "ogg",
            "ram",
            "raw",
            "TTA",
            "vox",
            "wav",
            "wma",
        ]
