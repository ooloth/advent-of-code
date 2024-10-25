export type Year =
  | 2015
  | 2016
  | 2017
  | 2018
  | 2019
  | 2020
  | 2021
  | 2022
  | 2023
  | 2024

export type Day =
  | 1
  | 2
  | 3
  | 4
  | 5
  | 6
  | 7
  | 8
  | 9
  | 10
  | 11
  | 12
  | 13
  | 14
  | 15
  | 16
  | 17
  | 18
  | 19
  | 20
  | 21
  | 22
  | 23
  | 24
  | 25

export type Part = 1 | 2

// TODO: use zod for parsing instead?
function parseYear(year: string): Year {
  const yearAsInteger = parseInt(year, 10)

  if (isNaN(yearAsInteger)) {
    throw new Error(`Year must be an integer (got "${year}")`)
  }

  if (yearAsInteger < 2015 || yearAsInteger > 2024) {
    throw new Error(`Year must be between 2015 and 2024 (got "${yearAsInteger}")`)
  }

  return yearAsInteger as Year
}

function parseDay(day: string): Day {
  const dayAsInteger = parseInt(day, 10)

  if (isNaN(dayAsInteger)) {
    throw new Error(`Day must be an integer (got "${day}")`)
  }

  if (dayAsInteger < 1 || dayAsInteger > 25) {
    throw new Error(`Day must be between 1 and 25 (got "${dayAsInteger}")`)
  }

  return dayAsInteger as Day
}

function parsePart(part: string): Part {
  const partAsInteger = parseInt(part, 10)

  if (isNaN(partAsInteger)) {
    throw new Error(`Part must be an integer (got "${part}")`)
  }

  if (![1, 2].includes(partAsInteger)) {
    throw new Error(`Part must be 1 or 2 (got "${partAsInteger}")`)
  }

  return partAsInteger as Part
}

/**
 * See: https://docs.deno.com/examples/command-line-arguments/
 */
export function parseSolveCliArgs() {
  const [year, day, part] = Deno.args[0].split('-')

  return {
    year: parseYear(year),
    day: parseDay(day),
    part: parsePart(part),
    submit: ['-s', '--submit'].includes(Deno.args[1]),
  }
}
