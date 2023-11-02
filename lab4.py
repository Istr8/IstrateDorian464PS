# -*- coding: utf-8 -*-
"""Lab4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-XIkKw3Kk1TNsHNmXlBFPZDs4DpuQIiw

Exercitiul 2

Pentru a începe, să construim un semnal sinusoidal de frecvență aleatoare, amplitudine unitară și fază nulă. Alegem o frecvență de 5 Hz.

Vom utiliza o frecvență de eșantionare sub-Nyquist, de exemplu 9 Hz. Pentru a genera fenomenul de aliere, să presupunem că avem o frecvență de eșantionare de 9 Hz.
"""

import numpy as np
import matplotlib.pyplot as plt

# Definirea semnalului sinusoidal
t = np.linspace(0, 1, 1000, endpoint=False)
x = np.sin(2 * np.pi * 5 * t)

# Frecventa de esantionare
fs = 9

# Graficul semnalului original si punctele de esantionare
plt.plot(t, x, label='Semnalul original')
plt.stem(np.arange(0, 1, 1 / fs), np.sin(2 * np.pi * 5 * np.arange(0, 1, 1 / fs)), 'r', markerfmt='ro', linefmt='r--', basefmt=' ', label='Punctele de esantionare')
plt.xlabel('Timp')
plt.ylabel('Amplitudine')
plt.title('Esantionarea sub-Nyquist a unui semnal sinusoidal')
plt.legend()
plt.show()

# Definirea altor doua semnale cu frecvente diferite
x1 = np.sin(2 * np.pi * 4 * t)
x2 = np.sin(2 * np.pi * 6 * t)


# Graficul semnalului original si cele doua semnale cu frecvente diferite

plt.figure(figsize=(10, 12))
plt.subplot(3, 1, 1)
plt.plot(t, x, label='Semnalul original')
plt.subplot(3, 1, 2)
plt.plot(t, x1, label='Semnal cu frecventa 4 Hz')
plt.subplot(3, 1, 3)
plt.plot(t, x2, label='Semnal cu frecventa 6 Hz')
plt.stem(np.arange(0, 1, 1 / fs), np.sin(2 * np.pi * 5 * np.arange(0, 1, 1 / fs)), 'r', markerfmt='ro', linefmt='r--', basefmt=' ', label='Punctele de esantionare')
plt.xlabel('Timp')
plt.ylabel('Amplitudine')
plt.title('Esantionarea sub-Nyquist a unui semnal sinusoidal')
plt.legend()
plt.show()

"""Exercitiul 3

Pentru a demonstra că alegerea unei frecvențe de eșantionare mai mare decât frecvența Nyquist înlătură fenomenul de aliere, vom utiliza o frecvență de eșantionare de 12 Hz, care este mai mare decât frecvența Nyquist calculată pentru semnalul cu frecvența de 5 Hz (frecvența Nyquist este jumătate din frecvența semnalului, deci în acest caz 2.5 Hz).

Vom utiliza același cod Python ca mai sus, doar că schimbăm valoarea frecvenței de eșantionare la 12 Hz.
"""

# Frecventa de esantionare mai mare decat frecventa Nyquist
fs_high = 12

# Graficul semnalului original si punctele de esantionare
plt.plot(t, x, label='Semnalul original')
plt.stem(np.arange(0, 1, 1 / fs_high), np.sin(2 * np.pi * 5 * np.arange(0, 1, 1 / fs_high)), 'r', markerfmt='ro', linefmt='r--', basefmt=' ', label='Punctele de esantionare')
plt.xlabel('Timp')
plt.ylabel('Amplitudine')
plt.title('Esantionarea cu o frecventa mai mare decat Nyquist')
plt.legend()
plt.show()

"""În acest grafic, puteți observa cum punctele de eșantionare acum se potrivesc mult mai bine cu semnalul original, iar fenomenul de aliere este eliminat.

De asemenea, putem reprezenta graficul celorlalte două semnale cu frecvențe diferite de 4 Hz și 6 Hz, esantionate la aceeași frecvență mai mare de 12 Hz:
"""

plt.figure(figsize=(10, 12))
plt.subplot(3, 1, 1)
plt.plot(t, x, label='Semnalul original')
plt.subplot(3, 1, 2)
plt.plot(t, x1, label='Semnal cu frecventa 4 Hz')
plt.subplot(3, 1, 3)
plt.plot(t, x2, label='Semnal cu frecventa 6 Hz')
plt.stem(np.arange(0, 1, 1 / fs_high), np.sin(2 * np.pi * 5 * np.arange(0, 1, 1 / fs_high)), 'r', markerfmt='ro', linefmt='r--', basefmt=' ', label='Punctele de esantionare')
plt.xlabel('Timp')
plt.ylabel('Amplitudine')
plt.title('Esantionarea sub-Nyquist a unui semnal sinusoidal')
plt.legend()
plt.show()