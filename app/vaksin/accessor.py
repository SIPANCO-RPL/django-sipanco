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
            queryset.filter(pasien_id=pasien_id)

        return queryset

    def create_reservasi(
        self, dict_data: Dict[str, Any]
    ) -> Optional[ReservasiVaksin]:
        try:
            return ReservasiVaksin(**dict_data)
        except:
            return None
