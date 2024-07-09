# ランダムな数値リストを生成し、各数値に$numを乗じて新しいリストを作成する

import random

# $numの値を設定
num = 5

# ランダムな数値リストを生成
random_list = [random.randint(1, 100) for _ in range(100)]

# 新しいリストを作成し、各要素に$numを乗じる
multiplied_list = [x * num for x in random_list]

# リストの合計、平均、最大値、最小値を計算
total_sum = sum(multiplied_list)
average = total_sum / len(multiplied_list)
max_value = max(multiplied_list)
min_value = min(multiplied_list)

# 結果を表示
print("Original List:", random_list)
print("Multiplied List:", multiplied_list)
print("Total Sum:", total_sum)
print("Average:", average)
print("Max Value:", max_value)
print("Min Value:", min_value)

# ランダムな数値リストをソートし、上位10個の数値を取得
sorted_list = sorted(random_list, reverse=True)
top_10 = sorted_list[:10]

# 上位10個の数値に$numを乗じて新しいリストを作成
top_10_multiplied = [x * num for x in top_10]

# 結果を表示
print("Top 10 Numbers:", top_10)
print("Top 10 Multiplied:", top_10_multiplied)

# 上位10個の数値の合計、平均、最大値、最小値を計算
top_10_sum = sum(top_10_multiplied)
top_10_average = top_10_sum / len(top_10_multiplied)
top_10_max = max(top_10_multiplied)
top_10_min = min(top_10_multiplied)

# 結果を表示
print("Top 10 Total Sum:", top_10_sum)
print("Top 10 Average:", top_10_average)
print("Top 10 Max Value:", top_10_max)
print("Top 10 Min Value:", top_10_min)

# ランダムリストの各要素に$numを掛けたリストから偶数だけを抽出
even_numbers = [x for x in multiplied_list if x % 2 == 0]

# 結果を表示
print("Even Numbers:", even_numbers)

# 偶数リストの合計、平均、最大値、最小値を計算
even_sum = sum(even_numbers)
even_average = even_sum / len(even_numbers)
even_max = max(even_numbers)
even_min = min(even_numbers)

# 結果を表示
print("Even Numbers Total Sum:", even_sum)
print("Even Numbers Average:", even_average)
print("Even Numbers Max Value:", even_max)
print("Even Numbers Min Value:", even_min)

# リストから指定した数値以上の数値をフィルタリングする関数
def filter_greater_than(numbers, threshold):
    return [x for x in numbers if x > threshold]

# $numの10倍以上の数値をフィルタリング
threshold = num * 10
filtered_list = filter_greater_than(multiplied_list, threshold)

# 結果を表示
print("Filtered List (Greater than {}):".format(threshold), filtered_list)
