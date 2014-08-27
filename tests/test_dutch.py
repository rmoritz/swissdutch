import unittest
from swissdutch.dutch import DutchPairingEngine
from swissdutch.constants import FideTitle, Colour, FloatStatus
from swissdutch.pairing import Player

class Test_DutchPairingEngine(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.engine  = DutchPairingEngine()

    def test_pair_2nd_round(self):
        input_players = (
            Player(name='Alice',
                   rating=2500,
                   title=FideTitle.GM,
                   pairing_no=1,
                   score=1,
                   float_status=FloatStatus.none,
                   opponents=(8,),
                   colour_hist=(Colour.white,)),
            Player(name='Bruno',
                   rating=2500,
                   title=FideTitle.IM,
                   pairing_no=2,
                   score=1,
                   float_status=FloatStatus.none,
                   opponents=(9,),
                   colour_hist=(Colour.black,)),
            Player(name='Carla',
                   rating=2400,
                   title=FideTitle.WGM,
                   pairing_no=3,
                   score=1,
                   float_status=FloatStatus.none,
                   opponents=(10,),
                   colour_hist=(Colour.white,)),
            Player(name='David',
                   rating=2400,
                   title=FideTitle.FM,
                   pairing_no=4,
                   score=0.5,
                   float_status=FloatStatus.none,
                   opponents=(11,),
                   colour_hist=(Colour.black,)),
            Player(name='Eloise',
                   rating=2350,
                   title=FideTitle.WIM,
                   pairing_no=5,
                   score=1,
                   float_status=FloatStatus.none,
                   opponents=(12,),
                   colour_hist=(Colour.white,)),
            Player(name='Finn',
                   rating=2300,
                   title=FideTitle.FM,
                   pairing_no=6,
                   score=1,
                   float_status=FloatStatus.none,
                   opponents=(13,),
                   colour_hist=(Colour.black,)),
            Player(name='Giorgia',
                   rating=2250,
                   title=FideTitle.FM,
                   pairing_no=7,
                   score=1,
                   float_status=FloatStatus.none,
                   opponents=(14,),
                   colour_hist=(Colour.white,)),
            Player(name='Kevin',
                   rating=2250,
                   title=FideTitle.FM,
                   pairing_no=8,
                   score=0,
                   float_status=FloatStatus.none,
                   opponents=(1,),
                   colour_hist=(Colour.black,)),
            Player(name='Louise',
                   rating=2150,
                   title=FideTitle.WIM,
                   pairing_no=9,
                   score=0,
                   float_status=FloatStatus.none,
                   opponents=(2,),
                   colour_hist=(Colour.white,)),
            Player(name='Mark',
                   rating=2150,
                   title=FideTitle.CM,
                   pairing_no=10,
                   score=0,
                   float_status=FloatStatus.none,
                   opponents=(3,),
                   colour_hist=(Colour.black,)),
            Player(name='Nancy',
                   rating=2100,
                   title=FideTitle.WFM,
                   pairing_no=11,
                   score=0.5,
                   float_status=FloatStatus.none,
                   opponents=(4,),
                   colour_hist=(Colour.white,)),
            Player(name='Patricia',
                   rating=2050,
                   title=0,
                   pairing_no=13,
                   score=0,
                   float_status=FloatStatus.none,
                   opponents=(6,),
                   colour_hist=(Colour.white,)),
            Player(name='Robert',
                   rating=2000,
                   title=0,
                   pairing_no=14,
                   score=0,
                   float_status=FloatStatus.none,
                   opponents=(7,),
                   colour_hist=(Colour.black,))
        )
        expected_players = [
            Player(name='Alice',
                   rating=2500,
                   title=FideTitle.GM,
                   pairing_no=1,
                   score=1,
                   float_status=FloatStatus.none,
                   opponents=(8, 5),
                   colour_hist=(Colour.white, Colour.black)),
            Player(name='Bruno',
                   rating=2500,
                   title=FideTitle.IM,
                   pairing_no=2,
                   score=1,
                   float_status=FloatStatus.none,
                   opponents=(9, 7),
                   colour_hist=(Colour.black, Colour.white)),
            Player(name='Carla',
                   rating=2400,
                   title=FideTitle.WGM,
                   pairing_no=3,
                   score=1,
                   float_status=FloatStatus.none,
                   opponents=(10, 6),
                   colour_hist=(Colour.white, Colour.black)),
            Player(name='David',
                   rating=2400,
                   title=FideTitle.FM,
                   pairing_no=4,
                   score=0.5,
                   float_status=FloatStatus.down,
                   opponents=(11, 9),
                   colour_hist=(Colour.black, Colour.white)),
            Player(name='Eloise',
                   rating=2350,
                   title=FideTitle.WIM,
                   pairing_no=5,
                   score=1,
                   float_status=FloatStatus.none,
                   opponents=(12, 1),
                   colour_hist=(Colour.white, Colour.white)),
            Player(name='Finn',
                   rating=2300,
                   title=FideTitle.FM,
                   pairing_no=6,
                   score=1,
                   float_status=FloatStatus.none,
                   opponents=(13, 3),
                   colour_hist=(Colour.black, Colour.white)),
            Player(name='Giorgia',
                   rating=2250,
                   title=FideTitle.FM,
                   pairing_no=7,
                   score=1,
                   float_status=FloatStatus.none,
                   opponents=(14, 2),
                   colour_hist=(Colour.white, Colour.black)),
            Player(name='Kevin',
                   rating=2250,
                   title=FideTitle.FM,
                   pairing_no=8,
                   score=0,
                   float_status=FloatStatus.up,
                   opponents=(1, 11),
                   colour_hist=(Colour.black, Colour.white)),
            Player(name='Louise',
                   rating=2150,
                   title=FideTitle.WIM,
                   pairing_no=9,
                   score=0,
                   float_status=FloatStatus.up,
                   opponents=(2, 4),
                   colour_hist=(Colour.white, Colour.black)),
            Player(name='Mark',
                   rating=2150,
                   title=FideTitle.CM,
                   pairing_no=10,
                   score=0,
                   float_status=FloatStatus.none,
                   opponents=(3, 13),
                   colour_hist=(Colour.black, Colour.white)),
            Player(name='Nancy',
                   rating=2100,
                   title=FideTitle.WFM,
                   pairing_no=11,
                   score=0.5,
                   float_status=FloatStatus.down,
                   opponents=(4, 8),
                   colour_hist=(Colour.white, Colour.black)),
            Player(name='Patricia',
                   rating=2050,
                   title=0,
                   pairing_no=13,
                   score=0,
                   float_status=FloatStatus.none,
                   opponents=(6, 10),
                   colour_hist=(Colour.white, Colour.black)),
            Player(name='Robert',
                   rating=2000,
                   title=0,
                   pairing_no=14,
                   score=1,
                   float_status=FloatStatus.down,
                   opponents=(7, 0),
                   colour_hist=(Colour.black, Colour.none))
        ]

        result_players = self.engine.pair_round(2, input_players)
        self.assertCountEqual(result_players, expected_players)

    def test_pair_3rd_round(self):
        input_players = (
            Player(name='Alice',
                   rating=2500,
                   title=FideTitle.GM,
                   pairing_no=1,
                   score=1,
                   float_status=FloatStatus.none,
                   opponents=(8, 5),
                   colour_hist=(Colour.white, Colour.black)),
            Player(name='Bruno',
                   rating=2500,
                   title=FideTitle.IM,
                   pairing_no=2,
                   score=2,
                   float_status=FloatStatus.none,
                   opponents=(9, 7),
                   colour_hist=(Colour.black, Colour.white)),
            Player(name='Carla',
                   rating=2400,
                   title=FideTitle.WGM,
                   pairing_no=3,
                   score=1.5,
                   float_status=FloatStatus.none,
                   opponents=(10, 6),
                   colour_hist=(Colour.white, Colour.black)),
            Player(name='David',
                   rating=2400,
                   title=FideTitle.FM,
                   pairing_no=4,
                   score=1.5,
                   float_status=FloatStatus.down,
                   opponents=(11, 9),
                   colour_hist=(Colour.black, Colour.white)),
            Player(name='Eloise',
                   rating=2350,
                   title=FideTitle.WIM,
                   pairing_no=5,
                   score=2,
                   float_status=FloatStatus.none,
                   opponents=(12, 1),
                   colour_hist=(Colour.white, Colour.white)),
            Player(name='Finn',
                   rating=2300,
                   title=FideTitle.FM,
                   pairing_no=6,
                   score=1.5,
                   float_status=FloatStatus.none,
                   opponents=(13, 3),
                   colour_hist=(Colour.black, Colour.white)),
            Player(name='Giorgia',
                   rating=2250,
                   title=FideTitle.FM,
                   pairing_no=7,
                   score=1,
                   float_status=FloatStatus.none,
                   opponents=(14, 2),
                   colour_hist=(Colour.white, Colour.black)),
            Player(name='Kevin',
                   rating=2250,
                   title=FideTitle.FM,
                   pairing_no=8,
                   score=0,
                   float_status=FloatStatus.up,
                   opponents=(1, 11),
                   colour_hist=(Colour.black, Colour.white)),
            Player(name='Louise',
                   rating=2150,
                   title=FideTitle.WIM,
                   pairing_no=9,
                   score=0,
                   float_status=FloatStatus.up,
                   opponents=(2, 4),
                   colour_hist=(Colour.white, Colour.black)),
            Player(name='Mark',
                   rating=2150,
                   title=FideTitle.CM,
                   pairing_no=10,
                   score=1,
                   float_status=FloatStatus.none,
                   opponents=(3, 13),
                   colour_hist=(Colour.black, Colour.white)),
            Player(name='Nancy',
                   rating=2100,
                   title=FideTitle.WFM,
                   pairing_no=11,
                   score=1.5,
                   float_status=FloatStatus.down,
                   opponents=(4, 8),
                   colour_hist=(Colour.white, Colour.black)),
            Player(name='Oskar',
                   rating=2100,
                   title=0,
                   pairing_no=12,
                   score=0,
                   float_status=FloatStatus.none,
                   opponents=(5,0),
                   colour_hist=(Colour.black,Colour.none)),
            Player(name='Patricia',
                   rating=2050,
                   title=0,
                   pairing_no=13,
                   score=0,
                   float_status=FloatStatus.none,
                   opponents=(6, 10),
                   colour_hist=(Colour.white, Colour.black)),
            Player(name='Robert',
                   rating=2000,
                   title=0,
                   pairing_no=14,
                   score=1,
                   float_status=FloatStatus.down,
                   opponents=(7, 0),
                   colour_hist=(Colour.black, Colour.none))
        )
        expected_players = [
            Player(name='Alice',
                   rating=2500,
                   title=FideTitle.GM,
                   pairing_no=1,
                   score=1,
                   float_status=FloatStatus.none,
                   opponents=(8, 5, 14),
                   colour_hist=(Colour.white, Colour.black, Colour.black)),
            Player(name='Bruno',
                   rating=2500,
                   title=FideTitle.IM,
                   pairing_no=2,
                   score=2,
                   float_status=FloatStatus.none,
                   opponents=(9, 7, 5),
                   colour_hist=(Colour.black, Colour.white, Colour.white)),
            Player(name='Carla',
                   rating=2400,
                   title=FideTitle.WGM,
                   pairing_no=3,
                   score=1.5,
                   float_status=FloatStatus.none,
                   opponents=(10, 6, 4),
                   colour_hist=(Colour.white, Colour.black, Colour.white)),
            Player(name='David',
                   rating=2400,
                   title=FideTitle.FM,
                   pairing_no=4,
                   score=1.5,
                   float_status=FloatStatus.downPrev,
                   opponents=(11, 9, 3),
                   colour_hist=(Colour.black, Colour.white, Colour.black)),
            Player(name='Eloise',
                   rating=2350,
                   title=FideTitle.WIM,
                   pairing_no=5,
                   score=2,
                   float_status=FloatStatus.none,
                   opponents=(12, 1, 2),
                   colour_hist=(Colour.white, Colour.white, Colour.black)),
            Player(name='Finn',
                   rating=2300,
                   title=FideTitle.FM,
                   pairing_no=6,
                   score=1.5,
                   float_status=FloatStatus.none,
                   opponents=(13, 3, 11),
                   colour_hist=(Colour.black, Colour.white, Colour.black)),
            Player(name='Giorgia',
                   rating=2250,
                   title=FideTitle.FM,
                   pairing_no=7,
                   score=1,
                   float_status=FloatStatus.none,
                   opponents=(14, 2, 10),
                   colour_hist=(Colour.white, Colour.black, Colour.white)),
            Player(name='Kevin',
                   rating=2250,
                   title=FideTitle.FM,
                   pairing_no=8,
                   score=0,
                   float_status=FloatStatus.upPrev,
                   opponents=(1, 11, 12),
                   colour_hist=(Colour.black, Colour.white, Colour.black)),
            Player(name='Louise',
                   rating=2150,
                   title=FideTitle.WIM,
                   pairing_no=9,
                   score=0,
                   float_status=FloatStatus.upPrev,
                   opponents=(2, 4, 13),
                   colour_hist=(Colour.white, Colour.black, Colour.white)),
            Player(name='Mark',
                   rating=2150,
                   title=FideTitle.CM,
                   pairing_no=10,
                   score=1,
                   float_status=FloatStatus.none,
                   opponents=(3, 13, 7),
                   colour_hist=(Colour.black, Colour.white, Colour.black)),
            Player(name='Nancy',
                   rating=2100,
                   title=FideTitle.WFM,
                   pairing_no=11,
                   score=1.5,
                   float_status=FloatStatus.downPrev,
                   opponents=(4, 8, 6),
                   colour_hist=(Colour.white, Colour.black, Colour.white)),
            Player(name='Oskar',
                   rating=2100,
                   title=0,
                   pairing_no=12,
                   score=0,
                   float_status=FloatStatus.none,
                   opponents=(5, 0, 8),
                   colour_hist=(Colour.black, Colour.none, Colour.white)),
            Player(name='Patricia',
                   rating=2050,
                   title=0,
                   pairing_no=13,
                   score=0,
                   float_status=FloatStatus.none,
                   opponents=(6, 10, 9),
                   colour_hist=(Colour.white, Colour.black, Colour.black)),
            Player(name='Robert',
                   rating=2000,
                   title=0,
                   pairing_no=14,
                   score=1,
                   float_status=FloatStatus.downPrev,
                   opponents=(7, 0, 1),
                   colour_hist=(Colour.black, Colour.none, Colour.white))
        ]

        result_players = self.engine.pair_round(3, input_players)
        self.assertCountEqual(result_players, expected_players)

    def test_pair_4th_round(self):
        input_players = (
            Player(name='Alice',
                   rating=2500,
                   title=FideTitle.GM,
                   pairing_no=1,
                   score=2,
                   float_status=FloatStatus.none,
                   opponents=(8, 5, 14),
                   colour_hist=(Colour.white, Colour.black, Colour.black)),
            Player(name='Bruno',
                   rating=2500,
                   title=FideTitle.IM,
                   pairing_no=2,
                   score=2.5,
                   float_status=FloatStatus.none,
                   opponents=(9, 7, 5),
                   colour_hist=(Colour.black, Colour.white, Colour.white)),
            Player(name='Carla',
                   rating=2400,
                   title=FideTitle.WGM,
                   pairing_no=3,
                   score=2,
                   float_status=FloatStatus.none,
                   opponents=(10, 6, 4),
                   colour_hist=(Colour.white, Colour.black, Colour.white)),
            Player(name='David',
                   rating=2400,
                   title=FideTitle.FM,
                   pairing_no=4,
                   score=2,
                   float_status=FloatStatus.downPrev,
                   opponents=(11, 9, 3),
                   colour_hist=(Colour.black, Colour.white, Colour.black)),
            Player(name='Eloise',
                   rating=2350,
                   title=FideTitle.WIM,
                   pairing_no=5,
                   score=2.5,
                   float_status=FloatStatus.none,
                   opponents=(12, 1, 2),
                   colour_hist=(Colour.white, Colour.white, Colour.black)),
            Player(name='Finn',
                   rating=2300,
                   title=FideTitle.FM,
                   pairing_no=6,
                   score=2.5,
                   float_status=FloatStatus.down,
                   opponents=(13, 3, 0),
                   colour_hist=(Colour.black, Colour.white, Colour.none)),
            Player(name='Giorgia',
                   rating=2250,
                   title=FideTitle.FM,
                   pairing_no=7,
                   score=2,
                   float_status=FloatStatus.none,
                   opponents=(14, 2, 10),
                   colour_hist=(Colour.white, Colour.black, Colour.white)),
            Player(name='Kevin',
                   rating=2250,
                   title=FideTitle.FM,
                   pairing_no=8,
                   score=0.5,
                   float_status=FloatStatus.upPrev,
                   opponents=(1, 11, 12),
                   colour_hist=(Colour.black, Colour.white, Colour.black)),
            Player(name='Louise',
                   rating=2150,
                   title=FideTitle.WIM,
                   pairing_no=9,
                   score=1,
                   float_status=FloatStatus.upPrev,
                   opponents=(2, 4, 13),
                   colour_hist=(Colour.white, Colour.black, Colour.white)),
            Player(name='Mark',
                   rating=2150,
                   title=FideTitle.CM,
                   pairing_no=10,
                   score=1,
                   float_status=FloatStatus.none,
                   opponents=(3, 13, 7),
                   colour_hist=(Colour.black, Colour.white, Colour.black)),
            Player(name='Nancy',
                   rating=2100,
                   title=FideTitle.WFM,
                   pairing_no=11,
                   score=1.5,
                   float_status=FloatStatus.downPrev,
                   opponents=(4, 8, 0),
                   colour_hist=(Colour.white, Colour.black, Colour.none)),
            Player(name='Oskar',
                   rating=2100,
                   title=0,
                   pairing_no=12,
                   score=0.5,
                   float_status=FloatStatus.none,
                   opponents=(5, 0, 8),
                   colour_hist=(Colour.black, Colour.none, Colour.white)),
            Player(name='Patricia',
                   rating=2050,
                   title=0,
                   pairing_no=13,
                   score=0,
                   float_status=FloatStatus.none,
                   opponents=(6, 10, 9),
                   colour_hist=(Colour.white, Colour.black, Colour.black)),
            Player(name='Robert',
                   rating=2000,
                   title=0,
                   pairing_no=14,
                   score=1,
                   float_status=FloatStatus.downPrev,
                   opponents=(7, 0, 1),
                   colour_hist=(Colour.black, Colour.none, Colour.white))
        )
        expected_players = [
            Player(name='Alice',
                   rating=2500,
                   title=FideTitle.GM,
                   pairing_no=1,
                   score=2,
                   float_status=FloatStatus.none,
                   opponents=(8, 5, 14, 3),
                   colour_hist=(Colour.white, Colour.black, Colour.black,
                                Colour.white)),
            Player(name='Bruno',
                   rating=2500,
                   title=FideTitle.IM,
                   pairing_no=2,
                   score=2.5,
                   float_status=FloatStatus.none,
                   opponents=(9, 7, 5, 6),
                   colour_hist=(Colour.black, Colour.white, Colour.white,
                                Colour.black)),
            Player(name='Carla',
                   rating=2400,
                   title=FideTitle.WGM,
                   pairing_no=3,
                   score=2,
                   float_status=FloatStatus.none,
                   opponents=(10, 6, 4, 1),
                   colour_hist=(Colour.white, Colour.black, Colour.white,
                                Colour.black)),
            Player(name='David',
                   rating=2400,
                   title=FideTitle.FM,
                   pairing_no=4,
                   score=2,
                   float_status=FloatStatus.up,
                   opponents=(11, 9, 3, 5),
                   colour_hist=(Colour.black, Colour.white, Colour.black,
                                Colour.white)),
            Player(name='Eloise',
                   rating=2350,
                   title=FideTitle.WIM,
                   pairing_no=5,
                   score=2.5,
                   float_status=FloatStatus.down,
                   opponents=(12, 1, 2, 4),
                   colour_hist=(Colour.white, Colour.white, Colour.black,
                                Colour.black)),
            Player(name='Finn',
                   rating=2300,
                   title=FideTitle.FM,
                   pairing_no=6,
                   score=2.5,
                   float_status=FloatStatus.downPrev,
                   opponents=(13, 3, 0, 2),
                   colour_hist=(Colour.black, Colour.white, Colour.none,
                                Colour.white)),
            Player(name='Giorgia',
                   rating=2250,
                   title=FideTitle.FM,
                   pairing_no=7,
                   score=2,
                   float_status=FloatStatus.down,
                   opponents=(14, 2, 10, 11),
                   colour_hist=(Colour.white, Colour.black, Colour.white,
                                Colour.black)),
            Player(name='Kevin',
                   rating=2250,
                   title=FideTitle.FM,
                   pairing_no=8,
                   score=0.5,
                   float_status=FloatStatus.up,
                   opponents=(1, 11, 12, 9),
                   colour_hist=(Colour.black, Colour.white, Colour.black,
                                Colour.white)),
            Player(name='Louise',
                   rating=2150,
                   title=FideTitle.WIM,
                   pairing_no=9,
                   score=1,
                   float_status=FloatStatus.down,
                   opponents=(2, 4, 13, 8),
                   colour_hist=(Colour.white, Colour.black, Colour.white,
                                Colour.black)),
            Player(name='Mark',
                   rating=2150,
                   title=FideTitle.CM,
                   pairing_no=10,
                   score=1,
                   float_status=FloatStatus.none,
                   opponents=(3, 13, 7, 14),
                   colour_hist=(Colour.black, Colour.white, Colour.black,
                                Colour.white)),
            Player(name='Nancy',
                   rating=2100,
                   title=FideTitle.WFM,
                   pairing_no=11,
                   score=1.5,
                   float_status=FloatStatus.up,
                   opponents=(4, 8, 0, 7),
                   colour_hist=(Colour.white, Colour.black, Colour.none,
                                Colour.white)),
            Player(name='Oskar',
                   rating=2100,
                   title=0,
                   pairing_no=12,
                   score=0.5,
                   float_status=FloatStatus.down,
                   opponents=(5, 0, 8, 13),
                   colour_hist=(Colour.black, Colour.none, Colour.white,
                                Colour.black)),
            Player(name='Patricia',
                   rating=2050,
                   title=0,
                   pairing_no=13,
                   score=0,
                   float_status=FloatStatus.up,
                   opponents=(6, 10, 9, 12),
                   colour_hist=(Colour.white, Colour.black, Colour.black,
                                Colour.white)),
            Player(name='Robert',
                   rating=2000,
                   title=0,
                   pairing_no=14,
                   score=1,
                   float_status=FloatStatus.none,
                   opponents=(7, 0, 1, 10),
                   colour_hist=(Colour.black, Colour.none, Colour.white,
                                Colour.black))
        ]

        result_players = self.engine.pair_round(4, input_players)
        self.assertCountEqual(result_players, expected_players)

    @unittest.skip
    def test_pair_5th_round(self):
        input_players = (
            Player(name='Alice',
                   rating=2500,
                   title=FideTitle.GM,
                   pairing_no=1,
                   score=3,
                   float_status=FloatStatus.none,
                   opponents=(8, 5, 14, 3),
                   colour_hist=(Colour.white, Colour.black, Colour.black,
                                Colour.white)),
            Player(name='Bruno',
                   rating=2500,
                   title=FideTitle.IM,
                   pairing_no=2,
                   score=3.5,
                   float_status=FloatStatus.none,
                   opponents=(9, 7, 5, 6),
                   colour_hist=(Colour.black, Colour.white, Colour.white,
                                Colour.black)),
            Player(name='Carla',
                   rating=2400,
                   title=FideTitle.WGM,
                   pairing_no=3,
                   score=2,
                   float_status=FloatStatus.none,
                   opponents=(10, 6, 4, 1),
                   colour_hist=(Colour.white, Colour.black, Colour.white,
                                Colour.black)),
            Player(name='David',
                   rating=2400,
                   title=FideTitle.FM,
                   pairing_no=4,
                   score=2.5,
                   float_status=FloatStatus.up,
                   opponents=(11, 9, 3, 5),
                   colour_hist=(Colour.black, Colour.white, Colour.black,
                                Colour.white)),
            Player(name='Eloise',
                   rating=2350,
                   title=FideTitle.WIM,
                   pairing_no=5,
                   score=3,
                   float_status=FloatStatus.down,
                   opponents=(12, 1, 2, 4),
                   colour_hist=(Colour.white, Colour.white, Colour.black,
                                Colour.black)),
            Player(name='Finn',
                   rating=2300,
                   title=FideTitle.FM,
                   pairing_no=6,
                   score=2.5,
                   float_status=FloatStatus.downPrev,
                   opponents=(13, 3, 0, 2),
                   colour_hist=(Colour.black, Colour.white, Colour.none,
                                Colour.white)),
            Player(name='Giorgia',
                   rating=2250,
                   title=FideTitle.FM,
                   pairing_no=7,
                   score=2,
                   float_status=FloatStatus.down,
                   opponents=(14, 2, 10, 11),
                   colour_hist=(Colour.white, Colour.black, Colour.white,
                                Colour.black)),
            Player(name='Kevin',
                   rating=2250,
                   title=FideTitle.FM,
                   pairing_no=8,
                   score=1,
                   float_status=FloatStatus.up,
                   opponents=(1, 11, 12, 9),
                   colour_hist=(Colour.black, Colour.white, Colour.black,
                                Colour.white)),
            Player(name='Louise',
                   rating=2150,
                   title=FideTitle.WIM,
                   pairing_no=9,
                   score=1.5,
                   float_status=FloatStatus.down,
                   opponents=(2, 4, 13, 8),
                   colour_hist=(Colour.white, Colour.black, Colour.white,
                                Colour.black)),
            Player(name='Mark',
                   rating=2150,
                   title=FideTitle.CM,
                   pairing_no=10,
                   score=1.5,
                   float_status=FloatStatus.none,
                   opponents=(3, 13, 7, 14),
                   colour_hist=(Colour.black, Colour.white, Colour.black,
                                Colour.white)),
            Player(name='Nancy',
                   rating=2100,
                   title=FideTitle.WFM,
                   pairing_no=11,
                   score=2.5,
                   float_status=FloatStatus.up,
                   opponents=(4, 8, 0, 7),
                   colour_hist=(Colour.white, Colour.black, Colour.none,
                                Colour.white)),
            Player(name='Oskar',
                   rating=2100,
                   title=0,
                   pairing_no=12,
                   score=0.5,
                   float_status=FloatStatus.down,
                   opponents=(5, 0, 8, 13),
                   colour_hist=(Colour.black, Colour.none, Colour.white,
                                Colour.black)),
            Player(name='Patricia',
                   rating=2050,
                   title=0,
                   pairing_no=13,
                   score=1,
                   float_status=FloatStatus.up,
                   opponents=(6, 10, 9, 12),
                   colour_hist=(Colour.white, Colour.black, Colour.black,
                                Colour.white)),
            Player(name='Robert',
                   rating=2000,
                   title=0,
                   pairing_no=14,
                   score=1.5,
                   float_status=FloatStatus.none,
                   opponents=(7, 0, 1, 10),
                   colour_hist=(Colour.black, Colour.none, Colour.white,
                                Colour.black))
        )
        expected_players = [
            Player(name='Alice',
                   rating=2500,
                   title=FideTitle.GM,
                   pairing_no=1,
                   score=3,
                   float_status=FloatStatus.none,
                   opponents=(8, 5, 14, 3),
                   colour_hist=(Colour.white, Colour.black, Colour.black,
                                Colour.white)),
            Player(name='Bruno',
                   rating=2500,
                   title=FideTitle.IM,
                   pairing_no=2,
                   score=3.5,
                   float_status=FloatStatus.none,
                   opponents=(9, 7, 5, 6),
                   colour_hist=(Colour.black, Colour.white, Colour.white,
                                Colour.black)),
            Player(name='Carla',
                   rating=2400,
                   title=FideTitle.WGM,
                   pairing_no=3,
                   score=2,
                   float_status=FloatStatus.none,
                   opponents=(10, 6, 4, 1),
                   colour_hist=(Colour.white, Colour.black, Colour.white,
                                Colour.black)),
            Player(name='David',
                   rating=2400,
                   title=FideTitle.FM,
                   pairing_no=4,
                   score=2.5,
                   float_status=FloatStatus.up,
                   opponents=(11, 9, 3, 5),
                   colour_hist=(Colour.black, Colour.white, Colour.black,
                                Colour.white)),
            Player(name='Eloise',
                   rating=2350,
                   title=FideTitle.WIM,
                   pairing_no=5,
                   score=3,
                   float_status=FloatStatus.down,
                   opponents=(12, 1, 2, 4),
                   colour_hist=(Colour.white, Colour.white, Colour.black,
                                Colour.black)),
            Player(name='Finn',
                   rating=2300,
                   title=FideTitle.FM,
                   pairing_no=6,
                   score=2.5,
                   float_status=FloatStatus.downPrev,
                   opponents=(13, 3, 0, 2),
                   colour_hist=(Colour.black, Colour.white, Colour.none,
                                Colour.white)),
            Player(name='Giorgia',
                   rating=2250,
                   title=FideTitle.FM,
                   pairing_no=7,
                   score=2,
                   float_status=FloatStatus.down,
                   opponents=(14, 2, 10, 11),
                   colour_hist=(Colour.white, Colour.black, Colour.white,
                                Colour.black)),
            Player(name='Kevin',
                   rating=2250,
                   title=FideTitle.FM,
                   pairing_no=8,
                   score=1,
                   float_status=FloatStatus.up,
                   opponents=(1, 11, 12, 9),
                   colour_hist=(Colour.black, Colour.white, Colour.black,
                                Colour.white)),
            Player(name='Louise',
                   rating=2150,
                   title=FideTitle.WIM,
                   pairing_no=9,
                   score=1.5,
                   float_status=FloatStatus.down,
                   opponents=(2, 4, 13, 8),
                   colour_hist=(Colour.white, Colour.black, Colour.white,
                                Colour.black)),
            Player(name='Mark',
                   rating=2150,
                   title=FideTitle.CM,
                   pairing_no=10,
                   score=1.5,
                   float_status=FloatStatus.none,
                   opponents=(3, 13, 7, 14),
                   colour_hist=(Colour.black, Colour.white, Colour.black,
                                Colour.white)),
            Player(name='Nancy',
                   rating=2100,
                   title=FideTitle.WFM,
                   pairing_no=11,
                   score=2.5,
                   float_status=FloatStatus.up,
                   opponents=(4, 8, 0, 7),
                   colour_hist=(Colour.white, Colour.black, Colour.none,
                                Colour.white)),
            Player(name='Oskar',
                   rating=2100,
                   title=0,
                   pairing_no=12,
                   score=0.5,
                   float_status=FloatStatus.down,
                   opponents=(5, 0, 8, 13),
                   colour_hist=(Colour.black, Colour.none, Colour.white,
                                Colour.black)),
            Player(name='Patricia',
                   rating=2050,
                   title=0,
                   pairing_no=13,
                   score=1,
                   float_status=FloatStatus.up,
                   opponents=(6, 10, 9, 12),
                   colour_hist=(Colour.white, Colour.black, Colour.black,
                                Colour.white)),
            Player(name='Robert',
                   rating=2000,
                   title=0,
                   pairing_no=14,
                   score=1.5,
                   float_status=FloatStatus.none,
                   opponents=(7, 0, 1, 10),
                   colour_hist=(Colour.black, Colour.none, Colour.white,
                                Colour.black))
        ]

        result_players = self.engine.pair_round(5, input_players)
        self.assertCountEqual(result_players, expected_players)