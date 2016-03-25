# play
Searching and playing your favorites musics (mp3) from command shell

================================================================================================
Pre-requisites:
================================================================================================
- Python version 2.7 or above
- VLC

================================================================================================
How-To:
================================================================================================
Usage: play <options> <keywords>

Options:
- -Z -> Play files randomly forever (default disabled)
- -L -> Repeat all (default disabled)
- -R -> Repeat current item (default disabled)

Keywords:
- --all -> Searches all mp3 files generating a playlist and execute it.

Example:
- $ play -R
- $ play --all
- $ play -R --all
- $ play -Z metallica
- $ play beatles let it be

================================================================================================
History:
================================================================================================
- Version 1.0 - 03/21/2016 - Coding the first version
- Version 1.1 - 03/24/2016 - Added a validation the arguments
- Version 1.2 - 03/25/2016 - Cleaning the code

================================================================================================
Issues:
================================================================================================
- Unknow

================================================================================================
Next Activities:
================================================================================================
- search and play videos (avi)
- search and view photos (jpeg)
