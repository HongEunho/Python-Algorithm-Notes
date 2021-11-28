fun main(args: Array<String>) {
    val n = readLine()!!.toInt()
    val list = readLine()!!.split(" ").map { it.toInt() }

    val upDp = Array(1001){1}
    val downDp = Array(1001){1}

    for(i in 1 until n) {
        for(j in 0 until i) {
            if(list[i] > list[j]) {
                upDp[i] = max(upDp[i], upDp[j] + 1)
            }
        }

    }

    for(i in n-2 downTo 0) {
        for(j in n-1 downTo i+1) {
            if(list[i] > list[j]) {
                downDp[i] = max(downDp[i], downDp[j] + 1)
            }
        }
    }

    var max = 0
    for(i in 0 until n) {
       if(upDp[i] + downDp[i] > max) {
           max = upDp[i] + downDp[i]
       }
    }

    print(max-1)
}
