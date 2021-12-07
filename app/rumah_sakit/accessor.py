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
            return None

    def _get_rumah_sakit(self, kode: str) -> Optional[RumahSakit]:
        return RumahSakit.objects.filter(pk=kode).first()
    
    def get_rumah_sakit_by_id(self, num: int) -> Optional[RumahSakit]:
        return RumahSakit.objects.get(id=num)
    
    def get_all_rumahsakit(self) -> List[RumahSakit]:
        return RumahSakit.objects.all()

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
    
    def create_jadwal(self, dict_data: Dict[str, Any], obj_rs: RumahSakit
    ) -> Optional[JadwalDokter]:
        try:
            new_jadwal = JadwalDokter(kode=dict_data["kode"], nama=dict_data["nama"], spesialis=dict_data["spesialis"], jadwal=dict_data["jadwal"], rumahsakit=obj_rs)
            new_jadwal.save()
            return new_jadwal
        except:
            return None

    def create_appointment(
        self, dict_data: Dict[str, Any]
    ) -> Optional[AppointmentDokter]:
        try:
            obj = AppointmentDokter(**dict_data)
            obj.save()
            return obj
        except:
            return None
