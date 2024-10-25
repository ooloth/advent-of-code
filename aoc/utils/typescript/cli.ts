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

export type Part = 'a' | 'b'

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
  if (!['a', 'b'].includes(part)) {
    throw new Error(`Part must be "a" or "b" (got "${part}")`)
  }

  return part as Part
}

function getDefaultYear(): Year {
  const now = new Date()
  const currentYear = now.getFullYear()
  const currentMonth = now.getMonth()
  const mostRecentAocYear = currentMonth === 12 ? currentYear : currentYear - 1

  return mostRecentAocYear as Year
}

function getActiveYear(): Year {
  const explicitYear = Deno.env.get('AOC_YEAR')
  const defaultYear = getDefaultYear()
  const activeYear = explicitYear ? parseYear(explicitYear) : defaultYear

  return activeYear
}

/**
 * See: https://docs.deno.com/examples/command-line-arguments/
 */
export function parseSolveCliArgs() {
  // Assume the last character represents the part (a or b) and everything before it represents the day (1-25)
  const arg = Deno.args[0]
  const day = arg.slice(0, -1) // All characters before the last one
  const part = arg.slice(-1) // The last character

  return {
    year: getActiveYear(),
    day: parseDay(day),
    part: parsePart(part),
  }
}
