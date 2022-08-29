word = input().upper()
word_alphabet = list(set(word))

count_list = []

for i in word_alphabet:
    count = word.count(i)
    count_list.append(count)

if count_list.count(max(count_list)) > 1:
    print('?')
else: 
    max_index = count_list.index(max(count_list))
    print(word_alphabet[max_index])
