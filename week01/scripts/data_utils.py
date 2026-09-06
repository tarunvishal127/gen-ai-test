from typing import List, Dict, Tuple
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

def sum_and_average(nums: List[int]) -> Tuple[float, float]:
    """Type hinting example: Return the sum and average of a list of integers in a tuple."""
    """Return (total, average) for a list of integers. - Docstring example."""
    total = sum(nums)
    return total, total / len(nums) if nums else 0

def city_with_max_population(city_pop: Dict[str, int]) -> str:
    """Return the city with the highest population.""" 
    return max(city_pop, key=city_pop.get)

def large_cities(city_pop: Dict[str, int], threshold: int = 1_000_000) -> List[int]:
    """Return a list of populations for cities with population above the threshold."""
    return [pop for pop in city_pop.values() if pop > threshold]

def classify_number(num: int):
    """Classify a number as Negative, Zero, or Positive."""
    if num < 0:
        return "Negative"
    elif num == 0:
        return "Zero"
    else:
        return "Positive"
    
def analyze_text_file(path: str):
    """Analyze a text file and return the number of lines, words, and characters."""
    with open(path, 'r') as file:
        text = file.readlines()
        num_lines = len(text)
        num_words = sum(len(line.split()) for line in text)
        num_chars = sum(len(line) for line in text)
    return num_lines, num_words, num_chars

def save_stats(stats:dict, out_path:str):
    """Save the statistics to a file."""
    with open(out_path, 'w') as file:
            file.write(f"Lines: {stats[0]}\nWords: {stats[1]}\nCharacters: {stats[2]}\n")

def average_salary(records: list[dict]) -> float:
    """Calculate the average salary from a list of records."""
    logging.info("average_salary called with %d records", len(records))
    
    if not records:
        logging.warning("average_salary called with empty records list; returning 0")
        return 0.0
    
    total_salary = sum(record["salary"] for record in records)
    average = total_salary / len(records)
    
    logging.info("average_salary completed; average salary = %s", average)
    return average



def city_with_highest_avg_salary(records: list[dict]):
    """Return the city with the highest average salary."""
    city_salary = {}
    city_count = {}
    for record in records:
        city = record["city"]
        salary = record["salary"]
        city_salary[city] = city_salary.get(city, 0) + salary
        city_count[city] = city_count.get(city, 0) + 1
    avg_salary_by_city = {city: city_salary[city] / city_count[city] for city in city_salary}
    max_city = max(avg_salary_by_city, key=avg_salary_by_city.get) if avg_salary_by_city else None
    return max_city

def filter_records(records: list[dict], age_threshold: int):
    """Filter records by age threshold."""
    filtered_records = [record for record in records if record["age"] > age_threshold]
    return filtered_records