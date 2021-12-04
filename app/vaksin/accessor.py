from datetime import time, date
from typing import Any, Dict, List, Optional

from .models import ReservasiVaksin, JadwalVaksin


class VaksinAccessor:
    def __init__(self) -> None:
        pass

    def get_reservasi_vaksin(
        self, pasien_id: Optional[int] = None
    ) -> List[ReservasiVaksin]:
        queryset = ReservasiVaksin.objects.all()

        if pasien_id:
            queryset.filter(pasien__id=pasien_id)

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

    def create_vaksin(self, date: date, waktu: time, kuota: int) -> Optional[JadwalVaksin]:
        try:
            jadwalVaksin = JadwalVaksin(date, waktu, kuota, 0)
            jadwalVaksin.save()
            return jadwalVaksin
        except:
            return None

    def get_all_jadwalVaksin(self) -> List[JadwalVaksin]:
        return JadwalVaksin.objects.all()

    def get_jadwalVaksin_by_petugas(self, kode: str) -> List[JadwalVaksin]:
        return JadwalVaksin.objects.filter(rumahSakit__id = kode)