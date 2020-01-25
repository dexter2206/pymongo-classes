# Repozytorium do zajęć z PyMongo


## Zanim zaczniemy

Wszystkie przykłady w tym repozytorium zakładają, że Mongo działa na lokalnej maszynie i domyślnym porcie, jak również
że nie skonfigurowano autoryzacji. Jeżeli Mongo jest skonfigurowane inaczej, proszę pamiętać o odpowiednim 
zmodyfikowaniu przykładów przed ich uruchomieniem.

Przygotowanie:
1. Sklonować repozytorium
2. Zainstalować paczki z pliku requiremets.txt (albo poprzez popup wyświetlany przez PyCharm, albo ręcznie używając 
`pip`)

## Organizacja przykładów

Przykłady korzystają z danych zawartych w pliku [examples/biographies.json](examples/biographies.json).
Skrypty o numerach 01 i 02 ładują dane do bazy danych, więc powinny zostać wykonane przed pozostałymi.
Zaleca się wykonywanie skryptów w kolejności ich numerku.

## Zadania do wykonywania wraz z przykładami

Poniższe zadania dotyczą tej samej kolekcji co przykłady w katalogu examples. Zaleca się wykonywanie ich na bieżąco
po odpowiadających im przykładach w celu potwierdzenia, że materiał prezentowany w danym przykładzie został zrozumiany

- **Example 03**: 
  1. Znaleźć wszystkich ludzi, którzy umarli w XX wieku.
  1. Znaleźć wszystkich ludzi, których imię kończy się na "s".
- **Example 04**:
  1. Zliczyć wszystkich ludzi urodzonych przez 1950 rokiem.
- **Example 06**:
  1. Znaleźć wszystkich ludzi urodzonych przed 1950 rokiem, pobrać jedynie ich imię, nazwisko,
     datę śmierci i urodzenia.
- **Example 07**:
  1. Znaleźć wszystkich ludzi, którzy dokonali więcej niż trzech kontrybucji
  2. Znaleźć wszystkich ludzi, którzy dokonali dokładnie trzech kontrybucji
- **Example 08**:
  1. Znaleźć wszystkich ludzi, którzy dooknali kontrybucji do języka Fortran i otrzymali nagrodę Turing Award
- **Example 09**:
  1. Znaleźć wszystkich ludzi, którzy otrzymali nagrodę ze "Science" w nazwie.
  2. Znaleźć wszystkich ludzi, którzy otrzymali nagrodę w 2001 roku.
- **Example 10**:
  1. Dla każdej z kontrybucji, znaleźć liczbę ludzi którzy jej dokonali.
  2. Dla każdej nagrody znaleźć pierwszy i ostatni rok, w którym została przyznana (oczywiście 
     wśród osób, które istnieją w bazie danych).
     
## Zadania do samodzielnej pracy

Poniższe zadania dotyczą kolekcji którą można znaleźć [tutaj](https://github.com/ozlerhakan/mongodb-json-files/blob/master/datasets/products.json)

Zadania z gwiazdką są trochę trudniejsze.

1. Napisać skrypt ładujący dane z pliku (uwaga, mimo rozszerzenie plik ten nie jest poprawnym JSONem!)
1. Wyświetlić nazwy wszystkich produktów.
2. Wyświetlić wszystkie usługi (czyli produkty o typie "service")
3. Wyświetlić wszystkie produkty w cenie od 20 do 210.
4. Wyświetlić wszystkie produkty będące akcesoriami dla telefonu AC7.
5. Wyświetlić średnią cenę akcesoriów.
5. \* Wyświetlić wszystkie usługi o nielimitowanym dostępnie do danych.
6. \* Wyświetlić średnią cenę akcesoriów pogrupowaną po produkcie do którego pasują.

