import sys

width, height = map(int,sys.stdin.readline().strip().split())
cut_count = int(sys.stdin.readline().strip())
cut_info = []
for i in range(cut_count):
    cut_info.append(sys.stdin.readline().strip().split())
cut_info_int = [list(map(int, pair)) for pair in cut_info]
wid_list = [0, height]
hei_list = [0, width]
for i in range(len(cut_info_int)):
    if cut_info_int[i][0] == 0:
        wid_list.append(cut_info_int[i][1])
    else:
        hei_list.append(cut_info_int[i][1])

wid_list_sorted = sorted(wid_list)
hei_list_sorted = sorted(hei_list)

wid_prev = 0
max_wid = 0
for i in wid_list_sorted:
    calc = i - wid_prev
    if max_wid < calc:
        max_wid = calc
    wid_prev = i

hei_prev = 0
max_hei = 0
for i in hei_list_sorted:
    calc = i - hei_prev
    if max_hei < calc:
        max_hei = calc
    hei_prev = i

ans = max_wid * max_hei
print(ans)