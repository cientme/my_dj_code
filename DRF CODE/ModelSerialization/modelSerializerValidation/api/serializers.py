from rest_framework import serializers
from  .models import Student

# Validators 


class StudentSerializer(serializers.ModelSerializer):
    def start_with_r(value):
        if value[0].lower() !='r':
            raise serializers.ValidationError("Name must be start withletter R or r")
            
    name = serializers.CharField(validators=[start_with_r])
    class Meta:
        model = Student
        fields = ['name', 'roll', 'city']

    # Fields Level Validation 
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError("Roll number must less than 200!!")
        return value


    # Object Level Vatidation 
    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == 'veeru' and ct.lower() != 'up':
            raise serializers.ValidationError("City must be Kolkata")
        return data

   
