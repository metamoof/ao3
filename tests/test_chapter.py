from ao3.chapter import Chapter


def test_chapter_number():
    ch = Chapter(23452549)  # this only has one chapter
    assert ch.number == 1
