Deduplicator
============

Why Deduplicator?
-----------------
Deduplicator came into existance because, through some combination of sorcery,
confusion, and bad habits, my wife managed to duplicate almost every file in
her music library (at least) 4 times. It got so bad that tears threatened to
fall, because "no matter how many times [she] cleans them up, they keep coming
back."

Geek husband to the rescue.

What is Deduplicator?
---------------------
An over-engineered hack to delete duplicate files, regardless of what their 
filesnames are.

How does it work?
-----------------
Deduplicator looks (recursively) though a specified directory, and compares
all files (that match a given file extension or pattern specified in the
self.FILE_EXTENSIONS variable) to each other by first hashing the file and
then storing that hash in a dictionary. Files that produce duplicate hashes are
then blacklisted and deleted once the directory has been thoroughly trawled.
