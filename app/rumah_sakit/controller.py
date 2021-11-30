from django.shortcuts import render


def lihat_rumah_sakit(request):
    return render(request, 'rumah_sakit.html')
