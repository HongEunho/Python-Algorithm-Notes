fun main(args: Array<String>) {
    val n = readLine()!!.toInt()

    val dp = Array(101) { IntArray(10) }
    dp[1][0] = 0
    for(i in 1 until 10) {
        dp[1][i] = 1
    }

    for(i in 2 until n+1) {
        for(j in 0 until 10) {
            when(j) {
                0 -> dp[i][j] = dp[i-1][1]
                9 -> dp[i][j] = dp[i-1][8]
                else -> dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1]) % 1000000000
            }
        }
    }

    var ans = 0L
    dp[n].forEach { ans += it }
    print(ans%1000000000)

}
