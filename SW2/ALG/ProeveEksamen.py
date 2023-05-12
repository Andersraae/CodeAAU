# 1.1 - d

# 1.2 - ingen

# 1.3 - a

# 1.4 - a, e

# 2.1 a Linear Probing - (20 + 0) mod 8 = 4 ... 4, 5, 6, 2, 1, 3, 6???, 7???

# 2.1 b Quadratic Probing - (20 + 2*0 + 3*0^2) mod 8 = 4 ... 4, 1, 4, 0, 5, 3, 0???, 1??? 

# 2.1 c (Eller faktisk b igen?) Double Hasing - (20 + 0 * (2*20)) mod 8 = 4 ... 4, 4, 4, 1, 5, 2, 0???, 0???
k = 0
i = 7
print((k + i * (2*k)) % 8)

# 2.2 - b

# 2.3 a - O(1)

# 2.3 b - O(n)

# 2.3 c -  
#   T(1) = 1 (constant time?)
#   a = 2 (subproblems)
#   n/b = n/2 size of each sub problem
#   f(n) = n
#   T(n) = 2*T(n/2) + n

# 2.3 d -
#   f(n) = Theta(n^(logb(a))) = Theta(n^(log2(2))) = Theta(n)
#   Therefore T(n) = Theta(n * log n)

# 2.4 a - 
    # Singly-to-Doubly-LL(List):
    #     L.head.prev = nil
    #     thisElement = l.head
    #     nextElement = L.head.next
    #     for List.length - 1:
    #         if nextElement != nil:
    #             nextElement.prev = thisElement
    #             thisElement = nextElement
    #             nextElement = nextElement.next
    #   return List
    
# 2.4 b -
#   line 2, 3, 4 = O(1)
#   line 5, 6, 7, 8, 9 = O(n)
#   line 10 = O(1)
#   runtime = O(n) 

# 3.1 -
#   I choose clue/graph-composer as root
#   I will write start and finish times as a/b where a is start and b is finish
#   clue/graph-composer 1/?, graphp/graphiz: v0.2.1 2/?, graphp/algoritms: v0.8.1 3/?, 
#   php 4/5, graphp/algoritms: v0.8.1 3/6, clue/graph: v0.9.0 7/8,
#   graphp/graphiz: v0.2.1 2/9, jms/composer-deps-analyzer: 0.1.0 10/11,
#   symfony/console: v2.2.1 12/13, clue/graph-composer 1/14
#
#   Linked list:
#   [clue/graph-composer > (graphp/graphiz, jms/composer-deps-analyzer, symfony/console),
#   graphp/graphiz > (graphp/algoritms, clue/graph, php),
#   graphp/algoritms > (php, clue/graph),
#   clue/graph > (php),
#   jms/composer-deps-analyzer > (php),
#   symfony/console > (php),
#   php > ()]

# 3.2 -
#   If you run topological sort on H with whatever php points to
#   is as the root of H, you get a topologically sorted linked
#   list of H. From here you can set php.next to be the root
#   of H. H and G are then one linked list. This will only work
#   if G is compiled first as the tail of G will be the only
#   node pointing to H and nothing from H points to G.

# 4.1 - 
#   Belleman-Ford would return false as there is a negative cycle
#   Dijstra's would not work as there is a negative edge
#   DAG would not work as there is a cycle

# 4.2 -
#   There are an infinite number of routes between 6 and 2, as
#   you could keep charging. One example of a route is {6, 4, 5, 2}
#   Same goes for 6 to 3. An example is {6, 4, 5, 1, 1, 1, 1, 1, 1, 5, 4, 3}

# 4.3 -
#   In this specific example you could make a check that if you
#   reach 100 after the first move. The edge where it happened
#   is restricted as you would be able to move whereever you 
#   want from there. This would require line 1 in relax to
#   make this check. Pseudo code:
#
#   Bellman-Ford(G, w, s):
#       Initialize-Single-Source(G, s)
#       for i = 1 to |G.V| - 1:
#           for each edge (u, v) in G.E:
#               Relax(u, v, w)
#
#   Relax(u, v, w):
#       if (v.d > u.d + w(u, v)) && (u.d + w(u, v) <= 0)
#           c.d = u.d + w(u, v)
#           v.pi = u