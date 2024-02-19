class Auto:
  def __init__(self): #  Methode zur Erstellung des Blaupause / Bauplan der Klasse
    self.hersteller = None
    self.modell = None
    self.leistung = None
  def __str__(self):
    return f"{self.hersteller} {self.modell} {self.leistung}"