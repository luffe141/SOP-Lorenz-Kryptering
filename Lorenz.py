K = 'abcdefg'
S = 'opqrs'

msg = input("Input message")
startK = input("Start position, K: ")
startS = input("Start position, S: ")


through_K = ''
for letter in msg:
	a=startK%len(K)
	through_K += XOR(letter, K[a])
	startK += 1

cipher = ''
for item in through_K:
	a=startS%len(S)
	cipher += XOR(item, S[a])
    if doRotate(M):
        startS += 1



























