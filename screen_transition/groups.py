groups = {
    "派遣契約管理": {
        "prefix": "派遣_",
        "screens": {
            "契約書管理": ["契約書一覧", "契約書作成", "契約書編集", "契約書レポート"],
            "契約締結": ["契約締結", "契約締結完了"]
        },
        "color": "#B3E0F2",
        "transitions": {
            "契約書処理": [
                ("契約書一覧", "契約書作成", "新規作成ボタン押下"),
                ("契約書一覧", "契約書編集", "編集ボタン押下"),
                ("契約書作成", "判定_契約書に問題がある", "登録ボタン押下"),
                ("契約書編集", "契約書一覧", "登録ボタン押下"),
                ("判定_契約書に問題がある", "契約書レポート", "はい"),
                ("判定_契約書に問題がある", "契約書一覧", "いいえ"),
                ("契約書レポート", "契約書編集", "編集ボタン押下"),
            ],
            "契約締結フロー": [
                ("契約締結", "契約締結完了", "署名後、契約締結ボタン押下"),
            ]
        }
    },
    "業務委託契約管理": {
        "prefix": "業務_",
        "screens": {
            "契約書管理": ["契約書一覧", "契約書作成", "契約書編集"],
            "契約締結": ["契約締結", "契約締結完了"],
            "発注管理": ["発注一覧", "発注書作成", "発注編集"],
            "請求管理": ["請求書一覧", "請求書作成", "請求書編集"],
            "支払い管理": ["支払い管理一覧", "支払い内容詳細", "支払い方法選択", "支払い内容確認", "支払い成功画面", "支払い失敗画面"]
        },
        "color": "#D5E8D4",
        "transitions": {
            "契約書処理": [
                ("契約書一覧", "契約書作成", "新規作成ボタン押下"),
                ("契約書一覧", "契約書編集", "編集ボタン押下"),
                ("契約書編集", "契約書一覧", "登録ボタン押下"),
            ],
            "契約締結フロー": [
                ("契約締結", "契約締結完了", "署名後、契約締結ボタン押下"),
            ],
            "発注処理": [
                ("発注一覧", "発注書作成", "新規作成ボタン押下"),
                ("発注一覧", "発注編集", "編集ボタン押下"),
                ("発注書作成", "発注一覧", "登録ボタン押下"),
                ("発注編集", "発注一覧", "登録ボタン押下"),
            ],
            "請求処理": [
                ("請求書一覧", "請求書作成", "新規作成ボタン押下"),
                ("請求書一覧", "請求書編集", "編集ボタン押下"),
                ("請求書作成", "請求書一覧", "登録ボタン押下"),
                ("請求書編集", "請求書一覧", "登録ボタン押下"),
            ],
            "支払いフロー": [
                ("支払い管理一覧", "支払い内容詳細", "詳細ボタン押下"),
                ("支払い内容詳細", "支払い管理一覧", "戻るボタン押下"),
                ("支払い管理一覧", "支払い方法選択", "支払いボタン押下"),
                ("支払い方法選択", "支払い内容確認", "登録ボタン押下"),
                ("支払い内容確認", "判定_支払いに成功した", "支払いボタン押下"),
                ("判定_支払いに成功した", "支払い成功画面", "はい"),
                ("判定_支払いに成功した", "支払い失敗画面", "いいえ"),
                ("支払い成功画面", "支払い管理一覧", "一覧に戻るボタン押下"),
                ("支払い失敗画面", "支払い管理一覧", "一覧に戻るボタン押下"),
            ]
        }
    },
    "AIマッチング": {
        "prefix": "AIマッチング_",
        "screens": {
            "案件管理": ["案件一覧", "案件作成", "案件詳細/編集"],
            "スタッフ管理": ["スタッフ一覧", "スタッフ新規登録", "スタッフ詳細/編集"],
            "マッチング": ["マッチング一覧", "マッチング詳細", "マッチング実施", "面談日程調整", "分析"],
        },
        "color": "#FFD700",
        "transitions": {
            "案件管理": [
                ("案件一覧", "案件作成", "新規作成ボタン押下"),
                ("案件一覧", "案件詳細/編集", "詳細ボタン押下"),
                ("案件詳細/編集", "案件一覧", "戻る or 登録ボタン押下"),
            ],
            "スタッフ管理": [
                ("スタッフ一覧", "スタッフ新規登録", "新規作成ボタン押下"),
                ("スタッフ一覧", "スタッフ詳細/編集", "詳細ボタン押下"),
                ("スタッフ新規登録", "スタッフ一覧", "登録ボタン押下"),
                ("スタッフ詳細/編集", "スタッフ一覧", "戻る or 登録ボタン押下"),
            ],
            "マッチング": [
                ("マッチング一覧", "マッチング詳細", "詳細ボタン押下"),
                ("マッチング一覧", "マッチング実施", "マッチングボタン押下"),
                ("マッチング詳細", "マッチング一覧", "戻るボタン押下"),
                ("マッチング実施", "マッチング一覧", "戻るボタン押下"),
            ],
        }
    },
    "PRM": {
        "prefix": "PRM_",
        "screens": {
            "パートナー管理（派遣会社・業務委託先）": ["パートナー一覧", "パートナー詳細", "FB実施", "取引実績分析"],
            "エンゲージメント": ["KPIダッシュボード", "営業フォロー", "チャット"],
            "パートナーポータル": ["ホーム", "ドキュメント共有"],
            "案件管理（SFA）": ["共有案件管理", "CRM連携", "顧客一覧", "顧客詳細", "分析", "フォローアップリスト"],
        },
        "color": "#B3E0F2",
        "transitions": {
            "パートナー管理（派遣会社・業務委託先）": [
                ("パートナー一覧", "パートナー詳細", "詳細ボタン押下"),
                ("パートナー詳細", "FB実施", "FBボタン押下"),
            ],
        }
    },
    "LMS": {
        "prefix": "LMS_",
        "screens": {
            "研修": ["研修一覧", "研修新規作成", "研修詳細/編集", "受講状況管理"],
            "テスト": ["テスト一覧", "テスト新規登録", "テスト詳細/編集", 
                    "テスト受験", "テスト受験結果",
                    "定着度理解テスト受験", "定着度理解テスト受験結果"
                    ],
            "ダッシュボード": ["パートナースタッフ"],
        },
        "color": "#B3E0F2",
        "transitions": {
            "研修": [
                ("研修一覧", "研修新規作成", "新規作成ボタン押下"),
                ("研修一覧", "研修詳細/編集", "詳細ボタン押下"),
                ("研修新規作成", "研修一覧", "戻る or 登録ボタン押下"),
                ("研修詳細/編集", "研修一覧", "戻るボタン押下"),
            ],
            "テスト": [
                ("テスト一覧", "テスト新規登録", "新規登録ボタン押下"),
                ("テスト一覧", "テスト詳細/編集", "詳細ボタン押下"),
                ("テスト新規登録", "テスト一覧", "戻る or 登録ボタン押下"),
                ("テスト詳細/編集", "テスト一覧", "戻るボタン押下"),
                ("パートナースタッフ", "テスト受験", "受験ボタン押下"),
                ("パートナースタッフ", "定着度理解テスト受験", "受験ボタン押下"),
                ("テスト受験", "テスト受験結果", "採点ボタン押下"),
                ("定着度理解テスト受験", "定着度理解テスト受験結果", "採点ボタン押下"),
            ],
        }
    },
    "業務フロー": {
        "prefix": "業務フロー_",
        "screens": {
            "業務フロー": ["業務フロー一覧", "業務フロー詳細/編集", "業務フロー新規登録", "可視化", "配布"]
        },
        "color": "#B3E0F2",
        "transitions": {
            "業務フロー": [
                ("業務フロー一覧", "業務フロー新規登録", "新規登録ボタン押下"),
                ("業務フロー一覧", "業務フロー詳細/編集", "詳細ボタン押下"),
                ("業務フロー新規登録", "業務フロー一覧", "戻る or 登録ボタン押下"),
                ("業務フロー詳細/編集", "業務フロー一覧", "戻るボタン押下"),
            ],
        }
    },
    "その他": {
        "prefix": "その他_",
        "screens": {
            "リマインド（各種契約・請求）": ["リマインド一覧", "リマインド新規登録", "リマインド編集"],
            "ひな形": [
              "派遣契約書 一覧", "派遣契約書 新規登録", "派遣契約書 編集", # 派遣契約書
              "業務委託契約書 一覧", "業務委託契約書 新規登録", "業務委託契約書 編集", # 業務委託契約書
              "発注書 一覧", "発注書 新規登録", "発注書 編集", # 発注書
              "請求書 一覧", "請求書 新規登録", "請求書 編集", # 請求書
            ]
        },
        "color": "#F4A460",
        "transitions": {
            "リマインド（各種契約・請求）": [
                ("リマインド一覧", "リマインド新規登録", "新規登録ボタン押下"),
                ("リマインド一覧", "リマインド編集", "編集ボタン押下"),
                ("リマインド新規登録", "リマインド一覧", "登録ボタン押下"),
                ("リマインド編集", "リマインド一覧", "登録ボタン押下"),
            ],
            "雛形": [
                ("業務委託契約書 一覧", "業務委託契約書 新規登録", "新規登録ボタン押下"),
                ("業務委託契約書 一覧", "業務委託契約書 編集", "編集ボタン押下"),
                ("業務委託契約書 新規登録", "業務委託契約書 一覧", "登録ボタン押下"),
                ("業務委託契約書 編集", "業務委託契約書 一覧", "登録ボタン押下"),
                ("派遣契約書 一覧", "派遣契約書 新規登録", "新規登録ボタン押下"),
                ("派遣契約書 一覧", "派遣契約書 編集", "編集ボタン押下"),
                ("派遣契約書 新規登録", "派遣契約書 一覧", "登録ボタン押下"),
                ("派遣契約書 編集", "派遣契約書 一覧", "登録ボタン押下"),
                ("発注書 一覧", "発注書 新規登録", "新規登録ボタン押下"),
                ("発注書 一覧", "発注書 編集", "編集ボタン押下"),
                ("発注書 新規登録", "発注書 一覧", "登録ボタン押下"),
                ("発注書 編集", "発注書 一覧", "登録ボタン押下"),
                ("請求書 一覧", "請求書 新規登録", "新規登録ボタン押下"),
                ("請求書 一覧", "請求書 編集", "編集ボタン押下"),
                ("請求書 新規登録", "請求書 一覧", "登録ボタン押下"),
                ("請求書 編集", "請求書 一覧", "登録ボタン押下"),
            ],
        }
    },
}
