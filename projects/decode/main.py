def encode(st):
    t = ['a', 'e', 'i', 'o', 'u']
    n = ['1', '2', '3', '4', '5']

    for char in range(len(t)):
        st = st.replace(t[char], n[char])
        char += 1
    return st


print(encode('This is an encoding test.'))


def decode(st):
    t = ['a', 'e', 'i', 'o', 'u']
    n = ['1', '2', '3', '4', '5']

    for char in range(len(t)):
        st = st.replace(n[char], t[char])
        char += 1

    return st


print(decode('Th3s 3s 1n 2nc4d3ng t2st.'))
