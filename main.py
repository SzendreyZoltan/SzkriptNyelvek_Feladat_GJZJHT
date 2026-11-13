from SZZ_modul import VarosIdojaras, atlaghomerseklet_szamitasa
import tkinter as tk
from tkinter import messagebox


class IdojarasApp:

  def __init__(self, root):
    self.root = root
    self.root.title("Vizuális Időjárás és Hőmérsékleti Zóna Szimulátor")
    self.root.geometry("420x425")
    self.root.resizable(False, False)

    self.varosok = [
        VarosIdojaras("Budapest", 20),
        VarosIdojaras("London", 12),
        VarosIdojaras("Kairó", 32),
        VarosIdojaras("Reykjavik", 5),
    ]
    self.aktualis_index = 0

    self.cim_label = tk.Label(
        root, text="", font=("Arial", 18, "bold"), pady=12
    )
    self.cim_label.pack()

    self.temp_label = tk.Label(root, text="", font=("Arial", 15), pady=6)
    self.temp_label.pack()

    self.zona_label = tk.Label(
        root, text="", font=("Arial", 13, "italic"), pady=6
    )
    self.zona_label.pack()

    self.kovetkezo_gomb = tk.Button(
        root,
        text="Következő város ➔",
        command=self.kovetkezo_varos,
        font=("Arial", 11),
        width=28,
    )
    self.kovetkezo_gomb.pack(pady=8)

    self.noveles_gomb = tk.Button(
        root,
        text="Hőmérséklet növelése (+1 °C)",
        command=self.homerseklet_novel,
        font=("Arial", 11),
        width=28,
    )
    self.noveles_gomb.pack(pady=6)

    self.csokkentes_gomb = tk.Button(
        root,
        text="Hőmérséklet csökkentése (-1 °C)",
        command=self.homerseklet_csokkent,
        font=("Arial", 11),
        width=28,
    )
    self.csokkentes_gomb.pack(pady=6)

    self.atlag_gomb = tk.Button(
        root,
        text="Összesített átlaghőmérséklet",
        command=self.statisztika_mutat,
        font=("Arial", 11),
        width=28,
    )
    self.atlag_gomb.pack(pady=8)

    self.frissit_nezet()

  def kovetkezo_varos(self):
    self.aktualis_index = (self.aktualis_index + 1) % len(self.varosok)
    self.frissit_nezet()

  def homerseklet_novel(self):
    aktualis_varos = self.varosok[self.aktualis_index]
    aktualis_varos.homersekletet_valtoztat(1)
    self.frissit_nezet()

  def homerseklet_csokkent(self):
    aktualis_varos = self.varosok[self.aktualis_index]
    aktualis_varos.homersekletet_valtoztat(-1)
    self.frissit_nezet()

  def statisztika_mutat(self):
    atlag = atlaghomerseklet_szamitasa(self.varosok)
    messagebox.showinfo(
        "Statisztikai Elemzés",
        "A rendszerben tárolt városok átlaghőmérséklete:\n\n"
        f"{atlag:.1f} °C",
    )

  def frissit_nezet(self):
    varos = self.varosok[self.aktualis_index]
    zona_szoveg, hatter_szin, szoveg_szin = varos.zona_meghatarozasa()

    self.cim_label.config(
        text=f"Város: {varos.nev}", bg=hatter_szin, fg=szoveg_szin
    )
    self.temp_label.config(
        text=f"Hőmérséklet: {varos.homerseklet} °C",
        bg=hatter_szin,
        fg=szoveg_szin,
    )
    self.zona_label.config(
        text=f"Időjárási zóna: {zona_szoveg}", bg=hatter_szin, fg=szoveg_szin
    )
    self.root.config(bg=hatter_szin)


if __name__ == "__main__":
  fo_ablak = tk.Tk()
  app = IdojarasApp(fo_ablak)
  fo_ablak.mainloop()