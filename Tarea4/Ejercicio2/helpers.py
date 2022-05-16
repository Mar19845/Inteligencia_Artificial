from functools import cmp_to_key

import numpy
import random

random.seed()

NUMBER_DIGITS = 9  # Number of digits (in the case of standard Sudoku puzzles, this is 9).


class Population:
    """ A set of candidate solutions to the Sudoku puzzle. These candidates are also known as the chromosomes
     in the population. """

    def __init__(self):
        self.candidates = []
        return

    def seed(self, nc, given):
        self.candidates = []

        # Determine the legal values that each square can take.
        helper = Candidate()
        helper.values = [[[] for j in range(0, NUMBER_DIGITS)] for i in range(0, NUMBER_DIGITS)]
        for row in range(0, NUMBER_DIGITS):
            for column in range(0, NUMBER_DIGITS):
                for value in range(1, 10):
                    if ((given.values[row][column] == 0) and not (
                            given.is_column_duplicate(column, value) or given.is_block_duplicate(row, column, value) or
                            given.is_row_duplicate(row, value))):
                        # Value is available.
                        helper.values[row][column].append(value)
                    elif given.values[row][column] != 0:
                        # Given/known value from file.
                        helper.values[row][column].append(given.values[row][column])
                        break

        # Seed a new population.
        for p in range(0, nc):
            g = Candidate()
            for i in range(0, NUMBER_DIGITS):  # New row in candidate.
                row = numpy.zeros(NUMBER_DIGITS)

                # Fill in the givens.
                for j in range(0, NUMBER_DIGITS):  # New column j value in row i.

                    # If value is already given, don't change it.
                    if given.values[i][j] != 0:
                        row[j] = given.values[i][j]
                    # Fill in the gaps using the helper board.
                    elif given.values[i][j] == 0:
                        row[j] = helper.values[i][j][random.randint(0, len(helper.values[i][j]) - 1)]

                # If we don't have a valid board, then try again. There must be no duplicates in the row.
                while len(list(set(row))) != NUMBER_DIGITS:
                    for j in range(0, NUMBER_DIGITS):
                        if given.values[i][j] == 0:
                            row[j] = helper.values[i][j][random.randint(0, len(helper.values[i][j]) - 1)]

                g.values[i] = row

            self.candidates.append(g)

        # Compute the fitness of all candidates in the population.
        self.update_fitness()

        print('Seeding complete.')

    def update_fitness(self):
        """ Update fitness of every candidate/chromosome. """
        for candidate in self.candidates:
            candidate.update_fitness()

    def sort(self):
        """ Sort the population based on fitness. """
        self.candidates.sort(key=cmp_to_key(self.sort_fitness))

    @staticmethod
    def sort_fitness(x, y):
        """ The sorting function. """
        if x.fitness < y.fitness:
            return 1
        elif x.fitness == y.fitness:
            return 0
        else:
            return -1


class Candidate:
    """ A candidate solutions to the Sudoku puzzle. """

    def __init__(self):
        self.values = numpy.zeros((NUMBER_DIGITS, NUMBER_DIGITS), dtype=int)
        self.fitness = 0.0

    def update_fitness(self):
        """ The fitness of a candidate solution is determined by how close it is to being the actual solution
        to the puzzle. The actual solution (i.e. the 'fittest') is defined as a 9x9 grid of numbers in the
        range [1, 9] where each row, column and 3x3 block contains the numbers [1, 9] without any duplicates
        (see e.g. https://www.sudoku.com/); if there are any duplicates then the fitness will be lower. """

        row_count = numpy.zeros(NUMBER_DIGITS)
        column_count = numpy.zeros(NUMBER_DIGITS)
        block_count = numpy.zeros(NUMBER_DIGITS)
        row_sum = 0
        column_sum = 0
        block_sum = 0

        for i in range(0, NUMBER_DIGITS):  # For each row...
            for j in range(0, NUMBER_DIGITS):  # For each number within it...
                row_count[self.values[i][j] - 1] += 1  # ...Update list with occurrence of a particular number.
                column_count[self.values[j][i] - 1] += 1  # ...Update list with occurrence of a particular number.

            row_sum += (1.0 / len(set(row_count))) / NUMBER_DIGITS
            row_count = numpy.zeros(NUMBER_DIGITS)

            column_sum += (1.0 / len(set(column_count))) / NUMBER_DIGITS
            column_count = numpy.zeros(NUMBER_DIGITS)

        # For each block...
        for i in range(0, NUMBER_DIGITS, 3):
            for j in range(0, NUMBER_DIGITS, 3):
                block_count[self.values[i][j] - 1] += 1
                block_count[self.values[i][j + 1] - 1] += 1
                block_count[self.values[i][j + 2] - 1] += 1

                block_count[self.values[i + 1][j] - 1] += 1
                block_count[self.values[i + 1][j + 1] - 1] += 1
                block_count[self.values[i + 1][j + 2] - 1] += 1

                block_count[self.values[i + 2][j] - 1] += 1
                block_count[self.values[i + 2][j + 1] - 1] += 1
                block_count[self.values[i + 2][j + 2] - 1] += 1

                block_sum += (1.0 / len(set(block_count))) / NUMBER_DIGITS
                block_count = numpy.zeros(NUMBER_DIGITS)

        # Calculate overall fitness.
        if int(row_sum) == 1 and int(column_sum) == 1 and int(block_sum) == 1:
            fitness = 1.0
        else:
            fitness = column_sum * block_sum * row_sum

        self.fitness = fitness

    def mutate(self, mutation_rate, given):
        """ Mutate a candidate by picking a row, and then picking two values within that row to swap. """

        r = random.uniform(0, 1.1)
        while r > 1:  # Outside [0, 1] boundary - choose another
            r = random.uniform(0, 1.1)

        success = False
        if r < mutation_rate:  # Mutate.
            while not success:
                row1 = random.randint(0, 8)
                row2 = row1

                from_column = random.randint(0, 8)
                to_column = random.randint(0, 8)
                while from_column == to_column:
                    from_column = random.randint(0, 8)
                    to_column = random.randint(0, 8)

                # Check if the two places are free...
                if given.values[row1][from_column] == 0 and given.values[row1][to_column] == 0:
                    # ...and that we are not causing a duplicate in the rows' columns.
                    if (not given.is_column_duplicate(to_column, self.values[row1][from_column])
                            and not given.is_column_duplicate(from_column, self.values[row2][to_column])
                            and not given.is_block_duplicate(row2, to_column, self.values[row1][from_column])
                            and not given.is_block_duplicate(row1, from_column, self.values[row2][to_column])):
                        # Swap values.
                        temp = self.values[row2][to_column]
                        self.values[row2][to_column] = self.values[row1][from_column]
                        self.values[row1][from_column] = temp
                        success = True

        return success


class Given(Candidate):
    """ The grid containing the given/known values. """

    def __init__(self, values):
        super().__init__()
        self.values = values

    def is_row_duplicate(self, row, value):
        """ Check whether there is a duplicate of a fixed/given value in a row. """
        for column in range(0, NUMBER_DIGITS):
            if self.values[row][column] == value:
                return True
        return False

    def is_column_duplicate(self, column, value):
        """ Check whether there is a duplicate of a fixed/given value in a column. """
        for row in range(0, NUMBER_DIGITS):
            if self.values[row][column] == value:
                return True
        return False

    def is_block_duplicate(self, row, column, value):
        """ Check whether there is a duplicate of a fixed/given value in a 3 x 3 block. """
        i = 3 * (int(row / 3))
        j = 3 * (int(column / 3))

        if ((self.values[i][j] == value)
                or (self.values[i][j + 1] == value)
                or (self.values[i][j + 2] == value)
                or (self.values[i + 1][j] == value)
                or (self.values[i + 1][j + 1] == value)
                or (self.values[i + 1][j + 2] == value)
                or (self.values[i + 2][j] == value)
                or (self.values[i + 2][j + 1] == value)
                or (self.values[i + 2][j + 2] == value)):
            return True
        else:
            return False


class Tournament:
    """ The crossover function requires two parents to be selected from the population pool.
    The Tournament class is used to do this.Two individuals are selected from the population
    pool and a random number in [0, 1] is chosen. If this number is less than the
    'selection rate' (e.g. 0.85), then the fitter individual is selected; otherwise, the weaker
    one is selected.
    """

    def __init__(self, selection_rate):
        self.sr = selection_rate

    def compete(self, candidates):
        """ Pick 2 random candidates from the population and get them to compete against each other. """
        c1 = candidates[random.randint(0, len(candidates) - 1)]
        c2 = candidates[random.randint(0, len(candidates) - 1)]
        f1 = c1.fitness
        f2 = c2.fitness

        # Find the fittest and the weakest.
        if f1 > f2:
            fittest = c1
            weakest = c2
        else:
            fittest = c2
            weakest = c1

        r = random.uniform(0, 1.1)
        while r > 1:  # Outside [0, 1] boundary. Choose another.
            r = random.uniform(0, 1.1)
        if r < self.sr:
            return fittest
        else:
            return weakest


class CycleCrossover:
    """ Crossover relates to the analogy of genes within each parent candidate mixing together in the hopes
     of creating a fitter child candidate. Cycle crossover is used here
     (see e.g. A. E. Eiben, J. E. Smith. Introduction to Evolutionary Computing. Springer, 2007). """

    def __init__(self):
        pass

    def crossover(self, parent1, parent2, crossover_rate):
        """ Create two new child candidates by crossing over parent genes. """
        child1 = Candidate()
        child2 = Candidate()

        # Make a copy of the parent genes.
        child1.values = numpy.copy(parent1.values)
        child2.values = numpy.copy(parent2.values)

        r = random.uniform(0, 1.1)
        while r > 1:  # Outside [0, 1] boundary. Choose another.
            r = random.uniform(0, 1.1)

        # Perform crossover.
        if r < crossover_rate:
            # Pick a crossover point. Crossover must have at least 1 row (and at most NUMBER_DIGITS-1) rows.
            crossover_point1 = random.randint(0, 8)
            crossover_point2 = random.randint(1, 9)
            while crossover_point1 == crossover_point2:
                crossover_point1 = random.randint(0, 8)
                crossover_point2 = random.randint(1, 9)

            if crossover_point1 > crossover_point2:
                temp = crossover_point1
                crossover_point1 = crossover_point2
                crossover_point2 = temp

            for i in range(crossover_point1, crossover_point2):
                child1.values[i], child2.values[i] = self.crossover_rows(child1.values[i], child2.values[i])

        return child1, child2

    def crossover_rows(self, row1, row2):
        child_row1 = numpy.zeros(NUMBER_DIGITS)
        child_row2 = numpy.zeros(NUMBER_DIGITS)

        remaining = list(range(1, NUMBER_DIGITS + 1))
        cycle = 0

        while (0 in child_row1) and (0 in child_row2):  # While child rows not complete...
            if cycle % 2 == 0:  # Even cycles.
                # Assign next unused value.
                index = self.find_unused(row1, remaining)
                start = row1[index]
                remaining.remove(row1[index])
                child_row1[index] = row1[index]
                child_row2[index] = row2[index]
                next = row2[index]

                while next != start:  # While cycle not done...
                    index = self.find_value(row1, next)
                    child_row1[index] = row1[index]
                    remaining.remove(row1[index])
                    child_row2[index] = row2[index]
                    next = row2[index]

                cycle += 1

            else:  # Odd cycle - flip values.
                index = self.find_unused(row1, remaining)
                start = row1[index]
                remaining.remove(row1[index])
                child_row1[index] = row2[index]
                child_row2[index] = row1[index]
                next = row2[index]

                while next != start:  # While cycle not done...
                    index = self.find_value(row1, next)
                    child_row1[index] = row2[index]
                    remaining.remove(row1[index])
                    child_row2[index] = row1[index]
                    next = row2[index]

                cycle += 1

        return child_row1, child_row2

    @staticmethod
    def find_unused(parent_row, remaining):
        for i in range(0, len(parent_row)):
            if parent_row[i] in remaining:
                return i

    @staticmethod
    def find_value(parent_row, value):
        for i in range(0, len(parent_row)):
            if parent_row[i] == value:
                return i


class Sudoku:
    """ Solves a given Sudoku puzzle using a genetic algorithm. """

    def __init__(self, number_of_candidates, number_of_elites, number_of_generations, number_of_mutations,
                 selection_rate):
        self.nc = number_of_candidates
        self.ne = number_of_elites
        self.ng = number_of_generations
        self.nm = number_of_mutations
        self.sr = selection_rate

        self.given = None
        self.population = None

    def load(self, path):
        # Load a configuration to solve.
        with open(path, 'r') as f:
            values = numpy.loadtxt(f).reshape((NUMBER_DIGITS, NUMBER_DIGITS)).astype(int)
            self.given = Given(values)

    @staticmethod
    def save(path, solution):
        # Save a configuration to a file.
        with open(path, 'w') as f:
            numpy.savetxt(f, solution.values.reshape(NUMBER_DIGITS * NUMBER_DIGITS), fmt='%d')

    def solve(self):
        # Mutation parameters
        phi = 0
        sigma = 1
        mutation_rate = 0.06

        # Create an initial population.
        self.population = Population()
        self.population.seed(self.nc, self.given)

        stale = 0
        for generation in range(0, self.ng):
            print(f'Generation {generation}')

            # Check for a solution.
            best_fitness = 0.0

            for c in range(0, self.nc):
                fitness = self.population.candidates[c].fitness
                if fitness == 1:
                    print(f'Solution found at generation {generation}!')
                    print(self.population.candidates[c].values)
                    return self.population.candidates[c]

                # Find the best fitness.
                if fitness > best_fitness:
                    best_fitness = fitness

            print(f'Best fitness: {best_fitness}')

            # Create the next population.
            next_population = []

            # Select elites (the fittest candidates) and preserve them for the next generation.
            self.population.sort()
            elites = []
            for e in range(0, self.ne):
                elite = Candidate()
                elite.values = numpy.copy(self.population.candidates[e].values)
                elites.append(elite)

            # Create the rest of the candidates.
            for count in range(self.ne, self.nc, 2):
                # Select parents from population via a tournament.
                t = Tournament(self.sr)
                parent1 = t.compete(self.population.candidates)
                parent2 = t.compete(self.population.candidates)

                # Cross-over.
                cc = CycleCrossover()
                child1, child2 = cc.crossover(parent1, parent2, crossover_rate=1.0)

                # Mutate child1.
                old_fitness = child1.fitness
                success = child1.mutate(mutation_rate, self.given)
                child1.update_fitness()
                if success:
                    self.nm += 1
                    if child1.fitness > old_fitness:  # Used to calculate the relative success rate of mutations.
                        phi = phi + 1

                # Mutate child2.
                old_fitness = child2.fitness
                success = child2.mutate(mutation_rate, self.given)
                child2.update_fitness()
                if success:
                    self.nm += 1
                    if child2.fitness > old_fitness:  # Used to calculate the relative success rate of mutations.
                        phi = phi + 1

                # Add children to new population.
                next_population.append(child1)
                next_population.append(child2)

            # Append elites onto the end of the population. These will not have been affected by crossover or mutation.
            for e in range(0, self.ne):
                next_population.append(elites[e])

            # Select next generation.
            self.population.candidates = next_population
            self.population.update_fitness()

            # Calculate new adaptive mutation rate (based on Rechenberg's 1/5 success rule).
            # This is to stop too much mutation as the fitness progresses towards unity.
            if self.nm == 0:
                phi = 0  # Avoid divide by zero.
            else:
                phi = phi / self.nm

            if phi > 0.2:
                sigma = sigma / 0.998
            elif phi < 0.2:
                sigma = sigma * 0.998

            mutation_rate = abs(numpy.random.normal(loc=0.0, scale=sigma, size=None))
            self.nm = 0
            phi = 0

            # Check for stale population.
            self.population.sort()
            if self.population.candidates[0].fitness != self.population.candidates[1].fitness:
                stale = 0
            else:
                stale += 1

            # Re-seed the population if 100 generations have passed with the fittest two candidates always
            # having the same fitness.
            if stale >= 100:
                print('The population has gone stale. Re-seeding...')
                self.population.seed(self.nc, self.given)
                stale = 0
                sigma = 1
                phi = 0
                self.nm = 0
                mutation_rate = 0.06

        print('No solution found.')
        return None