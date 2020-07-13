# Print out each element of the following array on a separate line:
a = ["Joe", "2", "Ted", "4.98", "14", "Sam",
     "void *", "42", "float", "pointers", "5006"]
# You may use whatever programming language you'd like.
# Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process.

for item in a:
    print(item)


Print out each element of the following array on a separate line, but this time the input array can contain arrays nested to an arbitrarily deep level:
a = ['Bob', 'Slack', ['reddit', '89', 101, ['alacritty', '(brackets)', 5, 375]], 0, [
    '{slice, owned}'], 22]
For the above input, the expected output is:
Bob
Slack
reddit
89
101
alacritty
(brackets)
5
375
0
{slice, owned}
22
You may use whatever programming language you'd like.
Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process.


result = []

for item in a:
