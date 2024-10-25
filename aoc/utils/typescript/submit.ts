import { type Day, parseSolveCliArgs, type Part, type Year } from './cli.ts'
import { type Answer, get_answer, isInteger } from './run.ts'

/**
 * See: https://docs.deno.com/api/deno/~/Deno.Command
 */
function submitAnswer(year: Year, day: Day, part: Part, answer: Answer) {
  if (!isInteger(answer)) {
    console.log('🤔 Solution is not an integer. Aborting.')
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

async function main() {
  const args = parseSolveCliArgs()
  const answer = await get_answer(args.year, args.day, args.part)

  submitAnswer(args.year, args.day, args.part, answer)
}

if (import.meta.main) {
  await main()
}
