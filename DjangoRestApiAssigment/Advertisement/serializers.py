from rest_framework import serializers, status
from .models import Advertisement
from .validators import AdvertisementValidation


class AdvertisementSerializer (serializers.ModelSerializer):

    class Meta:
        model = Advertisement
        fields = '__all__'

    def validate(self, data):
        _validators_dict = {
            "title": AdvertisementValidation.validate_title,
            "transaction_number": AdvertisementValidation.validate_transaction,
        }

        errors = {}

        for key, validator in _validators_dict.items():
            try:
                data[key] = validator(data[key])
            except serializers.ValidationError as validation_error:
                errors[key] = validation_error.detail

        if data["start_date"] > data["end_date"]:
            errors["end_date"] = "End date occurs before start date"

        if errors:
            raise serializers.ValidationError(errors)

        return data
