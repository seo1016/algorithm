import java.util.Scanner

fun main() = with(Scanner(System.`in`)) {
    val x = nextInt()
    var summ = 1
    var tmp = 0

    while(tmp < x) {
        tmp += summ
        summ++
    }

    if(summ%2 == 0) {
        val molecule = (tmp - x + 1)
        val denominator = summ - molecule
        println("$molecule/$denominator")
    }

    else {
        val denominator = (tmp - x + 1)
        val molecule = summ - denominator
        println("$molecule/$denominator")
    }
}