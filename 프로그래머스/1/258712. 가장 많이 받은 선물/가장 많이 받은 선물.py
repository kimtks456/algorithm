def solution(friends, gifts):
	n = len(friends)
    
	# 친구명 별 index
	idx = {name: i for i, name in enumerate(friends)}
	print(idx)

	# 친구 별 선물지수
	gift_idx = [0] * n
	
	# 친구별 선물 관계(행: give, 열: take)
	given = [[0] * n for _ in range(n)]
	for gift in gifts:
		giver, taker = map(idx.get, gift.split(' '))
		given[giver][taker] += 1
		# 선물지수 = 준 개수 - 받은 개수
		gift_idx[giver] += 1
		gift_idx[taker] -= 1

	# 다음달 선물 가장많이 받는 개수 count
	answer = 0
	for i in range(n):
		temp = 0 # 현재 친구가 받을 선물 수
		for j in range(n):
			if i == j: continue
            # 더 많이 줬다면, 받아야함
			if given[i][j] > given[j][i]:
				temp += 1
			elif given[i][j] == given[j][i]:
				if gift_idx[i] > gift_idx[j]:
					# 동일하게 주고받고, 선물지수 더 높다면, 받아야함
					temp += 1
		answer = max(answer, temp)

	return answer