valid_years = []
for year in range(1001, 3000):
    if year % 7 == 0 and year % 5 != 0:
        valid_years.append(year)
for i in range(0, len(valid_years), 5):
    line = valid_years[i:i+5]
    print("#".join(map(str, line)))