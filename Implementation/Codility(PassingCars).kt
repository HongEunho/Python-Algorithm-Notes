fun solution(A: IntArray): Int {

    var cnt = 0
    var answer = 0
    for(i in A.size-1 downTo 0) {
        if(A[i]==1) {
            cnt += 1
        } else {
            answer += cnt
        }
    }
    if(answer > 1000000000)
        return -1
    return answer
}
