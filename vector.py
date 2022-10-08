import math


def check_vecs(a, b):
    return check_vec(a) or check_vec(b) or len(a) != len(b)  # True = error


def check_vec(a):
    return len(a) < 2  # True = error


def add_vec(a, b, do_copy=True):
    if check_vecs(a, b):
        raise ValueError("Некорректное значение!")
    copy_a = a
    if do_copy:
        copy_a = a[:]
    for i in range(len(a)):
        copy_a[i] += b[i]
    return copy_a


def sub_vec(a, b, do_copy=True):
    copy_b = b
    if do_copy:
        copy_b = b[:]
    for i in range(len(b)):
        copy_b[i] *= -1
    return add_vec(a, copy_b)


def mul_vec(a, b):  # Скалярное произведение векторов
    if check_vecs(a, b):
        raise ValueError("Некорректное значение!")
    result = 0
    for i in range(len(a)):
        result += a[i] * b[i]
    return result


def mul_scale(a, num, do_copy=True):  # Произведение вектора на скаляр
    if check_vec(a):
        raise ValueError("Некорректное значение!")
    copy_a = a
    if do_copy:
        copy_a = a[:]
    for i in range(len(a)):
        copy_a[i] *= num
    return copy_a


def div_scale(a, num, do_copy=True):
    if check_vec(a) or num == 0:
        raise ValueError("Некорректное значение!")
    copy_a = a
    if do_copy:
        copy_a = a[:]
    for i in range(len(a)):
        copy_a[i] /= num
    return copy_a


def is_collinear(a, b):
    if check_vecs(a, b):
        raise ValueError("Некорректное значение!")
    return abs(cos_vecs(a, b)) == 1


def is_vec_dir(a, b):
    if check_vecs(a, b):
        raise ValueError("Некорректное значение!")
    return cos_vecs(a, b) == 1


def is_vec_undir(a, b):
    if check_vecs(a, b):
        raise ValueError("Некорректное значение!")
    return cos_vecs(a, b) == -1


def get_len(a):
    if check_vec(a):
        raise ValueError("Некорректное значение!")
    result = 0
    for i in range(len(a)):
        result += a[i] ** 2
    return result ** 0.5


def equal_vecs(a, b):
    if check_vecs(a, b):
        raise ValueError("Некорректное значение!")
    for i in range(len(a)):
        if a[i] != b[i]:
            return False
    return True


def equal_vecs_eps(a, b, eps):
    if check_vecs(a, b):
        raise ValueError("Некорректное значение!")
    for i in range(len(a)):
        if abs(a[i] - b[i]) >= eps:
            return False
    return True


def is_orthogonal(a, b):
    if check_vecs(a, b):
        raise ValueError("Некорректное значение!")
    return cos_vecs(a, b) == 0


def normal_vec(a, do_copy=True):
    if check_vec(a):
        raise ValueError("Некорректное значение!")
    copy_a = a
    if do_copy:
        copy_a = a[:]
    length = get_len(copy_a)
    for i in range(len(copy_a)):
        copy_a[i] /= length
    return copy_a


def change_dir(a, do_copy=True):
    if check_vec(a):
        raise ValueError("Некорректное значение!")
    copy_a = a
    if do_copy:
        copy_a = a[:]
    for i in range(len(a)):
        copy_a[i] *= -1
    return copy_a


def cos_vecs(a, b):
    if check_vecs(a, b) or get_len(a) == 0 or get_len(b) == 0:
        raise ValueError("Некорректное значение!")
    return mul_vec(a, b) / (get_len(a) * get_len(b))


def get_angle(a, b):
    if check_vecs(a, b) or get_len(a) == 0 or get_len(b) == 0:
        raise ValueError("Некорректное значение!")
    return math.acos(cos_vecs(a, b)) * 180 / math.pi  # Перевод из радиан в градусы


def proj_vec(a, b):
    if check_vecs(a, b) or get_len(b) == 0:
        raise ValueError("Некорректное значение!")
    return mul_scale(b, proj_scale(a, b) / get_len(b))


def proj_scale(a, b):
    if check_vecs(a, b) or get_len(b) == 0:
        raise ValueError("Некорректное значение!")
    return mul_vec(a, b) / get_len(b)