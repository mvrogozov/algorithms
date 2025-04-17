def read_input():
	l = int(input())
	n = list(map(int, input().strip().split()))
	k = int(input())
	return l,n,k

def s_avg(l,n,k):
	result = []
	cur_sum = sum(n[0:k])
	result.append(cur_sum/k)
	for i in range(l - k):
		cur_sum -= n[i]
		cur_sum += n[i+k]
		result.append(cur_sum/k)
	return result

l,n,k = read_input()

print('---')
print(' '.join(map(str, s_avg(l,n,k))))