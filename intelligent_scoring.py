# -*- coding: utf-8 -*-
"""
智能评分引擎
"""


class IntelligentScoring:
    """智能评分引擎"""

    def __init__(self):
        pass

    def score_stock(self, stock_data, first_board_result, fundamental_result):
        """
        综合评分

        评分维度：
        1. 首板质量（技术面） - 30分
        2. 基本面利好 - 30分
        3. 新闻舆情 - 20分
        4. 资金流向 - 15分
        5. 市场热度 - 5分
        """
        score = 0
        details = {}

        # 1. 首板质量（30分）
        if first_board_result.get('首板', False):
            score += 30
            冲 = first_board_result.get('冲', 0)
            实体 = first_board_result.get('实体', 0)
            details['首板质量'] = f"✅ 符合 (冲:{冲:.2%}, 实体:{实体:.2%})"

            # 首板内部加分
            if 冲 >= 0.095:
                score += 5
        else:
            details['首板质量'] = "❌ 不符合"

        # 2. 基本面（30分，从fundamental_result的score缩放）
        fundamental_score = fundamental_result.get('score', 0)
        score += fundamental_score * 0.3
        details['基本面'] = {
            'score': fundamental_score,
            'reasons': fundamental_result.get('reasons', []),
            'warnings': fundamental_result.get('warnings', [])
        }

        # 3. 新闻舆情（从fundamental_result获取）
        good_news_count = len(fundamental_result.get('good_news', []))
        if good_news_count > 0:
            sentiment_score = min(20, good_news_count * 5)
            score += sentiment_score
            details['舆情'] = f"利好公告:{good_news_count}条"
        else:
            details['舆情'] = "无明显利好"

        # 4. 涨幅热度（5分）
        change = stock_data.get('change', 0)
        if change >= 0.098:
            score += 5
            details['热度'] = "🔥 接近涨停"
        elif change >= 0.08:
            score += 3
            details['热度'] = "📈 强势"
        else:
            details['热度'] = f"涨幅 {change:.2%}"

        # 5. 市盈率调整
        pe = stock_data.get('pe', 0)
        if pe and 10 <= pe <= 30:
            score += 5
            details['估值'] = f"✅ PE合理 ({pe:.1f})"
        elif pe and pe > 50:
            score -= 10
            details['估值'] = f"⚠️ PE偏高 ({pe:.1f})"

        # 确保分数在0-100
        score = max(0, min(100, score))

        return {
            'final_score': score,
            'details': details
        }
