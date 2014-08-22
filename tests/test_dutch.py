import unittest
from swissdutch.dutch import DutchPairingEngine
from swissdutch.constants import FideTitle, Colour, FloatStatus
from swissdutch.pairing import PairingCard

class Test_DutchPairingEngine(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.engine = DutchPairingEngine()

    def test_pair_second_round(self):
        input_pairing_cards = (
            PairingCard(surname='Carlsen',
                        rating=2900,
                        title=FideTitle.GM,
                        pairing_no=1,
                        score=1,
                        opponents=(4,),
                        colour_hist=(Colour.white,)),
            PairingCard(surname='Aronian',
                        rating=2800,
                        title=FideTitle.GM,
                        pairing_no=2,
                        score=1,
                        opponents=(5,),
                        colour_hist=(Colour.black,)),
            PairingCard(surname='Silman',
                        rating=2400,
                        title=FideTitle.IM,
                        pairing_no=3,
                        score=1,
                        opponents=(6,),
                        colour_hist=(Colour.white,)),
            PairingCard(surname='Jones',
                        rating=2200,
                        title=FideTitle.WIM,
                        pairing_no=4,
                        score=0,
                        opponents=(1,),
                        colour_hist=(Colour.black,)),
            PairingCard(surname='Smith',
                        rating=2200,
                        title=FideTitle.CM,
                        pairing_no=5,
                        score=0,
                        opponents=(2,),
                        colour_hist=(Colour.white,)),
            PairingCard(surname='Adams',
                        rating=1200,
                        title=None,
                        pairing_no=6,
                        score=0,
                        opponents=(3,),
                        colour_hist=(Colour.black,)),
            PairingCard(surname='Bernstein',
                        rating=1200,
                        title=None,
                        pairing_no=7,
                        score=1,
                        float_status=FloatStatus.down,
                        opponents=(0,),
                        colour_hist=(Colour.none,))
        )
        expected_pairing_cards = [
            PairingCard(surname='Carlsen',
                        rating=2900,
                        title=FideTitle.GM,
                        pairing_no=1,
                        score=1,
                        opponents=(4,),
                        colour_hist=(Colour.white,)),
            PairingCard(surname='Aronian',
                        rating=2800,
                        title=FideTitle.GM,
                        pairing_no=2,
                        score=1,
                        opponents=(5,),
                        colour_hist=(Colour.black,)),
            PairingCard(surname='Silman',
                        rating=2400,
                        title=FideTitle.IM,
                        pairing_no=3,
                        score=1,
                        opponents=(6,),
                        colour_hist=(Colour.white,)),
            PairingCard(surname='Jones',
                        rating=2200,
                        title=FideTitle.WIM,
                        pairing_no=4,
                        score=0,
                        opponents=(1,),
                        colour_hist=(Colour.black,)),
            PairingCard(surname='Smith',
                        rating=2200,
                        title=FideTitle.CM,
                        pairing_no=5,
                        score=0,
                        opponents=(2,),
                        colour_hist=(Colour.white,)),
            PairingCard(surname='Adams',
                        rating=1200,
                        title=None,
                        pairing_no=6,
                        score=0,
                        opponents=(3,),
                        colour_hist=(Colour.black,)),
            PairingCard(surname='Bernstein',
                        rating=1200,
                        title=None,
                        pairing_no=7,
                        score=1,
                        float_status=FloatStatus.downPrev,
                        opponents=(0,),
                        colour_hist=(Colour.none,))
        ]

        result_pairing_cards = self.engine.pair_round(2, input_pairing_cards)
        self.assertEqual(result_pairing_cards, expected_pairing_cards)