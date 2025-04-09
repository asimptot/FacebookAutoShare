import sys
from init import *
from random import choice, sample
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

sys.path.append(r'C:\\Projects\\Facebook')
warnings.filterwarnings("ignore")

class Run:
    def setup(self):
        Setup.login(self)

    def post_item(self):
        sleep(4)

        groups = ["195742787646435", "629130403874861", "768029116612189", "420431268067377", "793360724080335",
                  "1410315885953010", "136508183210007", "marktplaatsnlenbe", "2918595698424887", "1485751045065290",
                  "485352805721016", "1149152901844716", "tweedehandsluc", "442322749557851", "1088508761166230",
                  "1920637111500562", "marktplaatsnlmpnl", "268531743485977", "950522088792363", "1564639383826014",
                  "344791418984909", "161788287353160", "409106342615124", "2dehands.belgie", "966726273448368",
                  "632371976948574", "144240095700637", "2420262874940317", "861540603997127", "497303997101254",
                  "417764385080191", "432802303464167", "333715203672619", "1448915402047557", "1405452759783161",
                  "TweedehandsengratisRoeselareenomstreken", "731336060305864", "874788459284416", "923020344377453",
                  "1432281567044238", "2ehandszeeland", "953203612601945", "610444195707697", "1430621307028508",
                  "856792697734553", "201647150335175", "132409403523019", "594385470573669", "tweedehandsdeinze",
                  "239692296169869", "175607979463810", "1597007657000468", "321752647879069", "557397854315859",
                  "1507611012873851", "785372088208185", "1545437155676813", "424944358378148", "342556525881120",
                  "1482011298748374", "836022013155968", "793793673982223", "407197882715546", "789742497839331",
                  "2002253650000390", "1436279473250275", "1914615218850249", "707801016048113", "711206576644538",
                  "908137912592550", "238072409715158", "400160106827399", "250081978530721",
                  "1450815345173542", "1306847489430275", "1667381546888502"
                  ]

        # 🔥 GRILL POST
        # image = "grill.jpg"
        # description = "Een licht gebruikte Ikea-grill, perfect voor zomerse barbecues. Wordt geleverd met alle accessoires. De prijs is 120€. De locatie is Rilland/Zeeland."

        # 💡 HANGLAMP POST
        image = "lamp.jpg"
        description = "Een stijlvolle hanglamp in goede staat, perfect voor elke kamer. Gratis op te halen in Rilland/Zeeland."

        for group_id in groups:
            group_url = f'https://www.facebook.com/groups/{group_id}/buy_sell_discussion'
            self.browser.get(group_url)
            print('Posting on Facebook group: ', group_url)
            sleep(2)

            Setup.ready_for_post(self, image, description)
            sleep(5)
            Setup.send_post(self)


    def close_browser(self):
        self.browser.close()


r = Run()
r.setup()
r.post_item()
r.close_browser()