
# sub-nodeはより細かく計算できるようにするため
# "": {"name": "", "lat": , "lon": },
# ("", ""),

nodes = {
    "main_gate": {"name": "正門", "lat": 34.984973, "lon": 135.960512},
    "canopy": {"name": "キャノピー前", "lat": 34.982625, "lon": 135.963138 },
    "cafeteria": {"name": "食堂前", "lat": 34.981874, "lon": 135.963103}, 
    "central": {"name": "セントラルアーク前", "lat": 34.981714, "lon": 135.963098},
    "betwen_across_and_prison": {"name": "アクロスプリズム間", "lat": 34.980991, "lon": 135.962146},
    "adoseminario": {"name": "アドセミ前", "lat": 34.980770, "lon": 135.962111},
    "colearning_main": {"name": "コラーニングメイン入口前", "lat": 34.980336, "lon": 135.962599},
    "destination": {"name": "目的地", "lat": 34.980316, "lon": 135.963133},
    "links": {"name": "リンクス前", "lat": 34.980312, "lon": 135.963573},
    "prisom_right": {"name": "プリズム右", "lat": 34.981408, "lon": 135.963608},
    "fountain": {"name": "噴水前", "lat": 34.981953, "lon": 135.963417},
    "headquarter": {"name": "本部前", "lat": 34.981767, "lon": 135.963621},
    "fountain_right": {"name": "噴水", "lat": 34.982052, "lon": 135.963766},
    "fountain_left1": {"name": "噴水左1", "lat": 34.982191, "lon": 135.963358},  
    "fountain_left2": {"name": "噴水左2", "lat": 34.981815, "lon": 135.963230},
    "core": {"name": "コアステ", "lat": 34.982302, "lon": 135.964053},
    "library": {"name": "図書館前", "lat": 34.982568, "lon": 135.964359},
    "rotary": {"name": "ロータリー前", "lat": 34.982850, "lon": 135.964557},
    "lorm": {"name": "ローム記念館", "lat": 34.984572, "lon": 135.964592},
    "sub_gate": {"name": "サブ門", "lat": 34.986875, "lon": 135.963063},
    "bus_stop": {"name": "バス停前", "lat": 34.982665, "lon": 135.962505},
    "under_bus_stop": {"name": "バス停下", "lat": 34.982472, "lon": 135.962521},
    "across_back_door": {"name": "アクロス裏口", "lat": 34.981850, "lon": 135.961848},
    "across": {"name": "アクロス前", "lat": 34.981490, "lon": 135.962242},
    "larcadia_back_door": {"name": "ラルカディア裏口", "lat": 34.981072, "lon": 135.961011},
    "larcadia": {"name": "ラルカディア", "lat": 34.980716, "lon": 135.961432},
    "adoseminario_left": {"name": "アドセミ左", "lat": 34.981010, "lon": 135.961829},
    "ground": {"name": "グラウンド前", "lat": 34.978622, "lon": 135.963535},
    "convinience": {"name": "生協コンビニ前", "lat": 34.981848, "lon": 135.962739},
    "sub1": {"name": "補助点1", "lat": 34.982069, "lon": 135.962151},
    "sub2": {"name": "補助点2", "lat": 34.982448, "lon": 135.963122},
    "sub3": {"name": "補助点3", "lat": 34.982615, "lon": 135.964622},
    "sub4": {"name": "補助点4", "lat": 34.982136, "lon": 135.963114},
    "sub5": {"name": "補助点5", "lat": 34.981501, "lon": 135.962814},
    "sub6": {"name": "補助点6", "lat": 34.981503, "lon": 135.963313},
    "sub7": {"name": "補助点7", "lat": 34.981441, "lon": 135.963074},
    "sub24": {"name": "補助点24", "lat": 34.981283, "lon": 135.963074},
    "sub8": {"name": "補助点8", "lat": 34.981316, "lon": 135.962564},
    "sub9": {"name": "補助点9", "lat": 34.980901, "lon": 135.961234},
    "sub10": {"name": "補助点10", "lat": 34.981125, "lon": 135.962323},
    "sub11": {"name": "補助点11", "lat": 34.981092, "lon": 135.962819},
    "sub12": {"name": "補助点12", "lat": 34.981136, "lon": 135.963597},
    "sub13": {"name": "補助点13", "lat": 34.980940, "lon": 135.963058},
    "sub14": {"name": "補助点14", "lat": 34.980883, "lon": 135.963589},
    "sub15": {"name": "補助点15", "lat": 34.980604, "lon": 135.962296},
    "sub16": {"name": "補助点16", "lat": 34.980520, "lon": 135.963581},
    "sub17": {"name": "補助点17", "lat": 34.980329, "lon": 135.962819},
    "sub18": {"name": "補助点18", "lat": 34.980077, "lon": 135.963557},
    "sub19": {"name": "補助点19", "lat": 34.979857, "lon": 135.963551},
    "sub20": {"name": "補助点20", "lat": 34.979558, "lon": 135.963546},
    "sub21": {"name": "補助点21", "lat": 34.979238, "lon": 135.963530},
    "sub22": {"name": "補助点22", "lat": 34.979040, "lon": 135.963525},
    "sub23": {"name": "補助点23", "lat": 34.978776, "lon": 135.963514},
}    


# 道順を指定する
# メインとなる道は２つ
# メインではない経路(枝)はメインに接続できるようにする

edges = dict([
    #
    # 正門から目的地まで(メイン1) ↓
    #
    ("main_gate", "canopy"),
    ("canopy", "sub2"),
    ("sub2", "sub4"),   
    ("sub4", "cafeteria"),   
    ("cafeteria", "central"),
    ("central", "sub5"),   
    ("sub5", "sub8"),   
    ("sub8", "sub10"),   
    ("sub10", "betwen_across_and_prison"),   
    ("betwen_across_and_prison", "adoseminario"),   
    ("adoseminario", "sub15"),   
    ("sub15", "colearning_main"),   
    ("colearning_main", "sub17"),   
    ("sub17", "destination"), 
    ("destination", "goal"),
    # メイン１の経路の枝  
    ("fountain_left2", "central"),   #メインに接続
    ("bus_stop", "canopy"),   #メインに接続
    ("under_bus_stop", "sub1"),   
    ("sub1", "across_back_door"),   
    ("across_back_door", "across"),   
    ("across", "sub10"),   #メインに接続
    ("convinience", "across"), #直前の("across", "sub10")に接続
    ("larcadia_back_door", "sub9"),   
    ("sub9", "larcadia"),   
    ("larcadia", "adoseminario_left"),    
    ("adoseminario_left", "adoseminario"),    #メインに接続
    ("sub11", "sub8"),  #メインに接続
    ("sub7", "central"),
    #
    # サブ門から店舗まで(メイン２) ↓
    #
    ("sub_gate", "lorm"),       
    ("lorm", "rotary"),   
    ("rotary", "sub3"),         
    ("sub3", "core"),   
    ("core", "library"),    
    ("library", "headquarter"),     
    ("headquarter", "prisom_right"),   
    ("prisom_right", "sub12"),   
    ("sub12", "sub14"),   
    ("sub14", "sub16"),   
    ("sub16", "links"),   
    ("links", "destination"),   
    ("destination", "goal"),
    # メイン２の経路の枝
    ("fountain_left1", "fountain"),   
    ("fountain", "headquarter"),   #メインに接続
    ("sub6", "prisom_right"),   #メインに接続
    ("ground", "sub23"),   
    ("sub23", "sub22"),   
    ("sub22", "sub21"),   
    ("sub21", "sub20"),   
    ("sub20", "sub19"),   
    ("sub19", "sub18"),    
    ("sub18", "links"),    #メインに接続
    ("sub24", "sub13"),
    ("sub13", "sub14"),    #メインに接続  
])