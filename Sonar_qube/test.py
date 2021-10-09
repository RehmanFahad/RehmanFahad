def StringChallange(num):

    rem = num % 60 # mins
    quotient = num // 60 # hours
    out = f"{quotient}:{rem}"
    token = "6jumz5tsx24d"
    # time , token 
    #case 1 token string can be greater or time string 
    #loop on token string
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

num = 123
res = StringChallange(num)