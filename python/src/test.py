import sys
import re

input_line = input()
input_list = [int(num) for num in input_line.split()]

input_size = len(input_list)
if input_size != 2:
	print("エラー")
	sys.exit()

row_list = []
point_list = []
pattern = r'\.'
for i in range(input_list[0]):
	row = input()
	if(len(row) != input_list[1]):
		print("エラー 文字列の数が指定の長さと違う")
		sys.exit()
	row_list.append(row)
	matches = [match.start() for match in re.finditer(pattern, row)]
	point_list.append(matches)

donuts_cont = 0
length_point_list = len(point_list)
for i in range(length_point_list):
	if not point_list[i] or i == 0 or i == length_point_list - 1:
		continue;
	points = point_list[i]
	for point in points:
		down_point = point - 1
		up_point = point + 1
		if(down_point in points or up_point in points):
			continue
		up_row = row_list[i - 1]
		down_row = row_list[i + 1]
		if(up_row[down_point] == "." or up_row[point] == "." or up_row[up_point] == "."):
			continue
		if(down_row[down_point] == "." or down_row[point] == "." or down_row[up_point] == "."):
			continue
		donuts_cont += 1

print(donuts_cont)