import haversine

def find_nearest_node(current_lat, current_lon, nodes_data):
    
    min_distance = float("inf") # 初期値を無限にする
    nearest_node_id = None # 一番近いnodeの名前を返すため
    
    # すべてのノードとの距離を測る
    # データ数が少ないため計算量はおおきくならない 
    for name in nodes_data:
        
        node_lat = nodes_data[name]["lat"]
        node_lon = nodes_data[name]["lon"]
        
        # haversineで2点間の距離を測る
        distance = haversine((current_lat, current_lon), (node_lat, node_lon))
        
        if distance < min_distance:
            min_distance = distance
            nearest_node_id = name
            
    
    return nearest_node_id # nodeの名前を返す
        
        