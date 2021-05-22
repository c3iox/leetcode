from typing import List

import typer
from loguru import logger


app = typer.Typer()


@app.command()
def max_profit(prices: List[int]) -> int:
    """
    给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。

    你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。

    返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock
    """
    # 什么都不买则是0
    ans = 0
    for buy in range(len(prices)):
        for sell in range(buy + 1, len(prices)):
            profit = prices[sell] - prices[buy]
            logger.debug(f"{sell=},{buy=},{profit=}")
            ans = max(profit, ans)

    logger.debug(f"{ans=}")
    return ans


if __name__ == "__main__":
    app()
