import alsaaudio # этот модуль надо предварительно установить: sudo apt-get install python-alsaaudio
mix = alsaaudio.Mixer() # инициализируем объект микшера
vol = mix.getvolume() # получили текущую громкость
mix.setvolume(90) # теперь пусть динамики поорут :) - установим громкость 90
