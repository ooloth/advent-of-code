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

/**
 * See: https://docs.deno.com/examples/command-line-arguments/
 */
export function parseSolveCliArgs() {
  const year = Deno.args[0]
  const day = Deno.args[1]
  const part = Deno.args[2]

  return {
    year: parseInt(year) as Year,
    day: parseInt(day) as Day,
    part: part as Part,
  }
}

/**
 * See: https://docs.deno.com/examples/command-line-arguments/
 */
export function parsePuzzleInputFromCliArg(): string {
  return Deno.args[0]
}
