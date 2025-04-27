import random

MAX_MAKINE = 50
MAX_IS = 100
SURE_ARALIK = (1, 100)
GECIS_MALIYET_ARALIK = (0, 20)

n = random.randint(1, MAX_IS)
m = random.randint(1, MAX_MAKINE)

print(f"İş sayısı: {n}, Makine sayısı: {m}")

is_sureleri = [[random.randint(*SURE_ARALIK) for _ in range(m)] for _ in range(n)]

gecis_maliyetleri = [[random.randint(*GECIS_MALIYET_ARALIK) for _ in range(m)] for _ in range(m)]

dp = [[float('inf')] * m for _ in range(n)]

for j in range(m):
    dp[0][j] = is_sureleri[0][j]

for i in range(1, n):
    for j in range(m):
        for k in range(m):
            toplam = dp[i-1][k] + gecis_maliyetleri[k][j] + is_sureleri[i][j]
            dp[i][j] = min(dp[i][j], toplam)

min_toplam_sure = min(dp[n-1])
print("Minimum toplam süre:", min_toplam_sure, "saniyedir.")



# Karmaşıklık Analizi:
# Zaman karmaşıklığı (Time Complexity):
#  - Üç iç içe döngü: O(n * m * m) = O(n * m²)
#  - Çünkü her iş için, her makine kombinasyonu kontrol ediliyor.
#
# Uzay karmaşıklığı (Space Complexity):
#  - dp tablosu: O(n * m)
#  - is_sureleri matrisi: O(n * m)
#  - gecis_maliyetleri matrisi: O(m * m)
#  - Toplam: O(n * m + m²)
#  - Genellikle n > m olduğu için baskın terim: O(n * m)
