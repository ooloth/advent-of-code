import { type Day, type Year } from './cli.ts'

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
