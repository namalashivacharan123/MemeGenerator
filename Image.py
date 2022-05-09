"""This module generates a meme by taking image and text."""

import os

from PIL import Image, ImageDraw, ImageFont


class MemeEngine:
    """
    The MemeEngine class.

    Load image.
    Crop image.
    Resize image.
    Save image.
    Create meme with image and provided text.
    """

    def __init__(self, path):
        """
        Instantiate the MemeEngine class.

        :param path: Takes the path of the folder where it can save images.
        :type path: str
        """
        self.path = path
        self.img = None
        self.img_loaded = False

    def load_img(self, img_path):
        """
        Load image.

        :param img_path: The relative or absolute path to an image
        :type img_path: str
        """
        self.img = Image.open(img_path)
        self.img_loaded = True

    def save_img(self, path):
        """
        Save Image to the given path.

        :param path: The relative path to the image. The image is saved under parent folder.
        :type path: str
        :return: Return the relative path to the image.
        """
        self.img.save(os.path.join(self.path, path))
        return os.path.join(self.path, path)

    def resize_img(self, width):
        """
        Resize the image to the given width and proportionate height.

        :param width: The width specifies the width of the image.
        :type width: int
        """
        if not self.img_loaded:
            raise Exception('Please load the image..!')

        ratio = width / float(self.img.size[0])
        height = int(ratio * float(self.img.size[1]))
        self.img = self.img.resize((width, height), Image.NEAREST)

    def crop_img(self, crop):
        """
        Crop the Image.

        :param crop: crop the image to the specified measurements. Ex: (10, 20, 15, 30)
        :type crop: tuple
        """
        if not self.img_loaded:
            raise Exception('Please load the image..!')

        self.img = self.img.crop(crop)

    def make_meme(self, in_path, out_path=None, body=None, author=None, crop=None, width=None):
        """Create a Postcard With a Text Greeting.

        :argument:
            in_path {str} -- the file location for the input image.
            out_path {str} -- the desired location for the output image.
            crop {tuple} -- The crop rectangle, as a (left, upper, right, lower)-tuple. Default=None.
            width {int} -- The pixel width value. Default=None.
        :returns:
            str -- the file path to the output image.
        """
        if in_path is not None:
            self.load_img(in_path)

        if crop is not None:
            self.crop_img(crop)

        if width is not None:
            self.resize_img(width)

        if body is not None:
            draw = ImageDraw.Draw(self.img)
            # Yagora
            font = ImageFont.truetype('Yagora.ttf', size=20)
            draw.text((10, 30), f"\"{body}\"", font=font, fill='white')
            draw.text((10, 60), f"- {author}", font=font, fill='white')

        if out_path is not None:
            out_path = self.save_img(out_path)
        else:
            out_path = self.save_img("tmp_sys_gen.jpg")
        return out_path
