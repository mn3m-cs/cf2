from rest_framework import serializers
from cof.models import Machine,Pod

class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = ['name','product_type','water_line_compitable','model']


class PodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pod
        fields = ['name','product_type','flavor','pack_size']
