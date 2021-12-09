from rest_framework import serializers


class AdvertisementValidation:
    @staticmethod
    def validate_title(title: str) -> str:
        if not str(title).istitle():
            raise serializers.ValidationError(
                "Name can only contain alphabetical symbols"
                )
        return title

    @staticmethod
    def validate_transaction(t_number: str) -> str:
        is_valid = True
        transaction_sections = str(t_number).split('-')
        slash_section = transaction_sections[2].split('/')
        if len(transaction_sections) != 3:
            is_valid = False
        elif not str(transaction_sections[1]).isnumeric():
            is_valid = False
        elif not str(transaction_sections[0]).isalpha():
            is_valid = False
        elif not str(slash_section[0]).isalpha():
            is_valid = False
        elif not str(slash_section[1]).isnumeric():
            is_valid = False
        if not is_valid:
            raise serializers.ValidationError("transaction format is incorrect")
        return t_number
