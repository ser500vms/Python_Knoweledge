# Задача №27. Решение в группах
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13


sentence = """She sells sea shells on the sea shore The shells 
that she sells are sea shells I'm sure So if she sells sea 
shells on the sea shore I'm sure that the shells are sea 
shore shells """

# sentence = sentence.lower().split()

# result = {}

# for i in sentence:
#     result[i] = result.get(i, 0)

# keys = result.keys()
# print(len(keys))

# result = set()
# for i in sentence:
#     result.add(i)
# print(len(result))

# Option 2:
print(len(set(sentence.lower().split())))