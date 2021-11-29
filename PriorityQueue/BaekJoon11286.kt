import java.util.*

fun main(args: Array<String>) {
    val n = readLine()!!.toInt()
    val lambda = { a: Int, b: Int -> when{
        a > b -> 1
        a < b -> -1
        else -> 0
    }}

    val pq = PriorityQueue{a:Pair<Int, Int>, b: Pair<Int, Int> ->
        when{
            a.first != b.first -> lambda(a.first, b.first)
            else -> lambda(a.second, b.second)
        }
    }

    for(i in 0 until n) {
        val x = readLine()!!.toInt()
        if (x != 0) {
            pq.add(Pair(abs(x), x))
        } else {
            val a = pq.poll() ?: Pair(0, 0)
            println(a.second)
        }
        print(pq)
    }
}
