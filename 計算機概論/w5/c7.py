from base64 import decode


gen_code_keys = (lambda book, plain_text:({c: str(book.find(c)) for c in plain_text}))
plain_text = 'no is no'
Don_Quixote = 'In a village of La Mancha, the name of which I have no desire to call to mind, there lived not long since one of those gentlemen that keep a lance in the lance-rack, an old buckler, a lean hack, and a greyhound for coursing.'
print(gen_code_keys(Don_Quixote, plain_text))

encoder = (lambda code_keys, plain_text:
    ''.join(['*' + code_keys[c] for c in plain_text])[1:])

encrypt = (lambda book, plain_text:
    encoder(gen_code_keys(book, plain_text), plain_text))





print(encrypt(Don_Quixote, 'no is no'))
    
gen_decode_keys = (lambda book, cipher_text:
    {s: book[int(s)] for s in cipher_text.split('*')})

print(gen_decode_keys(Don_Quixote, encrypt(Don_Quixote, 'no is no')))



