def StringChallange(num):
    rem = num % 60
    quotient = num // 60
    out = f"{quotient}:{rem}"
    token = "6jumz5tsx24d"
    max = len(out) if len(out) <= len(token) else len(token)
    print(max)
    final = ""
    for i in range(max):
        final += (out[i] + token[i])
    if len(out) <= len(token):
        final += token[max:]
    else:
        final += out[max:]
    return final

num = 29
res = StringChallange(num)