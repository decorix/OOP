from PIL import Image, ImageDraw

class ImageMixer:
    def create_table_image(self, images, size, sequence, rows, columns, show_grid, grid_color):
        result_image = Image.new('RGB', size)
        image_width, image_height = size[0] // columns, size[1] // rows
        
        for i in range(rows):
            for j in range(columns):
                image_index = int(sequence[(i * columns + j) % len(sequence)]) - 1
                current_image = images[image_index].resize((image_width, image_height))
                result_image.paste(current_image, (j * image_width, i * image_height))
                
                if show_grid:
                    self.draw_grid(result_image, image_width, image_height, i, j, grid_color)
        
        result_image.show()

    def create_zebra_image(self, images, size, sequence, stripes, show_grid, grid_color, stripe_type):
        result_image = Image.new('RGB', size)
        image_width, image_height = size[0], size[1] // stripes
        
        for i in range(stripes):
            image_index = int(sequence[i % len(sequence)]) - 1
            current_image = images[image_index].resize((image_width, image_height))
            result_image.paste(current_image, (0, i * image_height))
            
            if show_grid:
                self.draw_grid(result_image, image_width, image_height, i, 0, grid_color, stripe_type)
        
        result_image.show()
    
    def draw_grid(self, image, width, height, row, column, color, stripe_type=None):
        draw = ImageDraw.Draw(image)
        
        if stripe_type == 'horizontal':
            draw.rectangle([(0, row * height), (width, row * height + 1)], fill=color)
        elif stripe_type == 'vertical':
            draw.rectangle([(column * width, 0), (column * width + 1, height)], fill=color)
        else:
            draw.rectangle([(0, row * height), (width, row * height + 1)], fill=color)
            draw.rectangle([(column * width, 0), (column * width + 1, height)], fill=color)
            

# Example usage
mixer = ImageMixer()

images = [Image.open('C:\\Users\\User\\Desktop\\4sem\\OOP\\Lesson_10\\image1.png'), Image.open('C:\\Users\\User\\Desktop\\4sem\\OOP\\Lesson_10\\image2.png'), Image.open('C:\\Users\\User\\Desktop\\4sem\\OOP\\Lesson_10\\image3.png')]

# Creating table image
mixer.create_table_image(images, (800, 600), '123', 2, 2, True, 'black')

# Creating zebra image
mixer.create_zebra_image(images, (800, 600), '12', 4, True, 'black', 'vertical')
