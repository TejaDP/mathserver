from django.shortcuts import render

from django.shortcuts import render
def physics(request):
    power = ''
    intensity=''
    resistance=''

    if request.method == 'POST':
        intensity = float(request.POST.get('intensity'))
        resistance = float(request.POST.get('resistance'))
        power = (intensity ** 2) * resistance 
        return render(request, 'power.html', {'power': power, 'intensity':intensity, 'resistance':resistance,
})
