def validate_file_extension(value):
    import os

    from django.core.exceptions import ValidationError
    extension = os.path.splitext(value.name)[1]
    valid_extensions = ['.jpg', '.png']
    if not extension.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension!')