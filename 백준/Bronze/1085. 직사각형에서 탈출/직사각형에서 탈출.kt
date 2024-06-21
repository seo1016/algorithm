import java.util.Scanner

fun main() = with(Scanner(System.`in`)){
    val x = nextInt()
    val y = nextInt()
    val w = nextInt()
    val h = nextInt()

    val arr = arrayOf(w-x, h-y, x, y, w, h)
    println(arr.min())
}