class ImageManager:
    def __init__(self, obj, obj_class, image_field_list = ['image']):
        self.obj = obj
        self.obj_class = obj_class
        self.image_field_list = image_field_list

    def save(self):
        obj = self.obj
        pk = obj.pk
        if pk:
            this_record = self.obj_class.objects.get(pk=pk)
            for image_field in self.image_field_list:
                this_record_image = getattr(this_record, image_field)
                image = getattr(obj, image_field)
                if this_record_image != image:
                    this_record_image.delete(save=False)

    def delete(self):
        for image_field in self.image_field_list:
            image = getattr(self.obj, image_field)
            image.delete(save=False)