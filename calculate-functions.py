# Eingabe: Maße der drei Räume
raum1_laenge = 5  # Länge des ersten Raumes (Meter)
raum1_breite = 3.5  # Breite des ersten Raumes (Meter)
raum2_laenge = 4.5  # Länge des zweiten Raumes (Meter)
raum2_breite = 5  # Breite des zweiten Raumes (Meter)
raum3_laenge = 3.5  # Länge des dritten Raumes (Meter)
raum3_breite = 4  # Breite des dritten Raumes (Meter)

# Berechnung der Flächen
raum1_flaeche = raum1_laenge * raum1_breite
raum2_flaeche = raum2_laenge * raum2_breite
raum3_flaeche = raum3_laenge * raum3_breite

# Berechnung der gesamten Wohnfläche
wohnflaeche = raum1_flaeche + raum2_flaeche + raum3_flaeche

# Eingabe: Gesamtmietpreis
mietpreis_total = 1250  # Gesamtmietpreis in Euro

# Berechnung des Quadratmeterpreises
qm_preis = mietpreis_total / wohnflaeche

# Ausgabe der Ergebnisse
print("\nFlächen der Räume:")
print(f"Raum 1: {raum1_flaeche:.2f} m²")
print(f"Raum 2: {raum2_flaeche:.2f} m²")
print(f"Raum 3: {raum3_flaeche:.2f} m²")
print(f"Gesamte Wohnfläche: {wohnflaeche:.2f} m²")
print(f"Quadratmeterpreis: {qm_preis:.2f} Euro/m²")
