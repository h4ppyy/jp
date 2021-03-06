import json


def scanPost(data):
    result = []
    while(True):
        x = data.find('[')
        y = data.find(']')

        if x == -1 or y == -1:
            break

        raw = data[x+1:y]

        try:
            p_raw = raw.split('@')
            hanja = p_raw[0]
            hiragana = p_raw[1]
            hangul = p_raw[2]
            x = {
              'hanja': hanja,
              'hiragana': hiragana,
              'hangul': hangul
            }
            result.append(x)
        except BaseException:
            pass

        next = data[y+1:]
        data = next
    return result


def ParsePost(data):
    print('data = ', data)
    origin = data
    while(True):
        x = data.find('[')
        y = data.find(']')

        if x == -1 or y == -1:
            break

        target = data[x:y+1]
        raw = data[x+1:y]

        try:
            p_raw = raw.split('@')
            hanja = p_raw[0]
            hiragana = p_raw[1]
            hangul = p_raw[2]
            origin = origin.replace(target, '<mark data-toggle="tooltip" data-placement="bottom" title="{1} / {2}">{0}</mark>'.format(hanja, hiragana, hangul))
        except BaseException:
            pass

        next = data[y+1:]
        data = next

    return origin


def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]
