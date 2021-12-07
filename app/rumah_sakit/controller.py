from django.shortcuts import render


def lihat_rumah_sakit(request):
    return render(request, 'rumah_sakit.html')

def lihat_jadwal_dokter(request):
    return render(request, 'jadwal_dokter.html')

def lihat_ruangan(request):
    return render(request, 'list_ruangan.html')

def create_jadwal_dokter(request):
    return render(request, 'create_jadwal_dokter.html')

def create_ruangan(request):
    return render(request, 'create_ruangan.html')

def create_appointment(request):
    return render(request, 'create_appointment.html')

def list_appointment(request):
    return render(request, 'list_appointment.html')