from functools import wraps

TOTAL_RATE = 2

FUNC_SCOPE = ['test', 'test1']


def rate_count(func):
    func_num = {
        # 需要注意函数名不能重复
        func.__name__: 0
    }

    @wraps(func)
    def wrapper():
        if func.__name__ in FUNC_SCOPE:
            if func_num[func.__name__] >= TOTAL_RATE:
                raise Exception(f"{func.__name__}函数调用超过设定次数")
            result = func()
            func_num[func.__name__] += 1
            print(f" 函数 {func.__name__} 调用次数为： {func_num[func.__name__]}")
            return result
        else:
            # 不在计数限制的函数不受限制
            return func()

    return wrapper


@rate_count
def test1():
    pass


@rate_count
def test2():
    print("test2")
    pass


if __name__ == "__main__":
    try:
        test2()
        test2()
        test1()
        test1()
        test1()
    except Exception as e:
        print(e)
    test2()
    test2()


