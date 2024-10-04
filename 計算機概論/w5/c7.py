gen_code_keys = lambda book, plain_text: ({c: str(book.find(c)) for c in plain_text})

plain_text = "no is no"
book = "Once upon a time, in a house in a land far away"
Don_Quixote = "In a village of La Mancha, the name of which I have no desire to call to mind, there lived not long since one of those gentlemen that keep a lance in the lance-rack, an old buckler, a lean hack, and a greyhound for coursing. An olla of rather more beef than mutton, a salad on most nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra on Sundays, made away with three-quarters of his income. The rest of it went in a doublet of fine cloth and velvet breeches and shoes to match for holidays, while on week-days he made a brave figure in his best homespun. He had in his house a housekeeper past forty, a niece under twenty, and a lad for the field and market-place, who used to saddle the hack as well as handle the bill-hook. The age of this gentleman of ours was bordering on fifty; he was of a hardy habit, spare, gaunt-featured, a very early riser and a great sportsman. They will have it his surname was Quixada or Quesada (for here there is some difference of opinion among the authors who write on the subject), although from reasonable conjectures it seems plain that he was called Quexana. This, however, is of but little importance to our tale; it will be enough not to stray a hair’s breadth from the truth in the telling of it."
encoder = lambda code_keys, plain_text: "".join(
    ["*" + code_keys[c] for c in plain_text]
)[1:]
encrypt = lambda book, plain_text: encoder(gen_code_keys(book, plain_text), plain_text)
gen_decode_keys = lambda book, cipher_text: {
    s: book[int(s)] for s in cipher_text.split("*")
}
thecode = "22*13*33*137*59*11*23*11*1*57*6*13*1*2*6*57*2*6*1*22*13*33*137*59*11*23*11*1*57*6*173*7*11"
key = gen_decode_keys(Don_Quixote, thecode)
for i in thecode.split("*"):
    print(key[i], end="")
