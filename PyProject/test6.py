from PIL import Image

def crop_image(input_image_path, output_image_path):
    image = Image.open(input_image_path)
    # Создаем список пикселей, содержащий непрозрачные пиксели
    transparent = Image.new('RGBA', image.size, (0, 0, 0, 0))
    transparent.paste(image, (0, 0), mask=image)
    
    # Находим левую, правую, верхнюю и нижнюю границы непрозрачных пикселей
    left, top, right, bottom = image.width, image.height, 0, 0
    for x in range(image.width):
        for y in range(image.height):
            pixel = transparent.getpixel((x, y))
            if pixel[3] != 0:  # Если пиксель непрозрачный
                left = min(left, x)
                top = min(top, y)
                right = max(right, x)
                bottom = max(bottom, y)
    
    # Обрезаем изображение по найденным границам
    cropped_image = image.crop((left, top, right, bottom))
    
    # Сохраняем обрезанное изображение
    cropped_image.save(output_image_path)

if __name__ == '__main__':
    input_path = 'PyProject\\vizitka.png'  # Путь к исходному файлу
    output_path = 'output.png'  # Путь к выходному файлу
    crop_image(input_path, output_path)
    print("Изображение успешно обрезано.")
