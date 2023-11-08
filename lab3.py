def first():
    F1 = open("F1.txt", "w", encoding="utf8")
    while True:
        line = input("Введите строку: ")
        if not line:
            break
    F1.write(line + "\n")
    F1.close()
    F1 = open("F1.txt", "r", encoding="utf8")
    F2 = open("F2.txt", "w", encoding="utf8")
    for line in F1:
        words = line.strip().split()
        if len(words) == 1:
            F2.write(line)
    F1.close()
    F2.close()
    long = ""
    F2 = open("F2.txt", "r", encoding="utf8")
    for line in F2:
        word = line.strip()
        if len(words) > len(long):
            long = word
    F2.close()
    if long:
        print(f"Самое длинное слово в файле F2: {long}")
    else:
        print("В файле F2 нет строк с одним словом")


def second():
    File = open("Кинотеатр.txt", "r", encoding="utf8")
    line = File.readlines()
    date = input("Введите дату(формат дд.мм.гггг): ")
    popular = ""
    max = 0
    for l in line:
        info = l.strip().split()
        if info[-3] == date:
            print(l)
        visits = int(info[-1])
        if visits > max:
            max = visits
            popular = " ".join(info[:-1])
    if popular:
        print(f"Самый посещаемый фильм: {popular}, количество зрителей: {max}")
    else:
        print("Нет данных о фильмах на эту дату")
def third():
    file = open("Расписание.txt", "r", encoding="utf8")
    line = file.readlines()
    subjects={}
    for l in line:
        parts = l.split(":")
        subject = parts[0].strip()
        info = parts[1].strip()
        lesson_info = info.split()
        total=0
        for item in lesson_info:
            if item.endswith("(л)"):
                total += int(item[:-3])
            elif item.endswith("(пр)"):
                total += int(item[:-4])
            elif item.endswith("(лаб)"):
                total += int(item[:-5])
        subjects[subject]=total
    print(subjects)
print(third())
