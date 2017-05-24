def print_paths(predecessor):
    paths = {}
    for v in predecessor:
        paths[v] = ""
        p = predecessor[v]
        while p is not None:
            paths[v] += "<-"+p
            p = predecessor[p]
    for v, path in paths.items():
        print(v+":"+path)
