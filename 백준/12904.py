if __name__=="__main__":
    S = input()
    T = input()
    while len(S)!=len(T):
        if T.strip()[-1]=='B':
            T=T[:len(T)-1]
            T=T[::-1]
        elif T.strip()[-1]=='A':
            T=T[:len(T)-1]
    if T==S:
        print(1)
    else:
        print(0)
