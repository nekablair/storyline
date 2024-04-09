from rest_framework.serializers import ModelSerializer
from .models import ImageModel
import base64

def serialize_image(image):
    with image.image_data.open(mode="rb") as img_file:
        return base64.b64encode(img_file.read()).decode('ascii')

class ImageSerializer(ModelSerializer):
    class Meta:
        model = ImageModel
        fields = '__all__'



class AllImageSerializer(ModelSerializer):
    class Meta:
        model = ImageModel
        fields = '__all__'