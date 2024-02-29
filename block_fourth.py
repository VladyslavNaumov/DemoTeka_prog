import os

def find_pdf_by_name(folder_path, list_name):
    # Формуємо шаблон назви файлу з врахуванням назви списку
    pdf_name_template = f"{list_name}.pdf"

    # Пошук PDF-файлу у вказаній папці
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower() == pdf_name_template.lower():
                # Повертаємо повний шлях до знайденого PDF-файлу
                return os.path.join(root, file)

    # Якщо файл не знайдено, повертаємо порожню строку
    return ""

# Вказуємо шлях до папки, де потрібно шукати PDF-файли
pdf_folder_path = "шлях_до_папки_з_PDF"

# Припустимо, що list_name містить назву списку з третього блоку
list_name = "назва_списку"

# Пошук PDF-файлу за назвою списку
pdf_file_path = find_pdf_by_name(pdf_folder_path, list_name)

# Виведення результату
if pdf_file_path:
    print("PDF-файл знайдено:", pdf_file_path)
else:
    print("PDF-файл не знайдено.")