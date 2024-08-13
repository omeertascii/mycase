from rest_framework import serilaizers, viewsets
from .models import WorkGroup

class WorkGroupSerilaizer(serilaizers.ModelSerilaizer):
    class Meta:
        model = WorkGroup
        fields = '__all__'
        
class WorkGroupViewSet(viewsets.ModelViewSet):
    queryset = WorkGroup.objects.all()
    serilaizer_class = WorkGroupSerilaizer