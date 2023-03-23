# Trees

## Setup

Set the environment.  You only need to do this once.
```shell
$ pipenv install
```

## Run Tests

Run tests to determine when completed.

````shell
$ pipenv run pytest
================================================================== test session starts ==================================================================
platform darwin -- Python 3.10.4, pytest-7.2.2, pluggy-1.0.0
rootdir: /Users/ccheetham/src/skunkworks/trees
collected 2 items

test_display_tree.py ..                                                                                                                           [100%]

=================================================================== 2 passed in 0.01s ===================================================================

````

## Sample Output when Completed

When completed, run the `main` and you'll get the following output.

```shell
$ pipenv run python main.py
a
    b
        d
        e
            f
    c
        g
            h
        i
```
