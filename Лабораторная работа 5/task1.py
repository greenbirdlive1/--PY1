from pprint import pprint

diction_ = [{"bin": bin(x), "dec": x, "hex": hex(x), "oct": oct(x)} for x in range(0, 16)]

pprint(diction_)


