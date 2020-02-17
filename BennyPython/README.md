# MAL

Make a Lisp implementation in Python

This is the code for my independent study on writing a LISP interpreter

The guide can be found at: https://github.com/kanaka/mal/blob/master/process/guide.md

_by Bennyr20 - Benny Rubin_

## Log:

_1/22/20_

First Log entry! Woohoo!

Forked and cloned git repository. Ready to start work on writing the LISP interpreter at step 0: REPL (read, evaluate, print).

Finished step0
along with the optional command history part.

_1/23/20_

Start work on step 1

step1 symbols work. Lists do not work at the moment.

it is 3pm and Lists now work! I spent over an hour on really stupid bugs, but that's programming for yah!

_1/27/20_

working on step 2

Got a simple calculator working! You can now pass through expressions

Finished step 2

_1/27/20_

Starting work on step 3

_2/4/20_

It has been a bit since I updated the log, but I am now starting on step 4.

I am finding that the MalTypes is getting in my way and is not being helpful, so I am going to spend some time removing that and making it easier in the future.

Finished getting rid of MalTypes. I don't think this left any bugs

_2/6/20_

working on step 4.

Just finished _do_, _if_, and _fn\*_. Just need to test the functionality then continue to core.py

Spent about an hour debugging _fn\*_. Turns out I had one small typo.... UGH programming is very annoying sometimes

Working on core

After core, doing deferrable string step which involved the deferrable from step 1.

Finished core. Now just need to test.

_2/7/20_

Working on string operations. Just about done with step 4. Also did the not function deferrable.

Finished string deferrable. Moving on to step 5.

_2/11/20_

Starting work on Tail Call optimization. Essentially turning EVAL function calls into iteration to save stack frames.

_2/15/20_

Finished Tail Call optimization. Not the hardest thing, but took a while because it was a pain to debug. Moving on to step 6.

Finished step 6

_2/16/20_

Moving onto step 7: Quoting.
