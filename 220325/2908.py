a, b = map(str, input().split())


if a[2] > b[2]:
    case = True
elif a[2] == b[2]:
    if a[1] > b[1]:
        case = True
    elif a[1] == b[1]:
        if a[0] > b[0]:
            case = True
        else:
            case = False
    else:
        case = False
else:
    case = False

if case:
    print(a[2], a[1], a[0], sep='')
else:
    print(b[2], b[1], b[0], sep='')