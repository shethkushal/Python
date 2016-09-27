Kam and Lars are planning their upcoming wedding. They'd like to make their banquet as awkward as
possible by ensuring that at each dinner table, no one knows anyone else at the table. Write a program
that computes an assignment of people to tables using as few tables as possible. Your program should
run on the command line:

python wedding.py [friends-file] [seats-per-table]

Here
* friends-file is a text file containing a friendship graph with one line per person, where each
line first lists that person's name and then the list of people that they know (and we assume that
friendships are bidirectional, i.e. if A is friends with B then B is automatically friends with A)

*seats-per-table is an integer saying the maximum number of people that can be seated at a table.
The program can output whatever you'd like, except that the last line of output should be a machine-
readable representation of the solution you found, in this format:

[table-count] [table1-person1],[table1-person2],... [table2-person1],[table2-person2],...