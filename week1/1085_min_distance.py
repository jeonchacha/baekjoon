x,y,w,h = map(int,input().split())

width = w - x
# 중앙값에서 근접한 쪽이랑 계산 (0,0) (x,y) (w,h)
min_x_distance = width if width < x else x
height = h - y
min_y_distance = height if height < y else y

print(min_x_distance)if min_x_distance < min_y_distance else print(min_y_distance)