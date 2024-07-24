# キューをリストとして初期化
queue = []

# 要素1を追加
queue.append(1)
print("要素1追加後のキュー:", queue)

# 要素2を追加
queue.append(2)
print("要素2追加後のキュー:", queue)

# 先頭から要素を取得
first_element1 = queue.pop(0)
print("1回目の要素取得:", first_element1)
print("1回目の要素取得後のキュー:", queue)

# もう一度先頭から要素を取得
first_element2 = queue.pop(0)
print("2回目の要素取得:", first_element2)
print("2回目の要素取得後のキュー:", queue)

