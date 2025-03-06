from graphviz import Digraph
from groups import groups  # 別ファイルからグループデータをインポート

def initialize_dot():
    """Digraphオブジェクトを初期化して返す"""
    dot = Digraph(format="png")  # PDFからPNGに変更
    dot.attr(rankdir="LR", nodesep="0.3", ranksep="0.5", splines="polyline",
             fontsize="16", style="filled", fillcolor="white", fontname="Helvetica Neue")
    return dot

def lighten_color(hex_color, factor=0.2):
    """指定された色を少し薄くする"""
    hex_color = hex_color.lstrip('#')
    rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    lighter_rgb = tuple(min(255, int(c + (255 - c) * factor)) for c in rgb)
    return '#{:02X}{:02X}{:02X}'.format(*lighter_rgb)

def create_subgraph(dot, name, screens, prefix, color, transitions):
    """グループごとのサブグラフを作成し、カテゴリごとに分ける"""
    with dot.subgraph(name=f"cluster_{name}") as sub:
        sub.attr(label=name, labelloc="t", labeljust="l", style="filled", fillcolor=color, penwidth="1.5")

        # カテゴリごとにノードを追加
        for category in sorted(screens.keys()):
            screen_list = screens[category]
            category_color = lighten_color(color)
            with sub.subgraph(name=f"cluster_{name}_{category}") as subcat:
                subcat.attr(label=category, labelloc="t", labeljust="c", style="filled", fillcolor=category_color, penwidth="1.0", rankdir="LR")
                for screen in screen_list:
                    add_node_to_subgraph(subcat, screen, prefix)

                # 判定ノードもカテゴリ内に表示するために、transitionsから判定ノードを抽出して追加
                for transition_key in sorted(transitions.keys()):
                    transition_list = transitions[transition_key]
                    for src, dst, _ in transition_list:
                        if "判定_" in src and src not in screen_list:
                            add_node_to_subgraph(subcat, src, prefix)
                        if "判定_" in dst and dst not in screen_list:
                            add_node_to_subgraph(subcat, dst, prefix)

        # 判定ノードが他のカテゴリに入らないようにする
        for transition_key in sorted(transitions.keys()):
            transition_list = transitions[transition_key]
            for src, dst, _ in transition_list:
                if "判定_" in src:
                    add_node_to_subgraph(sub, src, prefix)
                if "判定_" in dst:
                    add_node_to_subgraph(sub, dst, prefix)

        # 横並びにするためのロジックを追加
        for transition_key in sorted(transitions.keys()):
            transition_list = transitions[transition_key]
            for i, (src, dst, _) in enumerate(transition_list[:-1]):
                next_src, next_dst, _ = transition_list[i + 1]
                if len(src) + len(dst) <= len(name):
                    sub.edge(prefix + src, prefix + dst, constraint="false")
                    sub.edge(prefix + dst, prefix + next_src, constraint="false")

        add_edges(sub, transitions, prefix)

def add_node_to_subgraph(sub, screen, prefix):
    """サブグラフにノードを追加する"""
    unique_screen_name = prefix + screen
    clean_screen_name = screen.replace("判定_", "")

    # 判定ノードは楕円（ellipse）、通常のノードはボックス
    shape = "ellipse" if "判定_" in screen else "box"
    
    sub.node(unique_screen_name, clean_screen_name, shape=shape,
             style="filled", fillcolor="white", fontsize="12", fontname="Helvetica Neue", width="1.2", height="0.5")

def add_edges(sub, transitions, prefix):
    """遷移を追加し、重複を防ぐ"""
    edge_attrs = {
        "fontsize": "10",
        "penwidth": "2",
        "color": "#5B9BD5",
        "arrowhead": "vee"
    }
    seen_edges = set()

    for transition_key in sorted(transitions.keys()):
        transition_list = transitions[transition_key]
        for src, dst, label in transition_list:
            add_edge_if_unique(sub, src, dst, label, prefix, edge_attrs, seen_edges)

def add_edge_if_unique(sub, src, dst, label, prefix, edge_attrs, seen_edges):
    """重複しない場合にエッジを追加する"""
    src_unique, dst_unique = prefix + src, prefix + dst
    edge_key = (src_unique, dst_unique, label)
    if edge_key not in seen_edges:
        sub.edge(src_unique, dst_unique, label=label, **edge_attrs)
        seen_edges.add(edge_key)

def render_group_transition(group_name, group_info):
    """グループごとにページを作成してレンダリングする"""
    dot = initialize_dot()
    create_subgraph(dot, group_name, group_info["screens"], group_info["prefix"], group_info["color"], group_info["transitions"])
    dot.render(f"image/{group_name}_画面遷移図", view=True)

def main():
    """メイン処理を実行する"""
    for group_name in sorted(groups.keys()):
        group_info = groups[group_name]
        render_group_transition(group_name, group_info)

if __name__ == "__main__":
    main()
