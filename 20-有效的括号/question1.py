import time


def func(str: str) -> bool:
    strack = list()
    for i in str:
        if (i == '{') or (i == '[') or (i == '('):
            strack.append(i)
            continue
        else:
            if strack is not None:
                if strack[-1] == '{' and i == '}':
                    strack.pop()
                elif strack[-1] == '[' and i == ']':
                    strack.pop()
                elif strack[-1] == '(' and i == ')':
                    strack.pop()
                else:
                    return False
            elif strack is not None:
                return False
            else:
                return False
    return True


if __name__ == '__main__':
    start = time.clock()
    str = "{{[]}()[]{}}"
    # str = "{{)}}"
    print(func(str))
    stop = time.clock()
    print(f"用时:", stop - start)
