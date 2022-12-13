# Mastermind

* The computer select N different items from a pool of M items and puts them in some order. This is the secret that the user has to find in the right order.

* The user selects N different items from the pool of M items in a certain order.
* The cumputer gives a * sign for every item that is in the same location as  in the secret and a + sign for every item that is in the secret but not in the place the user put it.

* The last two steps are repeated until the user finds the secret and the the user wins. If the user cannot find the secret in K guesses then the user loses.

* N, M and K can be be anything. Items can be anything (eg. colors, digits, letters, etc.)
* In the original game M = 6 colors, N = 4 and K = 12 and * was a back stick and + was a white stick.

* There difficulty can be increased by allowing items to be repated in the secret and/or by allowing empty spaces in the secret.


## Development

Setup

```
pip install pytest
```

Run tests:

```
PYTHONPATH=. pytest
```
