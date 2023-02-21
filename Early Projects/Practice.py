from string import ascii_uppercase

d = {ascii_uppercase[i-1]:i for i in range(1,27)}
d_two = {i:ascii_uppercase[i-1] for i in range(1,27)}
d_two[0] = ""

def incs(text):
    number_list = [0, 0, 0, 0]
    output = ""
    try:
        y =3
        for i in reversed(range(len(text))):
            number_list[y] += d[text[i]]
            y -=1
        for i in range(1,5):
            if (number_list[-i])+1 == 27:
                number_list[-i] = 1
            else:
                (number_list[-i]) += 1
                break
        for n in number_list:
            output += d_two[n]
        return output
    except (KeyError, ValueError):
        return "EH ERRRR"
    except:
        return 0