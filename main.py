import csv
import os

flag = False


try:
    with open("gdp.csv", "r", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=",")

        print("Усі дані з файлу gdp.csv")
        print("Country Name; 2019 [YR2019]")

        for row in reader:
            print(row["Country Name"], ";", row["2019 [YR2019]"])

except FileNotFoundError:
    print("Файл 'gdp.csv' не знайдено!")
except PermissionError:
    print("Немає доступу до файлу 'gdp.csv'!")
except Exception as e:
    print("Сталася помилка при роботі з файлом:", e)


try:
    with open("gdp.csv", "r", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=",")

        countries_input = input(
            "\nВведіть назви країн через кому,\n"
            "для яких потрібно знайти GDP per capita growth (annual %) "
            "за 2019 рік:\n"
        )

        countries = [c.strip().lower() for c in countries_input.split(",") if c.strip()]

        os.system("cls" if os.name == "nt" else "clear")

        print("Результати пошуку")
        print("Country Name; 2019 [YR2019]")

        with open("new_gdp.csv", "w", encoding="utf-8", newline="") as newfile:
            fieldnames = ["Country Name", "2019 [YR2019]"]
            writer = csv.DictWriter(newfile, fieldnames=fieldnames, delimiter=";")
            writer.writeheader()

            for row in reader:
                if row["Country Name"].lower() in countries:
                    flag = True
                    print(row["Country Name"], ";", row["2019 [YR2019]"])
                    writer.writerow({
                        "Country Name": row["Country Name"],
                        "2019 [YR2019]": row["2019 [YR2019]"]
                    })

        if not flag:
            print("Показників для вказаних країн у файлі не знайдено.")

except FileNotFoundError:
    print("Файл 'gdp.csv' не знайдено!")
except PermissionError:
    print("Немає доступу до файлу 'gdp.csv'!")
except Exception as e:
    print("Сталася помилка при роботі з файлом (пошук):", e)