import java.lang.Integer.max
import java.util.*
import java.util.ArrayDeque
import kotlin.collections.*

fun bfs(queue: ArrayDeque<IntArray>, graph: Array<Array<IntArray>>, n: Int, m: Int, h: Int) {
    val dx = intArrayOf(0, 0, 0, 0, 1, -1)
    val dy = intArrayOf(0, 0, 1, -1, 0, 0)
    val dz = intArrayOf(1, -1, 0, 0, 0, 0)

    while(queue.isNotEmpty()) {
        val(x, y, z) = queue.removeFirst()
        for(i in 0 until 6) {
            val nx = x + dx[i]
            val ny = y + dy[i]
            val nz = z + dz[i]

            if(nx < 0 || nx >= h || ny < 0 || ny >= n || nz < 0 || nz >= m) {
                continue
            }
            if(graph[nx][ny][nz] == 0) {
                graph[nx][ny][nz] = graph[x][y][z] + 1
                queue.add(intArrayOf(nx, ny, nz))
            }
        }
    }
}

fun findStart(n: Int, m: Int, h: Int, graph: Array<Array<IntArray>>, queue: ArrayDeque<IntArray>) {
    for(i in 0 until h) {
        for(j in 0 until n) {
            for(k in 0 until m) {
                if(graph[i][j][k] == 1) {
                    queue.add(intArrayOf(i, j, k))
                }
            }
        }
    }

    bfs(queue, graph, n, m, h)

    var cnt = -1
    for(i in 0 until h) {
        for(j in 0 until n) {
            for(k in 0 until m) {
                if(graph[i][j][k] == 0) {
                    print(-1)
                    return
                }
                cnt = max(cnt, graph[i][j][k])
            }
        }
    }

    if(cnt == 1) {
        print(0)
        return
    } else {
        print(cnt-1)
        return
    }
}


fun main(args: Array<String>) {
    val (m, n, h) = readLine()!!.split(" ").map { it.toInt() }
    val graph = Array(h){Array(n) { IntArray(m) } }
    val queue = ArrayDeque<IntArray>()

    for(i in 0 until h) {
        for(j in 0 until n) {
            val aa = readLine()!!.split(" ").map { it.toInt() }
            graph[i][j] = aa.toIntArray()
        }
    }

    findStart(n, m, h, graph, queue)
}
