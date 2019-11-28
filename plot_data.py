import matplotlib.pyplot as plt


''' Sigmoide vs ReLU pour score 2
# Sigmoide
plt.plot([-56.4, -34.78, -49.18, -56.88, -46.4, -40.7, -28.14, -5.92, -13.32, 7.36, 31.08, 49.66, 47.24, 62.54, 112.72, 92.86, 62.54, 148.08, 126.28, 134.74, 158.02, 186.52, 177.2, 165, 228.18, 191.98, 251.5, 210.54, 281.84, 236.54, 214.02, 274.86, 305.84, 358.3, 368.06, 368.94, 366.92, 318.14, 392.5, 321.64, 320.54], label='Sigmoide')
# ReLU
plt.plot([-55.92, -54.14, -40.1, -53.12, -20.76, -48.16, -11.2, 26.12, 47.74, 78.62, 83.44, 125.26, 133.9, 138.04, 157.7, 163.84, 186.76, 195.76, 181.08, 208.82, 222.4, 247.64, 297.68, 300.62, 224.66, 307.38, 302.66, 306.2, 353.34, 281.8, 375.58, 351.1, 429.54, 395.32, 407.46, 417.82, 491.62, 423.32, 439.36, 437.86, 430.28], label='ReLU')
# '''

''' Sigmoide avec SCORE1
plt.plot([-40.19, -39.48, -43.01, -36.76, -36.78, -31.23, -17.16, -9.2, -4.1, -1.21, 15.78, 18.11, 8.76, 9.69, 20.47, -7.87, -0.26, 42.53, -3.23, 36.83, -4.75, 27.3, 41.18, 22.26, 22.92, 66.41, 64.38, 24.0, 48.5, 86.96, 63.85, 98.25, 78.76, 111.3, 89.71, 85.95, 82.68, 52.33, 90.79, 74.17, 77.12, 83.91, 83.94, 38.07, 90.64, 36.1, 80.32, 59.93, 68.25, 44.67, 69.52, 10.5, 75.11, 58.25, 66.6, 105.4, 93.63, 52.4, 118.09, 77.71, 80.74, 94.67, 81.5, 82.1, 82.73, 102.88, 86.47, 79.67, 77.6, 97.92, 106.62, 103.28, 79.62, 120.45, 106.84, 64.06, 104.47, 112.51, 133.97, 106.84, 110.0, 106.03, 60.98, 113.53, 139.41, 100.18, 102.84, 141.11, 101.3, 112.62, 147.61, 123.86, 98.44, 118.49, 121.9, 116.38, 140.3, 159.13, 128.06, 109.89])
plt.plot([-37.82, -28.91, -32.65, -30.41, -19.74, -15.35, -7.96, -7.24, -12.21, -2.48, 2.65, 8.1, -8.11, -4.25, -3.25, 17.68, 41.37, 9.8, -9.73, 25.24, 2.85, 2.73, 19.11, 24.08, 24.9, 34.28, 36.27, 33.84, 57.96, 36.34, 68.22, 36.09, 68.55, 62.8, 102.29, 56.97, 66.49, 88.27, 32.68, 58.6, 91.51, 74.15, 39.47, 68.89, 63.63, 39.11, 18.84, 71.28, 41.78, 4.58, 27.3, 33.58, 59.01, 57.25, 56.33, 35.36, 69.08, 54.18, 35.19, 43.61, 104.9, 51.85, 45.46, 34.55, 49.33, 41.95, 30.27, 3.22, 25.63, 48.89, 42.61, 35.58, 58.46, 71.36, 11.37, 4.35, 33.26, 33.18, 57.04, 55.3, 29.08, -5.34, 41.27, 2.76, 53.22, 4.65, 19.73, 46.1, 57.88, 18.8, 54.27, 23.89, 18.96, 35.48, 40.79, -6.97, 32.95, 62.83, 47.05, 2.42])
'''

''' ReLU data SCORE 1
plt.plot([-42.05, -36.3, -34.25, -30.96, -22.59, -11.06, -5.1, -3.75, -0.52, -6.42, -3.29, 4.05, 6.22, 4.96, 26.55,
          16.87, 46.03, 14.35, 3.26, 18.6, 36.72, 26.07, 21.49, 35.56, 38.26, 27.33, 48.91, 71.21, 53.97, 65.74, 67.17,
          32.31, 70.77, 35.75, 62.2, 50.06, 74.32, 80.89, 43.15, 69.74, 70.84, 101.55, 119.09, 108.83, 93.94, 103.31,
          134.18, 99.44, 102.96, 127.78, 94.89, 126.74, 104.02, 114.19, 99.56, 135.67, 148.7, 81.22, 133.53, 118.61,
          142.53, 132.95, 127.75, 156.0, 136.43, 126.92, 138.42, 140.77, 131.1, 140.03, 137.77, 113.87, 119.65, 127.63,
          117.12, 121.71, 143.9, 136.73, 148.2, 123.43, 131.71, 127.69, 145.0, 156.31, 159.78, 112.16, 115.09, 127.66,
          157.37, 141.42, 154.11, 142.28, 149.28, 131.12, 135.32, 145.1, 117.62, 154.27, 170.13, 155.86] )

plt.plot([-45.19, -39.46, -39.93, -32.22, -31.4, -18.69, -21.92, -14.86, -18.91, -5.0, -8.47, -12.81, 21.2, 15.77,
          14.85, 5.4, 19.77, 19.73, 5.15, 18.21, 22.38, 38.23, 52.4, 11.95, 23.33, 12.72, 11.55, 42.02, 61.46, 67.8,
          48.55, 62.42, 29.32, 87.65, 95.18, 68.57, 50.7, 68.33, 49.46, 69.96, 112.0, 102.86, 85.4, 95.52, 81.64, 70.11,
          74.61, 62.51, 109.25, 92.05, 75.78, 78.88, 54.27, 59.17, 64.02, -5.08, 102.76, 62.72, 96.46, 18.8, 89.82,
          32.53, 75.96, 95.9, 103.89, 81.66, 104.57, 116.6, 67.77, 83.13, 91.06, 112.65, 91.65, 96.38, 103.78, 79.85,
          81.1, 67.41, 100.88, 71.92, 91.41, 100.49, 109.1, 91.26, 96.0, 86.79, 88.11, 110.9, 100.37, 112.77, 84.24,
          80.08, 88.36, 74.8, 83.82, 92.21, 100.12, 53.79, 77.72, 96.85])'''
plt.ylabel('Nombre de points')
plt.xlabel('Générations')
plt.title("Comparaison entre Sigmoide et ReLU sur 40 générations")
plt.legend()
plt.show()
