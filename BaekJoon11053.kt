import kotlin.collections.*
import kotlin.math.max
fun main(args: Array<String>) {
    val n = readLine()!!.toInt()
    val list = readLine()!!.split(" ").map { it.toInt() }

    val dp = Array(1001){1}
    dp[0] = 1

    for(i in 1 until n) {
        for(j in 0 until i) {
            if(list[i] > list[j]) {
                dp[i] = max(dp[i], dp[j] + 1)
            }
        }
    }

    println(dp.maxOrNull())
}
