# 1700 멀티탭 스케줄링
import sys
input = sys.stdin.readline
# N, K = map(int, input().split())
# usage_order = input().split()
N, K = 2, 7
usage_order = ['2', '3', '2', '3', '1', '2', '7']
def min_unplugs(num_slots, usage_order):
    plugs = []
    unplug_count = 0

    for current_index in range(len(usage_order)):
        current_device = usage_order[current_index]
        if current_device in plugs:
            continue
        
        if len(plugs) < num_slots:
            plugs.append(current_device)
            continue
        
        latest_use = -1
        device_to_unplug = -1

        for plugged_device in plugs:
            next_use = float('inf')
            for future_index in range(current_index + 1, len(usage_order)):
                if usage_order[future_index] == plugged_device:
                    next_use = future_index
                    break

            if next_use > latest_use:
                latest_use = next_use
                device_to_unplug = plugged_device

        plugs.remove(device_to_unplug)
        plugs.append(current_device)
        unplug_count += 1            
    return unplug_count

print(min_unplugs(N, usage_order))