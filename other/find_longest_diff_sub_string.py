import typer
from loguru import logger

app = typer.Typer()


@app.command()
def find_longest_diff_sub_string(content: str) -> str:
    """多个相同的最长 保留最后一个"""
    if not isinstance(content, str):
        return ""

    longest_start, longest_end = 0, 0
    current_start, current_end = 0, 0

    for current_start, start_value in enumerate(content):
        logger.debug(f"{current_start=},{start_value=}")
        current_end_start = current_start + 1
        for current_end, end_value in enumerate(
            content[current_end_start:], current_end_start
        ):
            logger.debug(f"{current_end=},{end_value=}")
            # 遍历从start开始，到有重复元素终止
            if len(content[current_start : current_end + 1]) > len(
                set(content[current_start : current_end + 1])
            ):
                break
        else:
            current_end += 1
        current_end -= 1
        logger.debug(f"x -> {current_end=},{current_start=}")
        if current_end - current_start >= longest_end - longest_start:
            longest_start, longest_end = current_start, current_end
    logger.debug(f"r -> {longest_end=},{longest_start=}")
    ret = content[longest_start : longest_end + 1]
    logger.debug(f"longest:{ret}")

    return ret


if __name__ == "__main__":
    app()
