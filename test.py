def times_ten_file(source, target):
    with open(source, "r", encoding="utf8") as source:
        source_lines = source.readlines()

    with open(target, "w", encoding="utf8") as target:
        target.writelines(source_lines)

        source_lines.pop(0)

        for _ in range(9):
            target.writelines(source_lines)


times_ten_file("searchTermsTimesTen.csv", "searchTermsTimes100.csv")
