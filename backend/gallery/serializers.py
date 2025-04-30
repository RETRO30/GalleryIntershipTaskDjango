import base64
import imghdr
from rest_framework import serializers
from gallery.models import Image

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'image_base64', 'description']

    def validate_image_base64(self, value):
        """
        Проверяет и дополняет base64 строку.
        """
        try:
            # Отделяем префикс, если он есть
            has_prefix = ',' in value
            header, data = value.split(',', 1) if has_prefix else (None, value)

            # Декодируем base64
            decoded_file = base64.b64decode(data)
        except Exception:
            raise serializers.ValidationError("Incorrect base64 string")

        # Определяем тип картинки
        file_type = imghdr.what(None, h=decoded_file)
        if file_type not in ['jpeg', 'png', 'gif', 'bmp', 'webp']:
            raise serializers.ValidationError("File is not image")

        # Если префикса не было — добавим его
        if not has_prefix:
            mime_type = f"image/{'jpeg' if file_type == 'jpg' else file_type}"
            value = f"data:{mime_type};base64,{data}"

        return value