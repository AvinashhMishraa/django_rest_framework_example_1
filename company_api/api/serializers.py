from rest_framework import serializers
from api.models import Company, Employee



# Company serializer
class CompanySerializer(serializers.HyperlinkedModelSerializer):

    id = serializers.ReadOnlyField()
    summary = serializers.SerializerMethodField()       # to call the get_summary() method

    class Meta:
        model = Company
        # fields = "__all__"
        fields = ["url", "id", "name", "location", "about", "type", "added_date", "active", "ceo", "summary"]
        
    # add a custom field to a ModelSerializer without actually adding it in the Model
    def get_summary(self, obj):
        return f"{obj.name} is a {obj.location} based {obj.type} company."
    


# Employee serializer
class EmployeeSerializer(serializers.HyperlinkedModelSerializer):

    id = serializers.ReadOnlyField()

    class Meta:
        model = Employee
        fields = "__all__"