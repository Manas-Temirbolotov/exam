from rest_framework import serializers

from account.models import Author, User


class AuthorRegisterSerializer(serializers.ModelSerializer):
    password_2 = serializers.CharField(max_length=64, write_only=True)

    class Meta:
        model = Author
        fields = ['username', 'password', 'password_2']

    def validate(self, data):
        if data['password'] != data['password_2']:
            raise serializers.ValidationError('Пароли должны совпадать')
        return data

    def create(self, validated_data):
        new_user = User(username=validated_data['username'],)
        new_user.set_password(validated_data['password'])
        new_user.save()
        new_author = Author.objects.create(
            user=new_user
        )
        new_author.save()
        return new_author
