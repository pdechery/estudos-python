import re
import reprlib

RE_WORD = re.compile('\w+')

class Sentence:

    def __init__(self,text):
        self.text = text
        self.words = RE_WORD.findall(text)

    '''
    Criar este método dentro da classe se torna iterável.
    Se retirado ela não será mais.
    '''
    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)


if __name__ == '__main__':

    s = Sentence('Já raiou a madrugada e aurora clareou')

    s # doctest +ELLIPSIS (pra que serve o doctest?)

    for word in s:
        print(word)

    list(s)


          



