// you can also use imports, for example:
// import kotlin.math.*

// you can write to stdout for debugging purposes, e.g.
// println("this is a debug message")

fun solution(A: Int, B: Int, K: Int): Int {
    var front = A / K
    var back = B / K

    var ans = back - front
    if(A % K == 0) {
        ans += 1
    }

    return ans
}
