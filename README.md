I wanted to understand how RatOS was presenting itsef as a klipper configuration. As RatOS is very modular, it utilizes quite a number of include files, which sometimes makes it a bit tedious to see what all is included. The klippy log has the interpreted view, but it does not retain the original indentation or comments in the include files.

This simple python script reads the printer.cfg file (or any other that you want to start with) and builds a flat file that has all the included files expanded in that single file. You _should_ be able to use this single file as your sole printer.cfg file, but I have never tried it. 

This software is probably full of bugs, only works for me, and will probably ruin your printer and computer, and anything that comes in contact with it.
