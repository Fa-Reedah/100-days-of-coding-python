# Treasure Map
row1 = ["✅", "✅", "✅"]
row2 = ["✅", "✅", "✅"]
row3 = ["✅", "✅", "✅"]

map_ = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure (e.g 23 [col 2, row 3])? ")
col = int(position[0])
row = int(position[1])

col_select = map_[col - 1]
row_select = col_select[row - 1] = "❌"

print(f"{row1}\n{row2}\n{row3}")
