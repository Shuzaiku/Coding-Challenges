#15 / 15 points submission
same = {}
diff = {}
violations = int(input())

for _ in range(violations):
    pair = input().split()
    if not pair[0] in same:
        same[pair[0]] = [pair[1]]
    else:
        same[pair[0]].append(pair[1])
for _ in range(int(input())):
    pair = input().split()
    if not pair[0] in diff:
        diff[pair[0]] = [pair[1]]
    else:
        diff[pair[0]].append(pair[1])

for _ in range(int(input())):
    assigned = set(input().split())
    for member in assigned:
        s_match = same.get(member)
        d_match = diff.get(member)

        if s_match:
            for m in s_match:
                if m in assigned:
                    violations -= 1
        if d_match:
            for m in d_match:
                if m in assigned:
                    violations += 1
print(violations)
