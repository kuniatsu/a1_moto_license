#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import re

def extract_keyword(question_text):
    """問題文から最も重要なキーワードを抽出"""
    if not question_text:
        return ""
    
    # 重要なキーワードの優先順位リスト
    keyword_patterns = [
        # 車両関連
        r'\bxe\s+mô\s+tô\b',  # xe mô tô (バイク)
        r'\bxe\s+đạp\b',      # xe đạp (自転車)
        r'\bxe\s+con\b',      # xe con (乗用車)
        r'\bxe\s+tải\b',      # xe tải (トラック)
        r'\bxe\s+khách\b',    # xe khách (バス)
        r'\bxe\s+cứu\s+thương\b',  # xe cứu thương (救急車)
        r'\bxe\s+cứu\s+hoả\b',     # xe cứu hoả (消防車)
        r'\bxe\s+quân\s+sự\b',     # xe quân sự (軍車)
        r'\bxe\s+công\s+an\b',     # xe công an (警察車)
        
        # 速度関連
        r'\btốc\s+độ\b',      # tốc độ (速度)
        r'\btối\s+đa\b',      # tối đa (最大)
        r'\btối\s+thiểu\b',   # tối thiểu (最小)
        
        # 標識関連
        r'\bbiển\b',          # biển (標識)
        r'\bbiển\s+báo\b',    # biển báo (標識)
        r'\bbiển\s+cấm\b',   # biển cấm (禁止標識)
        r'\bbiển\s+nguy\s+hiểm\b',  # biển nguy hiểm (危険標識)
        r'\bbiển\s+chỉ\s+dẫn\b',    # biển chỉ dẫn (案内標識)
        
        # 交通関連
        r'\bgiao\s+thông\b',  # giao thông (交通)
        r'\bgiao\s+nha\b',    # giao nhau (交差点)
        r'\bđường\s+sắt\b',   # đường sắt (鉄道)
        r'\bđường\s+bộ\b',    # đường bộ (道路)
        r'\bđường\s+cao\s+tốc\b',  # đường cao tốc (高速道路)
        
        # 安全関連
        r'\ban\s+toàn\b',     # an toàn (安全)
        r'\bnguy\s+hiểm\b',   # nguy hiểm (危険)
        r'\bphanh\b',         # phanh (ブレーキ)
        r'\bmũ\s+bảo\s+hiểm\b',  # mũ bảo hiểm (ヘルメット)
        
        # 禁止・違反関連
        r'\bcấm\b',          # cấm (禁止)
        r'\bvi\s+phạm\b',    # vi phạm (違反)
        r'\bnghiêm\s+cấm\b', # nghiêm cấm (厳禁)
        
        # 優先順位関連
        r'\bưu\s+tiên\b',    # ưu tiên (優先)
        r'\bthứ\s+tự\b',     # thứ tự (順序)
        
        # その他重要な単語
        r'\bđèn\b',          # đèn (信号)
        r'\bcòi\b',          # còi (クラクション)
        r'\bgiấy\s+phép\b',  # giấy phép (免許)
        r'\bđăng\s+ký\b',    # đăng ký (登録)
        r'\bkiểm\s+định\b',  # kiểm định (検査)
        r'\bbảo\s+hiểm\b',   # bảo hiểm (保険)
    ]
    
    # 問題文を小文字に変換して検索
    text_lower = question_text.lower()
    
    # パターンにマッチするキーワードを探す
    for pattern in keyword_patterns:
        matches = re.findall(pattern, text_lower)
        if matches:
            # 最初にマッチしたキーワードを返す
            return matches[0].strip()
    
    # マッチしない場合は、問題文から重要な単語を抽出
    # 一般的な単語を除外
    stop_words = {
        'câu', 'trong', 'các', 'dưới', 'đây', 'nào', 'là', 'có', 'được', 'phép',
        'điều', 'khiển', 'tham', 'gia', 'phải', 'như', 'thế', 'đúng', 'quy', 'tắc',
        'người', 'lái', 'xe', 'khi', 'gặp', 'hiệu', 'lệnh', 'của', 'cảnh', 'sát',
        'những', 'xe', 'nào', 'vi', 'phạm', 'quy', 'tắc', 'giao', 'thông'
    }
    
    # 単語を抽出（2文字以上の単語のみ）
    words = re.findall(r'\b\w{2,}\b', text_lower)
    
    # ストップワードを除外して重要な単語を探す
    for word in words:
        if word not in stop_words and len(word) >= 3:
            return word
    
    # それでも見つからない場合は最初の単語を返す
    if words:
        return words[0]
    
    return ""

def main():
    # JSONファイルを読み込み
    with open('a1Text.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # 各問題にキーワードを追加
    for item in data:
        if 'question_text' in item:
            keyword = extract_keyword(item['question_text'])
            item['keyword'] = keyword
    
    # 更新したデータをファイルに書き戻し
    with open('a1Text.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"各問題にキーワードを追加しました。")
    print(f"総問題数: {len(data)}")
    
    # キーワードの例を表示
    print("\nキーワードの例:")
    for i, item in enumerate(data[:10]):
        if 'keyword' in item:
            print(f"問題 {item['question_number']}: {item['keyword']}")

if __name__ == "__main__":
    main()
