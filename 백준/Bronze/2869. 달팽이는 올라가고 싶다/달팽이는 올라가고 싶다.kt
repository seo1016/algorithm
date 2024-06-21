import java.util.Scanner

fun main() = with(Scanner(System.`in`)) {
    val A = nextInt()
    val B = nextInt()
    val V = nextInt()

    print(if((V-A) % (A-B) == 0) (V-A) / (A-B) + 1 else (V-A) / (A-B) + 2)
}