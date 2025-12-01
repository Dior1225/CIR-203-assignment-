# ==============================================
# **EXERCISE 2: PYTHON LISTS (LOGISTICS SECTOR)**
# ==============================================

routes = ["Nairobi-Kisumu", "Mombasa-Malindi", "Nakuru-Eldoret",
          "Nyeri-Nanyuki", "Garissa-Mwingi", "Kitale-Bungoma",
          "Narok-Kajiado", "Isiolo-Marsabit", "Naivasha-Gilgil",
          "Thika-Muranga"]
print("Routes:", routes)

routes.append("Kakamega-Busia")
routes.remove("Garissa-Mwingi")
print("Updated routes:", routes)

routes.sort()
routes.reverse()
print("Sorted & reversed routes:", routes)

count_N = sum(1 for r in routes if r.startswith("N"))
print("Routes starting with N:", count_N)

long_routes = [r for r in routes if len(r) > 10]
print("Routes longer than 10 chars:", long_routes)
