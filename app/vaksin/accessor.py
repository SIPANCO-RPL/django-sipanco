from typing import Any, Dict, List, Optional

from .models import ReservasiVaksin, JadwalVaksin


class ReservasiVaksinAccessor:
    def __init__(self) -> None:
        pass

    def get_reservasi_vaksin(
        self,
        pasien_id: Optional[int] = None,
        rs_id: Optional[int] = None,
    ) -> List[ReservasiVaksin]:
        queryset = ReservasiVaksin.objects.all()

        if pasien_id:
            queryset.filter(pasien__id=pasien_id)

        if rs_id:
            queryset.filter(jadwal_vaksin__rumah_sakit__id=rs_id)

        return queryset

    def create_reservasi(
        self, dict_data: Dict[str, Any]
    ) -> Optional[ReservasiVaksin]:
        try:
            obj = ReservasiVaksin(**dict_data)
            obj.save()
            return obj
        except:
            return None


class JadwalVaksinAccessor:
    def __init__(self) -> None:
        pass

    def get_by_rs(self, rs_id) -> List[JadwalVaksin]:
        queryset = JadwalVaksin.objects.all()
        
        queryset.filter(rumah_sakit__id=rs_id)

        return queryset
