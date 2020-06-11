# Running a normal and global command

Normal command is for playing keystrokes in normal mode on the specified line
range. A global command is for running set of commands on a matching pattern

1. In the following text - move all ending with ' x' to the bottom.
  Solution: `:g/ x$/m$`
2. Find the first space and replace it with '-x-'
  Solution: `:'<,'>normal f xi-x-`

--  some text

line x
line y 
some line x
line z
some other line y
some more other line z

--  some other text


