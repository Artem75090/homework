import string


class WordsFinder():
    def __init__(self, *args):
        self.args = args

    def get_all_words(self):
        all_words = {}
        for i in self.args:
            with open(i, "r", encoding="utf-8") as file:
                text = file.read()
            text = text.replace("\n", " ")
            text_without_signs = text.translate(str.maketrans("", "", string.punctuation.replace("'", "")))
            text_without_signs = text_without_signs.lower().split(' ')
            all_words[i] = text_without_signs
        return all_words

    def find(self, word):
        dict_result = {}
        for i, j in self.get_all_words().items():
            for k in range(len(j)):
                if j[k] == word.lower():
                    dict_result[i] = k + 1
                    break
        return dict_result

    def count(self, word):
        dict_result = {}
        for i, j in self.get_all_words().items():
            counter = 0
            for k in range(len(j)):
                if j[k] == word.lower():
                    counter +=1
            dict_result[i] = counter
        return dict_result


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))

















#     def qwe(self):
#         for i in self.args:
#             print(i)
#
#
# qw = WordsFinder(123, 234, 345)
#
# qw.qwe()

