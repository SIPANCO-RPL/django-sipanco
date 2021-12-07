from typing import Any, Dict, List, Optional
from django.db.models import F

from .models import ReservasiVaksin, JadwalVaksin


class ReservasiVaksinAccessor:
    def __init__(self) -> None:
        pass

    def get_list(
        self,
        pasien_id: Optional[int] = None,
        rs_id: Optional[int] = None,
    ) -> List[ReservasiVaksin]:
        queryset = ReservasiVaksin.objects.all()

        if pasien_id:
            queryset = queryset.filter(pasien__id=pasien_id)

        if rs_id:
            queryset = queryset.filter(jadwal_vaksin__rumah_sakit__id=rs_id)

        return queryset

    def get_valid(
        self,
        pasien_id: Optional[int] = None,
        jadwal_id: Optional[int] = None,
    ) -> List[ReservasiVaksin]:
        queryset = ReservasiVaksin.objects.all().exclude(status="BATAL")
        if pasien_id:
            queryset = queryset.filter(pasien__id=pasien_id)
        
        if jadwal_id:
            queryset = queryset.filter(jadwal_vaksin__id=jadwal_id)

        return queryset

    def create(
        self, dict_data: Dict[str, Any]
    ) -> Optional[ReservasiVaksin]:
        try:
            obj = ReservasiVaksin(**dict_data)
            obj.save()
            return obj
        except Exception as e:
            print(e)
            return None


class JadwalVaksinAccessor:
    def __init__(self) -> None:
        pass

    def get_by_rs(self, rs_id) -> List[JadwalVaksin]:
        queryset = JadwalVaksin.objects.all()
        
        queryset = queryset.filter(rumah_sakit__id=rs_id)

        return queryset

    def get_by_id(self, id) -> Optional[JadwalVaksin]:
        try:
            return JadwalVaksin.objects.get(pk=id)
        except:
            return None
