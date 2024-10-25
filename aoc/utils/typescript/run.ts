import { type Day, parseSolveCliArgs, type Part, type Year } from './cli.ts'
import { readInputForDay } from './inputs.ts'

export type Input = string[]
export type Answer = number | null
export type Example = [Input, number]

async function get_solution_function(year: Year, day: Day, part: Part): Promise<(x: string[]) => Answer> {
  const modulePath = `${Deno.cwd()}/aoc/${year}/typescript/${day}${part}.ts`
  const module = await import(modulePath)
  return module.solution
}

export async function get_answer(year: Year, day: Day, part: Part): Promise<Answer> {
  const solution = await get_solution_function(year, day, part)
  const input = readInputForDay(year, day)

  return solution(input)
}

export function isInteger(answer: Answer): boolean {
  return typeof answer === 'number' && Number.isInteger(answer)
}

function printAnswer(answer: Answer): void {
  if (!isInteger(answer)) {
    console.log('🤔 Solution is not an integer. Have you solved this puzzle?')
  }

  console.log(`🔍 Answer: ${answer}`)
}

async function main() {
  const args = parseSolveCliArgs()
  const answer = await get_answer(args.year, args.day, args.part)

  printAnswer(answer)
}

if (import.meta.main) {
  await main()
}
