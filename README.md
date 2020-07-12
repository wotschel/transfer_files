# transfer_files
Transfer files from mounted device (memory card) to the local disc.

When coming home from a photoshooting it is always the same boring procedere.

1. mount the memory card
2. copy the new files
3. make a local folder
4. paste the files

This script takes the steps 2-4 for you.

Usage:

./transfer_files.py subfoldername

You have to adjust the local imagefolder and the mountpoint of your memorycard.

Known problem: The script looks for local and remote filenames, not hashes. If you have a file 0000.jpg on the local disc and your camera names a new file 0000.jpg it will be not copied.
