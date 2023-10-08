# Примеры использования библиотеки shutil
import shutil

## 1. Копирование файла из одного места в другое
src_path = "..\lesson_8\labClassSpecAttr.ipynb"
dst_path = "..\\"

shutil.copy(src_path, dst_path)

## 2. Копирование директории со всем содержимым:
src_path = "..\homework_4"
dst_path = "..\homework_3\dir"

shutil.copytree(src_path, dst_path)

## 3.  Перемещение файла из одного места в другое
src_path = "..\lesson_8\labClassSpecAttr.ipynb"
dst_path = "..\\"

shutil.move(src_path, dst_path)

## 4.  Создание архива из директории:
src_path = "..\lesson_2"
dst_path = "..\lesson2"

shutil.make_archive(dst_path, 'zip', src_path)

## 5.  Распаковка архива
src_path = "..\lesson2.zip"
dst_path = "..\lesson_2_zip"

shutil.unpack_archive(src_path, dst_path)