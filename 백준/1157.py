s = list(input().upper())
dic = {}
for index, values in enumerate(s):
    if values in dic:
        dic[values] += 1
    else:
        dic[values] = 1

a = list(dic.values())
m = max(a)

if a.count(m) >= 2:
    print('?')
else:
    for key, values in dic.items():
        if m == values:
            print(key)



# 출처 https://parkgihyeon.github.io/boj/boj1157/

# s = input().upper() # 단어 입력
# word_list = list(set(s)) # 단어에서 중복 알파벳 제거하고 리스트에 하나씩만 삽입
# count_list = [s.count(i) for i in word_list] # 각 알파벳이 단어(단어리스트)에서 몇 개씩 있는지 카운트

# if count_list.count(max(count_list)) > 1: # 가장 큰 횟수가 또 있는지(동일한 횟수) 확인
#     print('?')
# else:
#     print(word_list[count_list.index(max(count_list))])
