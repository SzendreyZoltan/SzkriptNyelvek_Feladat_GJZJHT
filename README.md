# SzkriptNyelvek_Feladat_GJZJHT

# Vizuális Időjárás és Hőmérsékleti Zóna Szimulátor

## Hallgató adatai

* **Név:** Szendrey Zoltán

* **Neptun-kód:** GJZJHT

## Feladat leírása

### Mit csinál a program?

Ez az interaktív grafikus (GUI) alkalmazás különböző virtuális városok (Budapest, London, Kairó, Reykjavik) időjárási adatait szemlélteti. A programban lehetőség van a városok közötti lapozásra, valamint az aktuális város hőmérsékletének dinamikus növelésére (+1 °C) és csökkentésére (-1 °C). Az alkalmazás a hőmérséklet alapján automatikusan meghatározza az időjárási zónát (Hűvös/Hideg, Kellemes, Meleg), és ennek megfelelően megváltoztatja a felület háttér- és szövegszíneit. Ezen felül egy gombnyomással kiszámítja és megjeleníti a rendszerben tárolt összes város aktuális átlaghőmérsékletét.

### Felhasználói leírás

* **Telepítési igények:** A program futtatásához **nem szükséges** semmilyen külső könyvtár vagy csomag telepítése, mivel kizárólag a Python alapértelmezett, beépített `tkinter` grafikus modulját használja.

* **Szükséges környezet:** Python 3.x értelmező telepítése, valamint a `main.py` és a `SZZ_modul.py` fájlok ugyanabban a mappában történő elhelyezése.

* **Indítás:** A program a `main.py` fájl futtatásával indítható el parancssorból/terminálból a `python main.py` paranccsal, vagy bármilyen fejlesztőkörnyezetből (pl. IDLE, VS Code, PyCharm).

## Felépítés

### Modulok

* **`SZZ_modul.py`**: Saját készítésű modul, amely az üzleti logikát, az adatszerkezetet és a statisztikai számításokat tartalmazza, elkülönítve a grafikus felülettől.

* **`tkinter`** (beépített modul): A grafikus ablak, a szöveges címkék, a vezérlőgombok és a felugró üzenetablak (`messagebox`) megjelenítéséért felelős.

### Függvények

* **`atlaghomerseklet_szamitasa(varosok_listaja)`** *(helye: `SZZ_modul.py`)*: Végigmegy a városokat tároló listán, összegzi azok aktuális hőmérsékletét, majd kiszámítja és visszatérési értékként visszaadja az átlaghőmérsékletet.

### Osztályok

* **`VarosIdojaras`** *(helye: `SZZ_modul.py`)*: Egy adott város adatait (név, hőmérséklet) és a hozzá tartozó logikai műveleteket összefogó osztály.

  * *Metódusai:* `__init__` (adatok inicializálása), `homersekletet_valtoztat` (hőmérséklet növelése/csökkentése), `zona_meghatarozasa` (időjárási zóna és a hozzá tartozó háttér- és betűszínek megállapítása).

* **`IdojarasApp`** *(helye: `main.py`)*: A teljes grafikus felhasználói felületet felépítő és a felhasználói eseményeket (gombnyomásokat) kezelő fő osztály.

  * *Metódusai:* `__init__` (ablak és gombok létrehozása), `kovetkezo_varos` (lapozás a városok között), `homerseklet_novel` (+1 °C), `homerseklet_csokkent` (-1 °C), `statisztika_mutat` (átlaghőmérséklet kiírása felugró ablakban), `frissit_nezet` (felület szövegeinek és színeinek dinamikus frissítése).