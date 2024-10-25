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

/**
 * Gets the input for the day from a local file and returns it as a list of strings.
 * Any trailing characters (e.g. newlines) are stripped from each line.
 * see: https://docs.deno.com/examples/reading-files/
 */
export function readInputForDay(year: Year, day: Day): string[] {
  const input_file = `${Deno.cwd()}/aoc/${year}/inputs/${day}.txt`

  const text = Deno.readTextFileSync(input_file)
  const lines = text.split('\n').map((line) => line.trimEnd())

  return lines
}

if (import.meta.main) {
  const lines = readInputForDay(2015, 2)
}
