        def fn(x): 
            """Return Eulerian path via dfs."""
            while graph[x]: fn(graph[x].pop()) 
            ans.append(x)