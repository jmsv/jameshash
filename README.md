# jameshash
bad hashing thing

```
>>> import jameshash
>>> jameshash.hash_password("correct horse battery staple", "a username")
'b3552dbd11ed73decb87fd157da1a35d6b98e5a3350d03036799f1bdd747ab7f'
```

Originally written as part of an operating systems and security module at university, given the task of writing a salted hash function.

__Please don't assume this is secure__, using hashing functions that aren't considered 'tried and tested' is always a bad idea; and this one is particularly awful. (I accept no liability for cracked passwords bla bla bla)

If you ended up here and can tell me why this hashing function is awful, let me know in the [issues](https://github.com/jmsv/jameshash/issues). While I'm sure it's awful, I have no way of proving it, so an explanation would help me learn stuff.

## Install

- `git clone https://github.com/jmsv/jameshash.git`
- `cd jameshash`
- `python setup.py install` (or `make install`)

## Use

- `hash_password` takes the password and the username, and returns the resultant hex string hash
- `check_password` takes the password, username and hash and returns `True` if the generated and expected hashes match

## Test

`python tests.py` (or `make test`)

## Contributing

Any suggestions / issues / pull requests are welcome.
