# import pytest
from ao3 import AO3, utils


def test_basic_single_chapter_work():
    workid = utils.work_id_from_url(
            'https://archiveofourown.org/works/23452549')
    api = AO3()
    work = api.work(workid)
    assert work.id == workid
    assert work.title == '[Podfic] You Can Go South In My Downs by MostWeakHamlets'
    assert work.author == 'CompassRose'
    assert work.fandoms == ['Good Omens - Neil Gaiman & Terry Pratchett',
                            'Good Omens (TV)']
    assert work.language == 'English'
    assert work.rating == ['Mature']
    assert work.category == ['M/M']
    assert work.additional_tags == ["Rated M Just To Be Safe",
                                    "frottage in the cottage",
                                    "South Downs Cottage (Good Omens)",
                                    "Hickies",
                                    "they're retired and will enjoy their date nights godammit",
                                    "they're still soft in this",
                                    "there's some tender moments",
                                    "Podfic",
                                    "Podfic Length: 10-20 Minutes",
                                    "Very Dramatic Readings",
                                    "freetalk",
                                    "I just wanted to get my mouth on that tag ok",
                                    "and pronounce it wrong TWO ways!"]
    assert work.num_chapters == 1
    assert work.total_chapters == 1
    assert work.chapters.number == 1
    assert work.associations == [{
        'relation': 'Inspired by',
        'work': 'You Can Go South In My Downs',
        'author': 'MostWeakHamlets',
        'work_id': 23203033,
        'author_link': '/users/MostWeakHamlets/pseuds/MostWeakHamlets',
    }]
