# # Task 2
#
# Скрипт имитирующий зрительскую волну для строки.
#
# Строка ввода всегда будет в нижнем регистре, но может быть пустой.
#
# Если символ в строке является пробелом, пропустите его.
#
# ```
# # example
# wave("hello") =>
# "Hello"
# "hEllo"
# "heLlo"
# "helLo"
# "hellO"
# ```

def wave(str_: str) -> None:
    for i in range(len(str_)):
        print(f"{str_[:i]}{str_[i].upper()}{str_[i+1:]}")


if __name__ == '__main__':
    wave("hello")