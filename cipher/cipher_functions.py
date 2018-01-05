# Functions for running an encryption or decryption algorithm

ENCRYPT = 'e'
DECRYPT = 'd'

# Write your functions after this comment.  Do not change the statements above
# this comment.  Do not use import, open, input or print statements in the
# code that you submit.  Do not use break or continue statements.


def clean_message(letters):
    """(str) -> str

    Precondition: the input message only consist of 26 English alphabetical
    characters.

    Return a copy of the message of input. The return message should only be
    consisted of 26 English alphabetical characters in
    uppercase(Without blank and symbol).

    >>> clean_message('how are you?')
    'HOWAREYOU'
    >>> clean_message('Nopqrstuvw')
    'NOPQRSTUVW'
    """
    uppercase_letter = ''
    for char in letters:
        # Transfer input letters into uppercase
        if char.isalpha():
            uppercase_letter = uppercase_letter + char.upper()
    return uppercase_letter


def encrypt_letter(letter, keystream_value):
    """(str, int) -> str

    Precondition: the first parameter(letter) input should be a single
    English letter and the second parameter input should be a number.
    the function just need to work for the 26 character of English alphabet.

    Return the result encrypted after applying the keystream value on
    the letter.

    >>> encrypt_letter('A', 2)
    'C'
    >>> encrypt_letter('B', 3)
    'E'
    """
    # Transfer letters into ASCII number. Then add keystream value to it.
    num = ord(letter) + keystream_value


    if num <= 90:
        return chr(num)
    else:
        return chr(num - 26)


def decrypt_letter(letter, key_stream_value):

    """(str, int) -> str

    Precondition: the first parameter(letter) input should be a
    single uppercase letter and the second parameter input should be a number.
    the function just need to work for the 26 character English alphabet.

    Return the result decrypted after applying the keystream value on
    the letter.

    >>> decrypt_letter('A', 1)
    'Z'
    >>> decrypt_letter('B', 2)
    'Z'
    """
    # Create a list representing alphabet.
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    letter_convert = alphabet.index(letter)
    number_after_decrypt = letter_convert - key_stream_value
    number_after_decrypt_real = number_after_decrypt - 26 * (number_after_decrypt // 26)
    return alphabet[number_after_decrypt_real]


def swap_cards(deck, index):
    """(list of int, int) -> NoneType

    Precondition: the input deck is a valid deck and index is a number.

    Swap the card at the index with the card that follows it.
    Treat the deck as circular: if the card at the index is on the
    bottom of the deck, swap that card with the top card.

    >>> deck = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15, 18, 21, \
    24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>> swap_cards(deck, 2)

    >>> deck = [ 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26, 1, 4, 7, 10, \
    13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15]
    >>> swap_cards(deck, 27)

    """
    # a is used for storing characters
    if index == len(deck) - 1:
        a = deck[-1]
        deck[-1] = deck[0]
        deck[0] = a
    # b is used for storing characters.
    else:
        b = deck[index]
        next_index = index + 1
        deck[index] = deck[next_index]
        deck[next_index] = b

def get_small_joker_value(deck):
    """(list of int) -> int

    Precondition: the input deck is a valid deck.

    Return the value of the small joker (value of the second highest card) for
    the given deck of cards.

    >>> deck = [ 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26, 1, 4, 7, 10, \
    13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15]
    >>> get_small_joker_value(deck)
    27
    >>> deck = [1, 2, 3, 4, 5]
    >>> get_small_joker_value(deck)
    4
    """
    small_joker_value = max(deck) - 1
    return small_joker_value

def get_big_joker_value(deck):
    """(list of int) -> int

    Precondition: the input deck is a valid deck.

    Return the value of the big joker (value of the highest card) for the
    given deck of cards.

    >>> deck = [ 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26, 1, 4, 7, 10, \
    13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15]
    >>> get_big_joker_value(deck)
    28
    >>> deck = [1, 2, 3, 4, 5]
    >>> get_big_joker_value(deck)
    5
    """

    return max(deck)


def move_small_joker(deck):
    """(list of int) -> NoneType

    Precondition: the input deck is a valid deck.

    Swap the small joker with the card after it. Treat the deck as circular.


    >>> deck = [ 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26, 1, 4, 7, 10, \
    13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15]
    >>> move_small_joker(deck)

    >>> deck = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15, 18, 21, \
    24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>> move_small_joker(deck)

    """

    small_joker_value = max(deck)-1
    swap_cards(deck, deck.index(small_joker_value))


def move_big_joker(deck):
    """(list of int) -> NoneType

    Precondition: the input deck is a valid deck.

    Move the big joker two cards down the deck. Treat the deck as circular.

    >>> deck = [ 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26, 1, 4, 7, 10, \
    13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15]
    >>> move_big_joker(deck)

    >>> deck = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15, 18, 21, \
    24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>> move_big_joker(deck)

    """

    big_joker_value = max(deck)
    # Swap the big joker twice.
    swap_cards(deck, deck.index(big_joker_value))
    swap_cards(deck, deck.index(big_joker_value))

def triple_cut(deck):

    """(list of int) -> NoneType

    Precondition: the input parameter is a valid deck.

    Every cards above the first joker goes to bottom of the deck.
    Every cards below the second joker goes to top of the deck.

    >>> deck = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15, 18, 21, \
    24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>> triple_cut(deck)

    >>> deck = [ 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26, 1, 4, 7, 10, \
    13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15]
    >>> triple_cut(deck)

    """

    s_joker_number = deck.index(get_small_joker_value(deck))
    b_joker_number = deck.index(get_big_joker_value(deck))

    # Choose the smaller joker as the first joker.
    first_joker_number = min(s_joker_number,  b_joker_number)

    # Choose the larger joker as the second joker.
    second_joker_number = max(s_joker_number, b_joker_number)

    # Slice the part before the first joker.
    first_part_deck = deck[:first_joker_number]

    # Slice the part between the first joker and the second joker.
    second_part_deck = deck[first_joker_number:second_joker_number+1]

    # Slice the part after the second joker.
    third_part_deck = deck[second_joker_number+1:]

    # Create a new deck following the expected order.
    new_deck = third_part_deck + second_part_deck + first_part_deck

    # Transfer elements in new deck back to the original deck.
    for i in range(0, len(new_deck)):
        deck[i] = new_deck[i]





def insert_top_to_bottom(deck):

    """(list of int) -> NoneType

    Precondition: The input parameter deck is a valid deck.

    Get the value of the last element in the deck,
    insert that many of cards before the last card.
    Special case: if the bottom card is the big joker,
    use the value of the small joker as the number of cards.

    >>> deck = [ 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26, 1, 4, 7, 10, \
    13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15]
    >>> insert_top_to_bottom(deck)

    >>> deck = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15, 18, 21, \
    24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>> insert_top_to_bottom(deck)

    """

    # Assume the number in the deck start from 1.
    # If the last number in the deck is big joker, denote actual value of
    # last card as n, use the number of small joker to replace that,
    # denote the value of last card as n-1.
    # Therefore we need to put first n-1 cards before the nth card,
    # which let the order of cards in the deck remains the same.
    # Pass this process.
    last_num = deck[-1]
    if last_num == max(deck):
        pass

    # If the last number is not the big joker.
    else:
        sliced_part = deck[:last_num]
        deck.remove(last_num)
        for element in sliced_part:
            deck.remove(element)
        for i in sliced_part:
            deck.append(i)
        deck.append(last_num)




def get_card_at_top_index(deck):
    """(list of int) -> int

    Precondition: The input parameter deck is a valid deck.

    Using the value of the top card as an index, return the card in the deck at
    that index. Special case: if the top card is the big joker,
    use the value of the small joker as the index.

    >>> deck = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15, 18, 21, \
    24, 27, 2, 5, 8, 11, 14, 17, 29, 23, 26]
    >>> get_card_at_top_index(deck)
    4
    >>> deck = [ 19, 25, 1, 4, 7, 10, 13, 16,22, 28, 3, 6, 9, 12, 15, 18, 21, \
    24, 27, 2, 5, 8, 11, 14, 17, 29, 23, 26]
    >>> get_card_at_top_index(deck)
    2
    """

    top_index = deck[0]
    # If the top card is the big joker, use the value of the small
    # Joker as the index.
    if top_index == get_big_joker_value(deck):
        target_card = deck[get_small_joker_value(deck)]
    else:
        target_card = deck[top_index]
    return target_card


def get_next_keystream_value(deck):
    """(list of int) -> int

    Precondition: The input parameter deck is a valid deck.

    Return a valid keystream value by repeating all five steps of the algorithm.

    >>> deck = [6,2,3,4,1,5]
    >>> get_next_keystream_value(deck)
    3
    >>> deck = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, \
    9, 12, 15, 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>> get_next_keystream_value(deck)
    11
    """
    move_small_joker(deck)
    move_big_joker(deck)
    triple_cut(deck)
    insert_top_to_bottom(deck)
    keystream_value = get_card_at_top_index(deck)

    # Repeat all the steps until a valid kystream value is found.
    while keystream_value >= max(deck) - 1:
        move_small_joker(deck)
        move_big_joker(deck)
        triple_cut(deck)
        insert_top_to_bottom(deck)
        keystream_value = get_card_at_top_index(deck)

    return keystream_value


def process_messages(deck, message, way_of_processing):
    """(list of int, list of str, str) -> list of str

    Precondition: input of way_of_processing is only consist of 'e' or 'd'.

    Return a list of message by using function 'encrypt_letter' or
    'decrypt_letter' to encrypt or decrypt given message.
    The way of processing message determined by the third parameter,
    way_of_processing.

    >>> deck = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15, 18, 21, \
    24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>> message = ['THISISITTHEMASTERSWORD','NOTHISCANTBEITTOOBAD']
    >>> process_messages(deck, message, 'e')
    ['EQFZSRTEAPNXLSRJAMNGAT', 'GLCEGMOTMTRWKHAMGNME']

    >>> deck = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15, 18, 21, \
    24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>> message = ['SXRZDNYHLPJGPANWXVCWV']
    >>> process_messages(deck, message, 'd')
    ['HOUSTONWEHAVEAPROBLEM']
    """

    message_after_process = []
    # Consider the case of encrypt
    if way_of_processing == 'e':
        for line in message:
            line = clean_message(line)
            new_line = ''
            for element in line:
                new_line += encrypt_letter(element, get_next_keystream_value(deck))
            message_after_process.append(new_line)
    # Consider the case of decrypt
    else:
        # Since the message that needs to be decrypted is already in uppercase
        # and without blank and symbol, we don't need to clean_message anymore.
        for line in message:
            new_line = ''
            for element in line:
                new_line += decrypt_letter(element, get_next_keystream_value(deck))
            message_after_process.append(new_line)

    return message_after_process





def read_messages(msg_file):

    """(file open for reading) -> list of str

    Precondition: The parameter msg_file should be a message file that is
    already open for reading and that file contains one message per line.

    Read and return the contents of the file as a list of messages. The returned
    message should strip the newline from each line,
    and in order in which they appear in the file.
    """

    new_message = []
    for line in msg_file:
        new_message.append(line.strip())
        # Since The returned message should strip the newline from each line.
    return new_message




def is_valid_deck(deck):
    """(list of int) -> bool

    Precondition: the length of input list is a list of number.

    Return true iff the input deck is a valid deck of cards,
    which means number of cards in the deck is consecutive.
    Return false if the input deck is not a valid deck of cards.

    >>> deck = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15, 18, 21, \
    24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>> is_valid_deck(deck)
    True
    >>> deck = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15, 18, 21, \
    24, 27, 2, 5, 8, 11, 14, 17, 29, 23, 26]
    >>> is_valid_deck(deck)
    False
    """

    for i in range(len(deck)):
        if not (i + 1) in deck:
            # Since the index for ith term is i + 1
            return False

    return True


def read_deck(deck_file):
    """(file open for reading) -> list of int

    Precondition: the file open for reading has to be in the same files with
    cipher_functions.py.
    The parameter deck_file refers to a deck file is already open for reading.

    Read and return the numbers that are in the file,
    with the same order that they are shown in the file.
    """

    deck = []
    for line in deck_file:
        for i in line.split():
            deck.append(int(i))
    return deck
