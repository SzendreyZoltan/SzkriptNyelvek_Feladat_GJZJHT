class VarosIdojaras:

  def __init__(self, nev, homerseklet):
    self.nev = nev
    self.homerseklet = homerseklet

  def homersekletet_valtoztat(self, ertek):
    self.homerseklet += ertek

  def zona_meghatarozasa(self):
    if self.homerseklet < 15:
      return "Hűvös / Hideg", "#a0c4ff", "#03045e"  # Kék háttér, sötétkék szöveg
    elif 15 <= self.homerseklet <= 25:
      return "Kellemes", "#caffbf", "#1b4332"  # Zöld háttér, sötétzöld szöveg
    else:
      return "Meleg", "#ffadad", "#6a040f"  # Pirosas háttér, bordó szöveg


def atlaghomerseklet_szamitasa(varosok_listaja):
  if not varosok_listaja:
    return 0.0
  osszeg = sum(varos.homerseklet for varos in varosok_listaja)
  return osszeg / len(varosok_listaja)