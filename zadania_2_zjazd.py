# # Nauka programowania w Pythonie - ćwiczenia domowe

# ## 3. Funkcje

# Przy pisaniu wszystkich funkcji pamiętaj o `type-hinting`, `docstring`
# i stworzeniu testów do weryfikacji czy funkcja działa poprawnie.

# ### Zadanie 3.1 Funkcje liczbowe

# Stwórz następujące funkcje. Niech każda z nich przyjmuje w argument do przeliczenia i zwraca przeliczoną wartość.

# 1. `stopy_na_metry` - przelicza odległość wyrażoną w stopach na metry,
# 2. `max` - zwraca większą z dwóch liczb - postaraj się nie używać funkcji `max` wbudowanej w pythona
# 3. `srednia` - oblicza średnią z dwóch liczb,
# 4. `pole_kola` - oblicza pole koła o podanym promieniu (jeden parametr)
# podpowiedź: wartość PI jest dostępna jako `Math.PI`
# 5. `bmi` - oblicza współczynnik BMI dla podanych dwóch parametrów: wzrostu w metrach i wagi w kg.
# 6. `pole_trojkata` - z trzema parametrami - oblicza pole trójkąta o podanych bokach z wzoru Herona.
# 7. `kilometry_na_mile` - przelicza odległość wyrażoną w kilometrach na mile
# 8. `mile_na_kilometry` - przelicza odległość wyrażoną w milach na kilometry

# Dla wybranych napisz też interaktywne programy, które pytają użytkownika o dane i wypisują wynik.

# ### Zadanie 3.2 | Miesiące

# Zapytaj użytkownika o nazwę miesiąca i na tej podstawie wypisz mu ile dni na dany miesiąc.
# Logikę obliczania liczby dni wydziel do osobnej funkcji.

# **Wersja A**
# Nie przyjmuj się lutym - zwracaj zawsze jedną wartość.

# **Wersja B (trudniejsza)**
# Jeżeli użytkownik poda luty - zapytaj go o rok. Na tej podstawie policz czy w tym roku luty był przestępny czy nie.
#
# ### Zadanie 3.3 | Operacje na listach

# Stwórz następujące funkcje. Każda z nich będzie przyjmowała listę liczb
# i na tej podstawie wykona odpowiednie operacje i zwróci odpowiedni wynik.

# ```
# lista_liczb = [10, 20, 30, 40]
# wynik = suma(lista_liczb)
# ```
# - `suma(liczby)` - zwraca sumę liczb z listy `liczby` - postaraj się nie używać funkcji `sum` wbudowanej w pythona
# - `srednia(liczby)` - zwraca średnią wartość z listy `liczby`
# - `max(liczby)` – zwraca największą wartość z listy
# `liczby` - postaraj się nie używać funkcji `max` wbudowanej w pythona
# - `roznica_min_max(liczby)` – różnica pomiędzy największą a najmniejszą liczbą w liście; `0` jeśli tablica jest pusta
# - `wypisz_wieksze(liczby, x)` – wypisuje (`print()`) wszystkie te liczby z listy `liczby`, które są większe od `x`
# - `pierwsza_wieksza(liczby, x)` – zwraca (`return`) pierwszą znalezioną w
# `liczby` liczbę większą od `x`; zwraca `None`, jeśli takiej liczby tam nie ma
# - `suma_wiekszych(liczby, x)` – zwraca (`return`) sumę liczb z listy `liczby`, które są większe niż `x`
# - `ile_wiekszych(liczby, x)` – liczy ile elementów listy `liczby` jest większych od liczby `x`
# - `wypisz_podzielne(liczby, x)` – wypisuje (`print`) wszystkie te liczby z listy `liczby`,
# które są podzielne przez `x`
# - `pierwsza_podzielna(liczby, x)` – zwraca (`return`) pierwszą znalezioną w
# `liczby` liczbę podzielną przez `x`; zwraca `None`, jeśli takiej liczby tam nie ma
# - `znajdz_wspolny(liczby1, liczby2)` – zwraca element (liczbę), który występuje zarówno w liście
# `liczby1`, jak i `liczby2`; zwraca `None`, jeśli takiego elementu nie ma
#
# ### Zadanie 3.4 | Przycinanie listy
# ​
# Zaimplementuj funkcję przycinającą listę na podstawie podanego warunku początkowego oraz końcowego:
# ​
# Przykład użycia:
#
# > przytnij(
# data = [1, 2, 3, 4, 5, 6, 7],
# start = lambda x: x > 3,
# stop = lambda x: x == 6,
# )
#
# [4, 5, 6]