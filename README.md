# Mastermind

* The computer selects N different items from a pool of M items and puts them in some order. This is the secret that the user has to find in the right order.

* The user selects N different items from the pool of M items in a certain order.
* The computer gives a `*` sign for every item that is in the same location as in the secret and a `+` sign for every item that is in the secret but not in the place the user put it.
  The order of the response does NOT correspond to the order of the values.

* The last two steps are repeated until the user finds the secret and the the user wins. If the user cannot find the secret in K guesses then the user loses.

* N, M and K can be be anything. Items can be anything (eg. colors, digits, letters, etc.)
* In the original game M = 6 colors, N = 4 and K = 12 and * was a back stick and + was a white stick.

* There difficulty can be increased by allowing items to be repeated in the secret and/or by allowing empty spaces in the secret.

Let's see an example when the pool of items are the 6 digits 1-6 and that the size of the secret is 4.
The computer selects 4 values randomly:

hidden:  3654
guess 1: 1234   `*+`   (4 is in the right place, 3 is in the wrong place)
guess 2: 1256   `*+`   (5 is in the right place, 6 is in the wrong place)
guess 3: 6354   `**++` (4 and 5 in the right place, 3 and 6 in the wrong place)
guess 4: 3654   `****`  win


## Development

Setup

```
pip install pytest
```

Run tests:

```
PYTHONPATH=. pytest
```
