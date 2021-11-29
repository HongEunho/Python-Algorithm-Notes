import java.util.*

fun main(args: Array<String>) {
    val n = readLine()!!.toInt()
    val pq = PriorityQueue<Int>()

    for(i in 0 until n) {
        val x = readLine()!!.toInt()
        if (x > 0) {
            pq.add(x)
        } else {
            val a = pq.poll() ?: 0
            println(a)
        }
    }
}
