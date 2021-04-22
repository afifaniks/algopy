from ds.dequeue import Dequeue


def is_palindrome(string):
    deq = Dequeue()

    for char in string:
        deq.add_rear(char)

    palindrome_flag = True

    while deq.size() > 1 and palindrome_flag:
        rear = deq.remove_rear()
        front = deq.remove_front()

        if rear != front:
            palindrome_flag = False

    return palindrome_flag


print(is_palindrome("madam"))
print(is_palindrome("madama"))
