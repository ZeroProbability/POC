#!/usr/bin/dtrace -qs
syscall:::entry
/pid == $1/
{
  @num[probefunc] = count();
}
