import requests
import time

weapons = {
  "pistol": ["Glock-18", "Dual Berettas", "P250", "Tec-9", "CZ75-Auto", "Desert Eagle", "R8 Revolver", "USP-S", "P2000", "Five-Seven"],
  "shotgun": ["Nova", "XM1014", "Sawed-Off", "MAG-7"],
  "smg": ["MAC-10", "MP7", "UMP-45", "P90", "PP-Bizon", "MP9", "MP5-SD"],
  "assault_riffle": ["Galil", "AK-47", "SG", "FAMAS", "M4A4", "M4A1-S", "AUG"],
  "sniper_riffle": ["SSG", "AWP", "G3SG1", "SCAR-20"],
  "machine_gun": ["M249", "Negev"]
}
skin = "Redline"
condition = "(Field-Tested)"

all_guns = [weapon for key in weapons.keys() for weapon in weapons[key]]

for weapon in all_guns:
  res = requests.get(f"https://steamcommunity.com/market/priceoverview/?appid=730&currency=3&market_hash_name={weapon} | {skin} {condition}")
  res_json = res.json()
  print("Weapon", weapon)
  print(res_json)
  print("----------")
  time.sleep(2)