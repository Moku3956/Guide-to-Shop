from haversine import haversine
import graph_data


def find_nearest_node(current_lat, current_lon, nodes_data, current_nodes_data):

    min_distance = float("inf")
    nearest_node_id = None
    
    # 最初の経路から50m離れたときにつかう
    REROUTE_THRESHOLD_KM = 0.05 
    
    # デフォルトは全探索しない
    needs_full_scan = False

    # 経路がすでにある場合
    if current_nodes_data:
        # まずは現在の経路（current_nodes_data）の上だけを探す
        for name in current_nodes_data:
            node_lat = nodes_data[name]["lat"]
            node_lon = nodes_data[name]["lon"]
            distance = haversine((current_lat, current_lon), (node_lat, node_lon))

            if distance < min_distance:
                min_distance = distance
                nearest_node_id = name

        # もし経路上の最短ノードでも50m以上離れていたら、全探索フラグを立てる
        if min_distance >= REROUTE_THRESHOLD_KM:
            needs_full_scan = True
    
    else:
        # 全探索フラグを立てる
        needs_full_scan = True

    # 全探索フラグがTrueのとき
    if needs_full_scan:
        for name in nodes_data:
            node_lat = nodes_data[name]["lat"]
            node_lon = nodes_data[name]["lon"]
            distance = haversine((current_lat, current_lon), (node_lat, node_lon))

            # (引き継いだ min_distance よりも近いノードが見つかれば更新)
            if distance < min_distance:
                min_distance = distance
                nearest_node_id = name

    # キャンパスから300m以上遠いとき
    if min_distance > 0.3:  # 300m
        nearest_node_id = "main_gate"
        
    return nearest_node_id  # nodeの名前を返す


def designed_route(node_name):
    route = [node_name]  # 現在地からの最短ノードは最初に保存
    # dictinaryをリンクリストのようにたどり、ノードの名前リストをreturn
    while graph_data.edges[node_name] != "goal":
        route.append(graph_data.edges[node_name])
        node_name = graph_data.edges[node_name]
    return route
