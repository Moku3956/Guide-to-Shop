from haversine import haversine
import graph_data


def find_nearest_node(current_lat, current_lon, nodes_data, current_nodes_data):

    min_distance = float("inf")  # 初期値を無限にする
    nearest_node_id = None  # 一番近いnodeの名前を返すため

    # すべてのノードとの距離を測る
    # 全探索ではあるがデータ数が少ないため計算量はおおきくならない

    if current_nodes_data:
        for name in current_nodes_data:
            node_lat = nodes_data[name]["lat"]
            node_lon = nodes_data[name]["lon"]

        # haversineで2点間の距離を測る
            distance = haversine((current_lat, current_lon), (node_lat, node_lon))

            if distance < min_distance:
                min_distance = distance
                nearest_node_id = name
                
    else:
        for name in nodes_data:
    
            node_lat = nodes_data[name]["lat"]
            node_lon = nodes_data[name]["lon"]
    
            # haversineで2点間の距離を測る
            distance = haversine((current_lat, current_lon), (node_lat, node_lon))
    
            if distance < min_distance:
                min_distance = distance
                nearest_node_id = name

    if min_distance > 0.3:  # haversineのデフォルト単位はkmなので、300mを0.3に
        nearest_node_id = "main_gate"
    return nearest_node_id  # nodeの名前を返す


def designed_route(node_name):
    route = [node_name]  # 現在地からの最短ノードは最初に保存
    # dictinaryをリンクリストのようにたどり、ノードの名前をreturn
    while graph_data.edges[node_name] != "goal":
        route.append(graph_data.edges[node_name])
        node_name = graph_data.edges[node_name]
    return route
