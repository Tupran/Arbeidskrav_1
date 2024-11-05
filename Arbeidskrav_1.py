# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 14:25:11 2024

@author: olean - Ole Andreas Gløersen

"""

# =============================================================================
#
# Beregning av årlige kostnader for elbil og bensibil,
# samt sammenligning av disse.
#
#
# Beregning ut fra nåværende kjørelengde på min forsikring som er:
# 40000 km/år
#
# =============================================================================


# =============================================================================
# Kjørelengde (km/år)
# =============================================================================

K = 40000


# =============================================================================
# Trafikkforsikring både elbil og bensinbil pr kr/dag
# =============================================================================

# pr kr/dag
TF = 8.38

# pr kr/år
TF_aar = TF*365


# =============================================================================
# Oppsett kostnader elbil
# =============================================================================

# Forsikling elbil/år
F_el = 5000

# Forbruk elbil (kW/km)
kW_km = 0.2

# Strømpris (kr/kWh)
kr_kWh = 2

# Kostnad pr km (kr/km)
kost_km_el = kW_km * kr_kWh

# Bomavgift elbil (kr/km)
bom_el = 0.1


# =============================================================================
# Oppsett kostnader bensinbil
# =============================================================================

# Forsikring bensinbil/år
F_ben = 7500

# Kostnad pr km (kr/km)
kost_km_ben = 1

# Bomavgift bensinbil (kr/km)
bom_ben = 0.3


# =============================================================================
# Årlige kostnader elbil
# =============================================================================

aar_kostnader_el = TF_aar + F_el + kost_km_el*K + bom_el*K


# =============================================================================
# Årlige kostnader bensinbil
# =============================================================================

aar_kostnader_ben = TF_aar + F_ben + kost_km_ben*K + bom_ben*K


# =============================================================================
# Differanse elbil/bensinbil (kr/år)
# =============================================================================

diff = aar_kostnader_ben - aar_kostnader_el


# =============================================================================
# Resultat
# =============================================================================

print ()
print ()
print ("*******************************************************")
print ("*                                                     *")
print ("* Sammenligning av årlige kostnader mellom            *")
print ("* elbil og bensinbil (ved 40.000 km/år i kjørelengde) *")
print ("*                                                     *")
print ("*******************************************************")
print ()
print (f"Kostnader for elbil kroner pr år....: {aar_kostnader_el:.2f}")
print ()
print (f"Kostnader for bensinbil kroner pr år: {aar_kostnader_ben:.2f}")
print ()
print (f"Differanse elbil - bensinbil........: {diff:.2f}")
print ("-------------------------------------------------------")
print (f"Elbil er {diff:.2f} kroner billigere enn bensinbil pr år.")
print ()
print ()

