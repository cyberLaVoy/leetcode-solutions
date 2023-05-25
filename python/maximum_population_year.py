import numpy as np

class Solution:
    def maximumPopulation(self, logs: list[list[int]]) -> int:
        """
        Finds the earliest year with the maximum population based on given living range logs.

        Args:
            logs (list[list[int]]): A list of living range logs, where each log is represented as [birth_year, death_year].

        Returns:
            int: The earliest year with the maximum population.

        """
        population_per_year = {}  # A dictionary to store the population count for each year
        logs = np.array(logs)  # Convert logs to a NumPy array for easier calculations
        min_year = logs.min()  # Find the minimum year in the logs
        max_year = logs.max()  # Find the maximum year in the logs
        
        # Iterate over each year from the minimum to the maximum year
        for year in range(min_year, max_year + 1):
            if year not in population_per_year.keys():
                population_per_year[year] = 0  # Initialize the population count for each year to 0
            
            # Iterate over each living range log
            for living_range in logs:
                # Check if the current year falls within the living range (not including year of death)
                if year >= living_range[0] and year < living_range[-1]:
                    population_per_year[year] += 1  # Increment the population count for the current year
        
        max_population = max(population_per_year.values())  # Find the maximum population count
        earliest_year_at_max_population = None
        
        # Iterate over the years in ascending order
        for year in sorted(population_per_year.keys()):
            # Find the earliest year with the maximum population
            if population_per_year[year] == max_population:
                earliest_year_at_max_population = year
                break
        
        return earliest_year_at_max_population  # Return the earliest year with the maximum population

solution = Solution()
example1 = solution.maximumPopulation( [[1993,1999],[2000,2010]] )
print(example1)