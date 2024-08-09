# These are school projects! Github page may be all cluttered until 2025 or 2026.

work = {

	"Monday": 3, "Tuesday": 4, "Wednesday": 2, "Thursday": 1, "Friday": 1, 
}
work["Saturday"] = 0

work.pop("Wednesday")
print(len(work))

if "Friday" in work:
    print(work)