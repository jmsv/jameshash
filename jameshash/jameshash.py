from __future__ import print_function


class Hash:
    """
    Hash class for containing decimal values and generating hex string
    """

    def __init__(self, dec_list):
        self.dec_list = dec_list
        self.hex_string = self.hex()

        for i in range(len(self.dec_list)):
            self.dec_list[i] %= 256

    def hex(self):
        hash_string = ""
        for i in range(len(self.dec_list)):
            self.dec_list[i] %= 256
            hash_string += hex(self.dec_list[i]).replace('L', '')[2:].zfill(2)
        return hash_string


def merge_lists(a, b):
    """
    Merge lists - e.g.,
    [1, 2, 3, 4, 5, 6] & ['a', 'b', 'c']
    => [1, 'a', 2, 'b', 3, 'c', 4, 5, 6]
    :param a: List a
    :param b: List b
    :return: Merged lists
    """
    result = []
    length = min([len(a), len(b)])
    for i in range(length):
        result.append(a[i])
        result.append(b[i])
    result += a[length:] + b[length:]
    return result


def largest_prime_factor(number):
    """
    Calculate the largest prime factor of a number
    :param number: Number of which largest prime should be found
    :return: Integer: largest prime factor
    """
    count = 2
    while count * count <= number:
        if number % count:
            count += 1
        else:
            number //= count
    return int(number)


def hash_password(password, username, blocks=32):
    """
    Main password hashing function
    :param password: Password
    :param username: Username - used for salt
    :param blocks: Number of blocks of 0xFF:
    32 blocks => 64-character hex output
    :return: Hex hash string
    """
    if not isinstance(blocks, int) or blocks > 32:
        raise ValueError("Block count value must be an integer, <= 64")
    if len(username) < 5:
        raise ValueError("Username must be at least 5 characters long")
    if len(password) < 5:
        raise ValueError("Password must be at least 5 characters long")

    padding_depth = blocks / 2 + 1

    # Pad password and username
    padded_password = password.rjust(padding_depth)
    padded_username = username.ljust(padding_depth)

    # Generate ord lists for password and salt (based on username)
    password_dec = [ord(c) for c in padded_password]
    salt_dec = [ord(c) for c in padded_username]

    # Merge password and salt lists
    ascii_dec = merge_lists(salt_dec, password_dec)

    # Initialise result list - decimal equivalent of hex hash
    # By default, length is 32
    result_dec = [1] * blocks

    # Apply hashing using mathematical operations as entropy
    for i, char in enumerate(ascii_dec * 4):
        for j in range(blocks * 4):
            # Generate entropy from seeds: char ascii, block size, counter etc.
            entropy = char * (2 ** (blocks + j + 1) + 1)
            # Prime factors calculated to make algorithm more computationally
            # expensive, and therefore harder to crack
            entropy *= largest_prime_factor(char) * (i + 1)
            entropy *= largest_prime_factor(i + j + char)
            # Increment counters
            result_dec[(i + j) % blocks] += int(entropy)

            # Modulus by 256 (has no effect in long run, but helps avoid
            # numbers that are too big to handle)
            result_dec[(i + j) % blocks] %= 256

    result_hash = Hash(result_dec)
    return result_hash.hex()


def check_password(password, username, hash_hex):
    """
    Checks password against a hash
    :param password: The password
    :param username: The username - needed for salt
    :param hash_hex: The hex hash output
    :return: True or False, where True is a match
    """
    return hash_password(password, username) == hash_hex


if __name__ == '__main__':
    print(hash_password("password", "username"))
