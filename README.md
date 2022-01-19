# stringreverse

Where a file has been obfuscated by reversing and flipping its constituant lines, stringreverse will flip them back.

Unreversed Example:
,ss2
coler.@
crsr.`
txet.
.edom SOD ni nur eb tonnac margorp sihT!

Reversed Example
!This program cannot be run in DOS mode.
.text
`.rsrc
@.reloc
2ss,

Usage: [required] --file [optional] --debug --help
Example: ./stringreverse.py --file yourfile.123 --debug
Required Arguments:
--file - File being opened.
Optional Arguments:
--output - output file name of the new executable.  Will be output.exe by default otherwise.
--debug - Prints verbose logging to the screen to troubleshoot issues with a recon installation.
--help - You're looking at it!
