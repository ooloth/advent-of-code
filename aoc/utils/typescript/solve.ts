import { type Day, parseSolveCliArgs, type Part, type Year } from './cli.ts'
import { readInputForDay } from './inputs.ts'

type Input = string[]
type Answer = number | null
type Example = [Input, number]

async function get_solution_function(year: Year, day: Day, part: Part): Promise<(x: string[]) => Answer> {
  const modulePath = `${Deno.cwd()}/aoc/${year}/typescript/${day}${part === 1 ? 'a' : 'b'}.ts`
  console.log('modulePath', modulePath)
  const module = await import(modulePath)
  console.log('module', module)
  return module.solution
}

async function get_answer(year: Year, day: Day, part: Part): Promise<Answer> {
  const solution = await get_solution_function(year, day, part)
  console.log('solution function:', solution)

  const input = readInputForDay(year, day)
  console.log('input:', input)

  return solution(input)
}

function isAnswerAnInteger(answer: Answer): boolean {
  return typeof answer === 'number' && Number.isInteger(answer)
}

function printAnswer(answer: Answer): void {
  if (!isAnswerAnInteger(answer)) {
    console.log('🤔 Solution is not an integer. Have you solved this puzzle?')
  }

  console.log(`🔍 Answer: ${answer}`)
}

/**
 * See: https://docs.deno.com/api/deno/~/Deno.Command
 */
function submitAnswer(year: Year, day: Day, part: Part, answer: Answer) {
  if (!isAnswerAnInteger(answer)) {
    console.log('🤔 Solution is not an integer. Have you solved this puzzle?')
    console.log(`🔍 Answer: ${answer}`)
    return
  }

  console.log('Submitting answer...')

  const aocSessionCookieFile = `${Deno.cwd()}/.aoc-session-cookie`

  // see: https://github.com/scarvalhojr/aoc-cli?tab=readme-ov-file#usage-%EF%B8%8F
  const command = new Deno.Command(Deno.execPath(), {
    args: `aoc s -y ${year} -d ${day} -s ${aocSessionCookieFile} ${part} ${answer}`.split(' '),
  })

  command.outputSync()
  // const { code, stdout, stderr } = command.outputSync()
}

if (import.meta.main) {
  console.log('Running TypeScript solution')

  const args = parseSolveCliArgs()
  console.log('args:', args)

  const answer = await get_answer(args.year, args.day, args.part)
  console.log('answer:', answer)

  if (args.submit) {
    submitAnswer(args.year, args.day, args.part, answer)
  } else {
    printAnswer(answer)
  }
}
