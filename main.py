
def count_batteries_by_health(present_capacities):
  counts = {
    "healthy": 0,
    "exchange": 0,
    "failed": 0
  }
  capacityRated = 120
  for capacityPresent in present_capacities:
    sohPercentage = (capacityPresent/capacityRated)*100
    if sohPercentage > 80:
      counts["healthy"] += 1
      print(f"Battery with {capacityPresent} Ah is healthy.")
    elif 62 <= sohPercentage <= 80:
      counts["exchange"] += 1
      print(f"Battery with {capacityPresent} Ah needs replacement.")
    else:
      counts["failed"] += 1
      print(f"Battery with {capacityPresent} Ah has failed.")
  return counts


def test_bucketing_by_health():
  present_capacities = [113, 116, 80, 95, 92, 70]
  counts = count_batteries_by_health(present_capacities)

  print("Counting batteries by SoH...\n")
  print(f"Healthy batteries: {counts['healthy']}")
  print(f"Exchange batteries: {counts['exchange']}")
  print(f"Failed batteries: {counts['failed']}")


if __name__ == '__main__':
  test_bucketing_by_health()
