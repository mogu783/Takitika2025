def Keisan(Name,Score):
    Tensu = Score
    Rate = [D[Name[a]] for a in range(4)]
    Junni = [-30,-10,10,50]
    heikin = sum(Rate) // 4
    sTensu = sorted(Tensu)
    J = []
    for a in range(4):
        I = sTensu.index(Tensu[a])
        J.append(I)
    Result = []
    Hosei = [round((heikin-a)/20) for a in Rate]
    for a in range(4):
        Result.append(round((Tensu[a]-300)/10+Junni[J[a]]+Hosei[a]))
    return Result


N = int(input()) #Total number of participants
D = dict() #key=name, value=rate
G = [] #Glade 
for _ in range(N):
    S = input() #input: name(grade):previous_rate:now_rate
    i,j = S.index("("),S.index(")")
    n = S[:i]
    G.append(S[i+1:j])
    for b in range(len(S)):
        if S[b] == ":":
            j = b
    r = int(S[j+1:])
    D[n] = int(r)
D2 = D.copy()

Q = int(input()) #Number of matches
PN = set() #Player names' set

for q in range(Q):
    Name = list(input().split()) #input: player1 player2 player3 player4 
    for n in Name:
        PN.add(n)
    Score = list(map(int,input().split())) #input: score1 score2 score3 score4
    result = Keisan(Name,Score)
    for a in range(4):
        D[Name[a]] += result[a]
    if sum(Score) == 0:
        print(str(q+1) + "番目がズレてる")    
    
#Output
i = 0
for n in D:
    if n in PN:
        print(n + "(" + G[i] + ")" + ":" + str(D2[n]) + ":" + str(D[n]))
    else:
        print(n + "(" + G[i] + ")" + ":" + str(D2[n]) + ":" + str(D2[n]))
    i += 1

#入力

#人数
#(名前 レート) * N行
#試合数
#4人の名前
#4人の点数
#上2行を試合数回繰り返す
