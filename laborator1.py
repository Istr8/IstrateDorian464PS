# -*- coding: utf-8 -*-
"""Laborator1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1c5xsHThpNotBhk8ukEEYo8vjCv-2d2SS
"""

import numpy as np
from matplotlib import pyplot as plt

"""Exercitiul 1

"""

t = np.linspace(0.0, 0.03, 1000)
x = np.cos(520 * np.pi * t + t/3)
y = np.cos(280 * np.pi *t - np.pi/3)
z = np.cos(120* np.pi * t + np.pi/3)

fig, (ax1,ax2,ax3) = plt.subplots(3)
ax1.plot(t,x)
ax2.plot(t,y)
ax3.plot(t,z)

frecventa = 1  # Frequency of the sine wave in Hz
amplitudine = 1  # Amplitude of the sine wave

t2 = np.linspace(0.0, 1.0, 1000)
x2 = np.cos(520 * np.pi * t2 + t2/3)
y2 = np.cos(280 * np.pi *t2 - np.pi/3)
z2 = np.cos(120* np.pi * t2 + np.pi/3)

rata_esantionare = 200
pas_timp = 1 / rata_esantionare

pas_timp

t_esantioane = np.arange(0.0, 1.0, pas_timp)
x_esantionat = amplitudine * np.cos(520 * np.pi * t_esantioane + t_esantioane/3)

y_esantionat = np.cos(280 * np.pi *t_esantioane - np.pi/3)
z_esantionat = np.cos(120* np.pi * t_esantioane + np.pi/3)

# Plotați semnalul continuu și cel esantionat
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(t2, x2)
plt.title('Semnal Continuu')
plt.subplot(2, 1, 2)
plt.stem(t_esantioane, x_esantionat, markerfmt='ro', basefmt='r')
plt.title('Semnal Esantionat')

plt.tight_layout()
plt.show()

# Plotați semnalul continuu și cel esantionat
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(t2, y2)
plt.title('Semnal Continuu')
plt.subplot(2, 1, 2)
plt.stem(t_esantioane, y_esantionat, markerfmt='ro', basefmt='r')
plt.title('Semnal Esantionat')

plt.tight_layout()
plt.show()

# Plotați semnalul continuu și cel esantionat
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(t2, z2)
plt.title('Semnal Continuu')
plt.subplot(2, 1, 2)
plt.stem(t_esantioane, z_esantionat, markerfmt='ro', basefmt='r')
plt.title('Semnal Esantionat')

plt.tight_layout()
plt.show()

"""Exercitiul 3

a) Tesantion = 1/fesantion = 1/2000 = 0.0005s
b) 1 byte = 8 biți
Dacă un eșantion este memorat pe 4 biți, atunci avem nevoie de jumătate de byte pentru a stoca fiecare eșantion, deoarece 4 biți sunt jumătate din 8 biți.

Numărul de eșantioane = Frecvența de eșantionare * Numărul de secunde într-o oră.

Numărul de eșantioane = 2000 eșantioane/s * 3600 s/oră = 7,200,000 eșantioane/oră.

Numărul total de bytes = Numărul total de eșantioane * 0.5 bytes/eșantion.

Numărul total de bytes = 7,200,000 eșantioane/oră * 0.5 bytes/eșantion = 3,600,000 bytes/oră.

Prin urmare, 1 oră de achiziție a semnalului digitizat va ocupa 3,600,000 bytes.
"""