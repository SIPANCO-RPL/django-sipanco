from typing import Any, Dict, List, Union, Optional

from app.rumah_sakit.models import Ruangan, RumahSakit, AppointmentDokter, JadwalDokter


class RumahSakitAccessor:
    def __init__(self) -> None:
        pass

    def create_ruangan(self, kode: str, kapasitas: int, rumah_sakit: RumahSakit) -> Optional[Ruangan]: 
        try:
            ruangan = Ruangan.objects.create(kode=kode, kapasitas=kapasitas, kapasitasTergunakan=0, rumahSakit=rumah_sakit)
            return ruangan
        except:
            print("gagal")
            return None

    def _get_rumah_sakit(self, kode: str) -> Optional[RumahSakit]:
        return RumahSakit.objects.filter(pk=kode).first()

    def get_all_ruangan(self) -> List[Ruangan]:
        return Ruangan.objects.all()

    def get_ruangan_by_rumah_sakit(self, rumah_sakit: RumahSakit) -> List[Ruangan]:
        return Ruangan.objects.filter(rumahSakit=rumah_sakit)
    
    def get_appointment_dokter(
        self, pasien_id: Optional[int] = None
    ) -> List[AppointmentDokter]:
        queryset = AppointmentDokter.objects.all()

        if pasien_id:
            queryset.filter(pasien__id=pasien_id)

        return queryset

    def create_appointment(
        self, dict_data: Dict[str, Any]
    ) -> Optional[AppointmentDokter]:
        try:
            obj = AppointmentDokter(**dict_data)
            obj.save()
            return obj
        except:
            return None
