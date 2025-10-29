import zipfile
import re

zip_path = 'voina-i-mir.zip'
target_filename = None#ищем первый файл внутри архива

with zipfile.ZipFile(zip_path, 'r') as zf:
    for name in zf.namelist():
        if name.endswith('.txt'):
            target_filename = name
            break
    if target_filename is None:
        print("Текстовый файл в архиве не найден.")
        exit()
    with zf.open(target_filename) as file:
        content_bytes = file.read()

text = content_bytes.decode('utf-8')
letters = re.findall(r'[A-Za-zА-Яа-яЁё]', text)
freq = {}
total_letters = len(letters)
for ch in letters:
    freq[ch] = freq.get(ch, 0) + 1
sorted_freq = sorted(freq.items(), key=lambda item: item[1], reverse=True)
with open('result.txt', 'w', encoding='utf-8') as f:
    for letter, count in sorted_freq:
        ratio = count / total_letters
        f.write(f'{letter} {ratio:.8f}\n')